from threading import Thread, Lock, current_thread
import time

class DBprocess:
    def __init__(self):
        self.l1 = Lock()
        self.l2 = Lock()
        self.l3 = Lock()

    def run(self):
        if current_thread().name == "rama":
            self.rama_db()
        else:self.sita_db()

    def rama_db(self):
        with self.l1:
            print('rama enterd oracle')
            time.sleep(1)

            with self.l2:
                print('rama enterd the sybase')
                time.sleep(1)

                with self.l3:
                    print('rama enterd the informics')

    def sita_db(self):
        with self.l3:
            print('sita enterd the informics')
            time.sleep(1)

            with self.l2:
                print("sita enterd the sybase")
                time.sleep(1)

                with self.l1:
                    print('sita entered the oracle')

db = DBprocess()
t1 = Thread(target=db.run,name='rama')
t2 = Thread(target=db.run,name='sita')





