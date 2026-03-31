# # class father:
# #     def workP(self):
# #         print('eorking')
# #
# #     def drive(self):
# #         print('drivuing')
# #
# # class mother:
# #     def cook(self):
# #         print('cooking')
# #     def drivbe(self):
# #         print('driving m')
# #
#
#
#
# class os:
#     def __init__(self):
#         print('os is created ')
#     def check(self):
#         print('os working proparly')
#
# class charger:
#     def __init__(self):
#         print('charger is cerated')
#
#     def getchjarger(self):
#         print('charger is accures')
#
# class mobile:
#     def __init__(self):
#         self.o = os()
#         print('mobile is cerated')
#
#     def hasa(self,ch):
#         print('cahjrger is acupy')
#
# m = mobile()
# m.o.check()
# c = charger()
# c.getchjarger()
# m.hasa(c)
# m = None
# c.getchjarger()


class heart:
    def __init__(self):
        print('hello this is myheart')
    def check(self):
        print('person has a heart')

class mobile:
    def mobile_charge(self):
        print('100% charge')

class person:
    def __init__(self):
        print('person is here')
        self.he = heart()

    def check_mobile(self,a):
        print('person having mobile')

p = person()
m = mobile()
m.mobile_charge()
p.check_mobile(m)
p.he.check()



