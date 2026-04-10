# print('enter a program')
#
# a = int(input('entera number'))
# b = int(input('entera number'))
#
# try:
#     if a>b:
#         print('diff is',a-b)
#     else:
#         raise Exception()
# except Exception:
#     print('the a>b the value is greate')


class InvalidinpException(Exception):
    pass

class InvalidBalenceException(Exception):
    pass

class Bank:
    def __init__(self,bal):
        self.bal = bal
        self.amt = int(input('enter a amount'))

    def with_drow(self):
        try:
            if self.amt<0:
                raise InvalidinpException()
            elif self.amt>self.bal:
                raise InvalidBalenceException()
            else:print('amount with drow sucessfully reming amount',self.bal-self.amt)
        except InvalidinpException:
            print('amount must greate than 0')
        except InvalidBalenceException:
            print('amount must be less than balence')
b = Bank(500)
b.with_drow()


