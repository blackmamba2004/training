class ThreadData:
    __shared_attrs = {
        'name': 'thread1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


thread1 = ThreadData()
thread2 = ThreadData()
thread1.id = 3
thread2.attr_new = 'new-attr'
print(thread1.__dict__)

print(thread2.__dict__)
