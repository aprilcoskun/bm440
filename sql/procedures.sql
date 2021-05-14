create or replace procedure insert_product(
    barcode_param in products.barcode%type,
    name_param in products.name%type,
    price_param in products.price%type,
    stock_param in products.stock%type) is
begin
    insert into products(barcode, name, price, stock)
    values (barcode_param, name_param, price_param, stock_param);
    commit;
end;
/

create or replace procedure insert_customer(
    tc_param in customers.tc%type,
    name_param in customers.name%type,
    email_param in customers.email%type,
    phone_param in customers.phone%type) is
begin
    insert into customers(tc, name, email, phone)
    values (tc_param, name_param, email_param, phone_param);
    commit;
end;
/