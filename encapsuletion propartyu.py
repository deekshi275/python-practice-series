# class emp:
#     def __init__(self):
#         self.__sal = None
#
#     @property
#     def sal(self):
#         return  (self.__sal)
#     @sal.setter
#     def sal(self,s):
#         if s>0:
#             self.__sal = s
#         else:print('invalid')
#
# e = emp()
# e.sal = 10000
# print('salary is ',e.sal)
#
class human:
    def __init__(self):
        self.__age = None

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,n):
        if n<=0 or n>=120:
            print('invalid age')
            self.__age = n
        elif n>18:
            print("adult")
            self.__age = n
        else:
            print('child')


h =human()
h.age = 40
print(h.age)
