# class mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#
# class smartphone(mobile):
#     def __init__(self,b,p,color):
#         self.color = color
#         super().__init__(b,p)
#
#     def display(self):
#         print(self.brand,self.price,self.color)
#
# c = smartphone('apple',10000,'black')
# c.display()
# c1=smartphone('infinix',10000,'black')
# c1.display()


# class card:
#     def __init__(self,cardno,expdate,cvv,balence):
#         self.cardno = cardno
#         self.expdate = expdate
#         self.cvv = cvv
#         self.balence = balence
#         print(f'card no is {self.cardno},card experidate{self.expdate},card cvv{self.cvv}')
#
#     def withDrow(self,amount):
#
#         if self.balence>amount:
#             self.balence -=amount
#             print('amount withdrow sucessfully',amount)
#
#     def swip(self):
#         print('payment sucesfully')
#
#     def check_balenc(self):
#         print('your courent self.balence is ',self.balence)
#
#
# class credit(card):
#     def __init__(self,cardno,exodate,cvv,balence):
#         super().__init__(cardno,exodate,cvv,balence)
#     def credit_amount(self):
#         print('amount credited sucesfully')
#     def paybilss(self,bill):
#         if bill<self.balence:
#             self.balence-=bill
#             print('your bill is ',bill,'payment sucesfull')
#         else:
#             print('invalid self.balence')
#
# class debitcard(card):
#     def __init__(self,c,e,v,b):
#         super().__init__(c,e,v,b)
#
#     def deposit(self,rs):
#         if rs>0:
#             global balence
#             balence+=rs
#         else:print('invalid amount')
#
# class forexcard(card):
#     def __init__(self,root,target,c,e,v,b):
#         self.root ='inr'
#         self.target = 'us$'
#         super().__init__(c,e,v,b)
#         print('root is ',self.root,'target is ',self.target)
#     def loadamount(self,amount):
#         self.amount = amount
#         amoun =0
#         amoun+=amount
#         print('your loded amount is ',amount)
#
#     def convertamount(self):
#         print('$',self.amount*99)
#
#
#
#
# c = credit(401,'2/20',28736,5000)
# c.withDrow(1000)
# c.check_balenc()
# c.swip()
# c.credit_amount()
# c.paybilss(100)
# c.check_balenc()
# print('------------------------------')
# d=debitcard(111,'2/29',16367,100)
# d.swip()
# d.withDrow(20)
# d.check_balenc()



#-----------------------------------class car --------------------------

class vehicle:
    def __init__(self,veh_no,brand,fuel_type):
        self.veh_no = veh_no
        self.brand = brand
        self.fuel_type = fuel_type

    def start(self):
        print('vehical start')
    def stop(self):
        print('vehical stop')
    def display(self):
        print(f'vehical no is {self.veh_no}\n vehical brand is {self.brand}\n vehical fuel type is {self.fuel_type}')

class bike(vehicle):
    def kickstart(self):
        print('bike will start')
class car(vehicle):
    def opentrunk(self):
        print('open the trunk')
class electric(vehicle):
    def charge(self):
        print('start charging')
    def check_battery(self):
        print('battery is full')

b = bike(143,"royal enfield",'petrol')
b.display()
b.start()
b.stop()
b.kickstart()
print('---------------------------------------------------')
c = car(34567,'mustang','petrol')
c.display()
c.opentrunk()
c.start()
c.stop()
print('------------------------------------------------------')
e = electric(12345,'rio','electric')
e.display()
e.start()
e.stop()
e.charge()
e.check_battery()

