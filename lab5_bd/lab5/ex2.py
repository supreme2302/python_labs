import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    #! Открытие соединения
    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )
            self._connection.set_character_set('utf8')

    #! Закрытие соединения
    def disconnect(self):
        if self._connection:
            self._connection.close()


class Zakaz:

    def __init__(self, db_connection, prodact_name, description):
        self.db_connection = db_connection.connection
        self.zakaz = prodact_name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("insert into labApp_zakaz (name, usluga) values(%s, %s);",
                  (self.zakaz, self.description))

        self.db_connection.commit()
        #c.execute("SELECT * FROM zakaz;")

        c.close()


conn = Connection("root", "1", "lab6")

with conn:
    prodact = Zakaz(conn, 'Домашние услуги', "Сделать уборку")
    prodact.save()

