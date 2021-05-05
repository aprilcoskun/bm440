from dataclasses import dataclass
from datetime import datetime
import cx_Oracle


@dataclass
class Employee:
    tc: str
    name: str
    password: str
    title: str
    email: str = None
    phone: str = None


@dataclass
class Product:
    barcode: str
    name: str
    price: int
    stock: int


@dataclass
class Customer:
    tc: str
    name: str
    email: str = None
    phone: str = None


@dataclass
class Sale:
    customer_name: str
    employee_name: str
    sale_date: datetime
    product_name: str
    product_price: int
    product_total: int


def rows_to_dict_list(cursor):
    columns = [i[0].lower() for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]


def rows_to_dict(cursor):
    columns = [i[0].lower() for i in cursor.description]
    row_list = [dict(zip(columns, row)) for row in cursor]
    return row_list[0]


class DBConnection:
    _conn: cx_Oracle.Connection

    def __init__(self):
        self._connect_db()
        print("INFO: \t  Connected to Oracle DB ( version:", self._conn.version, ")")

    def _connect_db(self):
        self._conn = cx_Oracle.connect("nini", "cokgizlisifre", "nisancoskun.com/xepdb1", encoding="UTF-8")

    def get_employee(self, tc):
        cur = self._conn.cursor()
        cur.execute("select * from staff where tc = :tc", tc=tc)
        data = rows_to_dict(cur)
        cur.close()
        return Employee(**data)

    def get_all_staff(self):
        try:
            cur = self._conn.cursor()
            cur.execute("select * from staff")
            data = rows_to_dict_list(cur)
            cur.close()
            return data
        except cx_Oracle.OperationalError:
            self._connect_db()
            cur = self._conn.cursor()
            cur.execute("select * from staff")
            data = rows_to_dict_list(cur)
            cur.close()
            return data

    def get_all_products(self):
        cur = self._conn.cursor()
        cur.execute("select * from products")
        data = rows_to_dict_list(cur)
        cur.close()
        return data

    def get_all_customers(self):
        cur = self._conn.cursor()
        cur.execute("select * from customers")
        data = rows_to_dict_list(cur)
        cur.close()
        return data

    def get_all_sales(self):
        cur = self._conn.cursor()
        cur.execute("select * from sales")
        data = rows_to_dict_list(cur)
        cur.close()
        return data


db_conn = DBConnection()
