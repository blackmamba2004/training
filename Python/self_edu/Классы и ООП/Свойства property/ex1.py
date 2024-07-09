# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     old = property(get_old, set_old)
#
#
# p = Person('Symon', 20)
# p.__dict__['old'] = 'old object'
# p.old = 35
# print(p.old, p.__dict__)

nums = [1,2,3,4,5,6,7,8,9]
print(nums[0:1])