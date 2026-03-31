# from typing import overload, override
#
#
# class animal:
#     def eat(self):
#         print('animal eate')
#     def walk(self):
#         print('ani,al cal walk')
#     def sleep(self):
#         print('sleeping')
#
# class tiger(animal):
#     @override
#     def sleep(self):
#         print('tiger can sleep 24 hours')
#
# class panda(animal):
#     @override
#     def eat(self):
#         print('eat by hands support')
#
# t=  tiger()
# t.eat()
# t.sleep()
# t.walk()
# print('-------------------------')
#
# p = panda()
# p.eat()


class pen:
    def __init__(self,price):
        self.price = price

    def __add__(self, other):
        return  self.price + other.price

    def __ge__(self, other):
        return self.price >= other.price
p1 = pen(10)
p2 = pen(20)
print(p1 + p2)
print(p1 <= p2)