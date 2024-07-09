class Singleton:
    def __init__(self, cls):
        self.__cls = cls
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = self.__cls(*args, **kwargs)

        return self.__instance


@Singleton
class Database:
    def __init__(self, user, password, port):
        self.__user = user
        self.__password = password
        self.__port = port

    def __del__(self):
        self.__instance = None


SingletonDatabase = Singleton(Database)
db = SingletonDatabase('admin', '1234', '5432')
print(db)
db1 = Database('symon', '123', '5432')
db2 = Database('matwey', '565', '5050')
print(db2.__dict__)