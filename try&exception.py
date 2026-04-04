class demo:
    def fun1(self):
        print('in fun1')
        try:
            self.fun2()
        except Exception:
            print('problem in fun2')

    def fun2(self):
        print('in fun2')
        a = 10
        b = 0
        try:
            print(a/b)
        except Exception:
            print('problem occured')

d = demo()

try:
    d.fun1()
except Exception:
    print('problem in main')