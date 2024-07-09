class Database:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, passwd, port):
        if not self.__initialized:
            self.user = user
            self.passwd = passwd
            self.port = port
            self.__initialized = True

    def __del__(self):
        print('Удаляем экзмепляр', self.__instance)
        self.__instance = None
        self.__initialized = False

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
print(db)
print(id(db), id(db2))
db.connect()
db2.connect()
del db2
print(db)
del db