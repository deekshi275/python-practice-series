import threading
from threading import Thread, current_thread
import time
class house:
    def __init__(self):
        self.white = threading.Lock()
        t1 = Thread(target=self.run,name='boy')
        t2 = Thread(target=self.run,name='girl')
        t3 = Thread(target=self.run,name='other')

        t1.start()
        time.sleep(1)
        t2.start()
        time.sleep(1)
        t3.start()

    def run(self):
        with self.white:

            print(current_thread().name,"has entered the bath room")
            time.sleep(4)
            print(current_thread().name,"boy take the bath")
            time.sleep(2)
            print('both room is free',current_thread().name,'exits from bothroom')

h = house()