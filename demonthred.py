import time
from threading import Thread


class Typecheck(Thread):
    def run(self):
        if self.name =='typing':
            self.typing()
        elif self.name == 'spell':
            self.spell_check()
        else:
            self.autosave()

    def typing(self):
        print('typing started')
        time.sleep(5)
        print('typing is completed')

    def spell_check(self):
        while True:
            print('spelling checking in process')
            time.sleep(3)

    def autosave(self):
        while True:
            print('auto saving is progress')
            time.sleep(3)

t1 = Typecheck()
t2 = Typecheck()
t3 = Typecheck()

t1.name ='typing'
t2.name = 'spell'
t3.name = 'auto'
t2.daemon = True
t3.daemon = True

t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()