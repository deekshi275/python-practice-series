class airtel:
    def recharge(self,cardnum = None, exp = None,cvv=None,username=None,password=None,upiId=None,pin=None):
        if cardnum and exp and cvv:
            print('recharge by card')
            print(cardnum)
        elif username and password:
            print('recharge by netbank')
            print(username)
        elif upiId and pin:
            print('recharge by upi')
            print(upiId )
        else:
            print('einvald input')
c = airtel()
c.recharge(cardnum=12345,exp=2003,cvv=456)
c.recharge(username='deekshi',password='143')
c.recharge(upiId='2345678.ylx',pin=345678)
c.recharge()