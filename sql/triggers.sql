create trigger delete_staff after delete on staff for each row
    begin
        insert into deleted_staff(tc, name, password, email, phone, title)
        values (:old.tc, :old.name, :old.password, :old.email, :old.phone, :old.title);
    end;
/
create trigger delete_product after delete on products for each row
    begin
        insert into deleted_products(barcode, price, name, stock)
        values (:old.barcode, :old.price, :old.name, :old.stock);
    end;
/
create trigger delete_customer after delete on customers for each row
    begin
        insert into deleted_customers(tc, name, email, phone)
        values (:old.tc, :old.name, :old.email, :old.phone);
    end;
/
create trigger delete_sale after delete on sales for each row
    begin
        insert into deleted_sales(customer_tc, product_barcode, sale_date, product_total, staff_tc)
        values (:old.customer_tc, :old.product_barcode, :old.sale_date, :old.product_total, :old.staff_tc);
    end;
/


INSERT INTO NINI.CUSTOMERS (TC, NAME, EMAIL, PHONE) VALUES ('12345678912', '123123', '123123', '123123')