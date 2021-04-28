import cx_Oracle


class Employee:
    username: str

    def __init__(self, username):
        self.username = username


class Product:
    def __init__(self):
        pass


class Customer:
    def __init__(self):
        pass


class Sale:
    def __init__(self):
        pass


class DBConnection:
    _conn: cx_Oracle.Connection

    def __init__(self):
        self._conn = cx_Oracle.connect("nini", "cokgizlisifre", "nisancoskun.com/xepdb1", encoding="UTF-8")
        print("INFO: \t  Connected to Oracle DB ( version:", self._conn.version, ")")

    def get_version(self):
        return self._conn.version

    def get_user(self, username):
        # cur = self._conn.cursor()
        # cur.execute("select * from staff where username = :username", username=username)
        # val, = cur.fetchone()
        # print(val)

        return Employee(username=username)


db_conn = DBConnection()
