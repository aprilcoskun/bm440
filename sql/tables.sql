create table staff(
    tc char(11) primary key not null,
    name varchar2(50) not null,
    password varchar2(150) not null,
    email varchar2(50),
    phone varchar2(50),
    title varchar2(50) not null
);

create table customers(
    tc char(11) primary key not null,
    name varchar2(50) not null,
    email varchar2(50),
    phone varchar2(50)
);

create table products(
    barcode number(10) primary key not null,
    price number(10) not null,
    name varchar2(50) not null,
    stock number(10) default on null 1
);

create table sales(
    customer_tc char(11) not null,
    product_barcode number(10) not null,
    sale_date date default on null sysdate,
    product_total number(10) default on null 1,
    staff_tc char(11) not null,
    constraint fk_product_barcode foreign key (product_barcode) references products (barcode),
    constraint fk_customer_tc foreign key (customer_tc) references customers (tc),
    constraint fk_staff_tc foreign key (staff_tc) references staff (tc)
);

create table deleted_staff(
    tc char(11) primary key not null,
    name varchar2(50) not null,
    password varchar2(150) not null,
    email varchar2(50),
    phone varchar2(50),
    title varchar2(50) not null
);

create table deleted_customers(
    tc char(11) primary key not null,
    name varchar2(50) not null,
    email varchar2(50),
    phone varchar2(50)
);

create table deleted_products(
    barcode number(10) primary key not null,
    price number(10) not null,
    name varchar2(50) not null,
    stock number(10) default on null 1
);

create table deleted_sales(
    customer_tc char(11) not null,
    product_barcode number(10) not null,
    sale_date date default on null sysdate,
    product_total number(10) default on null 1,
    staff_tc char(11) not null
);