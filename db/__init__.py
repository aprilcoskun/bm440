from pydantic import BaseModel, Field
from datetime import datetime
import cx_Oracle


class Employee(BaseModel):
    tc: str
    name: str
    password: str
    title: str
    email: str = None
    phone: str = None


class Product(BaseModel):
    barcode: str
    name: str
    price: int
    stock: int


class Customer(BaseModel):
    tc: str
    name: str
    email: str = None
    phone: str = None


class Sale(BaseModel):
    customer_tc: str
    staff_tc: str
    sale_date: datetime = Field(default_factory=datetime.utcnow)
    product_barcode: int
    product_total: int


class DBConnection:
    _conn: cx_Oracle.Connection

    def __init__(self):
        self._connect_db()

    def get_employee(self, tc):
        data = self._execute_stmt("select * from staff where tc = :tc", tc=tc)[0]
        return Employee(**data)

    def get_all_staff(self):
        return self._execute_stmt("select * from staff")

    def get_all_products(self):
        return self._execute_stmt("select * from products")

    def get_products_by_barcode(self, barcode):
        return self._execute_stmt("select * from products where barcode like '%'||:barcode||'%'", barcode=barcode)

    def get_products_by_name(self, name):
        return self._execute_stmt("select * from products where name like '%'||:name||'%'", name=name)

    def get_all_customers(self):
        return self._execute_stmt("select * from customers")

    def insert_customer(self, customer: Customer):
        cur = self._conn.cursor()
        cur.callproc("insert_customer", (customer.tc, customer.name, customer.email, customer.phone))
        cur.close()
        return True

    def update_customer(self, customer: Customer):
        return self._execute_upsert("update customers set name = :name, email = :email, phone = :phone where tc = :tc",
                                    **customer.dict())

    def delete_customer(self, tc):
        return self._execute_upsert("delete from customers where tc = :tc", tc=tc)

    def insert_product(self, product: Product):
        cur = self._conn.cursor()
        cur.callproc("insert_product", (product.barcode, product.name, product.price, product.stock))
        cur.close()
        return True

    def update_product(self, product: Product):
        return self._execute_upsert(
            "update products set price = :price, name = :name, stock = :stock where barcode = :barcode",
            **product.dict())

    def delete_product(self, barcode):
        return self._execute_upsert("delete from products where barcode = :barcode", barcode=barcode)

    def insert_employee(self, employee: Employee):
        return self._execute_upsert("""insert into staff(tc, name, password, email, phone, title) 
        values(:tc, :name, :password, :email, :phone, :title)""", **employee.dict())

    def update_employee(self, employee: Employee):
        return self._execute_upsert(
            "update staff set name = :name, email = :email, phone = :phone, title = :title where tc = :tc",
            **employee.dict())

    def delete_employee(self, tc):
        return self._execute_upsert("delete from staff where tc = :tc", tc=tc)

    def insert_sale(self, sale: Sale):
        return self._execute_upsert(
            """insert into sales(customer_tc, product_barcode, sale_date, product_total, staff_tc) 
            values (:customer_tc, :product_barcode, :sale_date, :product_total, :staff_tc)""", **sale.dict())

    def get_all_sales(self):
        return self._execute_stmt("""
        select sale_date, product_total, c.name as customer_name, s.name as employee_name, p.name as product_name, price
        from sales
        left join customers c on c.tc = sales.customer_tc
        left join products p on p.barcode = sales.product_barcode
        left join staff s on s.tc = sales.staff_tc""")

    def _connect_db(self):
        self._conn = cx_Oracle.connect("nini", "cokgizlisifre", "nisancoskun.com/xepdb1", encoding="UTF-8")
        print("INFO: \t  (Re)connected to Oracle DB ( version:", self._conn.version, ")")

    def _execute_upsert(self, statement, **kwargs):
        start_time = datetime.now()
        while True:
            try:
                cur = self._conn.cursor()
                cur.execute(statement, kwargs)
                self._conn.commit()  # this is important!!
                cur.close()
                print(f"\"{statement}\" executed in {(datetime.now() - start_time).microseconds / 1000} ms")
                return True
            except cx_Oracle.OperationalError:
                # Reconnect when connection is lost
                self._connect_db()
            except Exception as e:
                return str(e)

    def _execute_stmt(self, statement, **kwargs):
        start_time = datetime.now()
        while True:
            try:
                cur = self._conn.cursor()
                cur.execute(statement, kwargs)

                # Turn tuple row data to dicts
                columns = [i[0].lower() for i in cur.description]
                data = [dict(zip(columns, row)) for row in cur]

                cur.close()
                print(f"\"{statement}\" executed in {(datetime.now() - start_time).microseconds / 1000} ms")
                return data
            except cx_Oracle.OperationalError:
                # Reconnect when connection is lost
                self._connect_db()


database = DBConnection()
