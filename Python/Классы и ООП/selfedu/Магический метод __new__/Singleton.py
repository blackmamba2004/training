class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, passwd, port):
        self.user = user
        self.passwd = passwd
        self.port = port

    def __del__(self):
        Database.__instance = None

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.passwd}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"Запись в БД {data}")


db = Database('admin', '123', '5432')
db2 = Database('admin2', '567', '8080')
print(id(db), id(db2))
db.connect()
db2.connect()
