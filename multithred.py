import time

class Demo:
    def bank(self):
        self.name = input('enter a name')
        self.age = input('enter a age')
        print(self.name,self.age)
    def printing(self):
        for i in range(5):
            print('deekshith')
            time.sleep(3)
    def add(self):
        a = 10
        b = 20
        print(a+b)

d = Demo()
d.bank()
d.printing()
d.add()