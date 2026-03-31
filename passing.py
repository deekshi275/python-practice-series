# class employe:
#     def __init__(self,eno,ename,esal):
#         self.eno  = eno
#         self.ename = ename
#         self.esal = esal
#
#     def display(self):
#         print('name of employe is ',self.ename)
#         print('salary is ',e.esal)
#         print('emp number is ',e.eno)
#
#
# class test:
#     def modify(e):
#         e.esal = e.esal + 20000
#         e.eno = 2345767
#         e.display()
#
#
#
# e = employe(123,'deekshi',100000)
# test.modify(e)
# test.modify(e)
# test.modify(e)
from random import betavariate
from tkinter.font import names


# class person:
#     def __init__(self):
#         self.name = "deekshi"
#         self.age = self.dob()
#         print('name is ',self.name)
#
#     class dob:
#         def __init__(self):
#             self.ag = 23
#
#         def display(self):
#             print('age is ',self.ag)
# p = person()
# p.age.display()



class human:
    def __init__(self):
        self.heart = self.hear()
        self.brin = self.brin()


    class hear:
        def __init__(self):
            self.beat = "Pumps blood throughout the body"
            self.pump = 'heart beet 72 times in minut'

        def hertfun(self):
            print(self.beat)

    class brin:
        def __init__(self):
            self.bfun= 'Processes sensory info (sight, sound, touch, etc.) '


        def brinfun(self):
            print('brain ',self.bfun,)

h = human()
h.heart.hertfun()
h.brin.brinfun()

