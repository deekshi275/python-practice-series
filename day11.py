# import time
# from threading import Thread
#
#
# class task1(Thread):
#     def run(self):
#         print('entering the bankin meted')
#         time.sleep(3)
#         print('amount is looding')
#         time.sleep(3)
#         print('collect your cash')
#
# class task2(Thread):
#     def run(self):
#         for i in range(3):
#             print('deekshi')
#             time.sleep(4)
# class task3(Thread):
#     def run(self):
#         a = 100
#         b = 1000
#         print(b+a)
#
# t1 = task1()
# t2 = task2()
# t3 = task3()
#
# t1.start()
# t2.start()
# t3.start()
#
import time
from threading import Thread

class movie(Thread):
    def run(self):
        if self.name == 'prodcer':
            self.producer()
        elif self.name =='directro':
            self.director()
        elif self.name == 'actor':
            self.actor()
        else:
            self.support()




    def producer(self):
        print('producer start investing')
        time.sleep(5)
        print('producer stop invest')

    def director(self):
        while True:
            print('director directing movie')
            time.sleep(5)

    def actor(self):
        while True:
            print('actor acting movie')
            time.sleep(5)

    def support(self):
        while True:
            print('support artist acting in movie')
            time.sleep(5)


m = movie()
m1 = movie()
m2 = movie()
m3 = movie()

m.name = 'prodcer'
m1.name = 'directro'
m2.name = 'actor'
m3.name = 'support'

m1.daemon = True
m2.daemon = True
m3.daemon = True

m.start()
time.sleep(1)
m1.start()
time.sleep(1)
m2.start()
time.sleep(1)
m3.start()
