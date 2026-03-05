#--------------@classmethod-----------------------
#-------------@staticmethod-----------------------

# class vehical:
#     wheel = 4
#     @classmethod
#     def run(cls,name,n):
#         cls.n = n
#         print(f'the {name} runs with {cls.n} wheels')
#
# vehical().run('car',4)
# a = vehical()
# a.run('truck',4)
# a.run('bike',2)

class student:
    collage = 'gecm hassan'

    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
        print(f'student name is {self.name} and age is {self.age} and collage is {self.collage}')

    @classmethod
    def subject(cls,name,marks):
        print(name,marks,cls.collage)

    @staticmethod
    def result(n):
        if n>=35:
            print('pass')
        else:
            print('fail')


s = student('deekshi',20,401,)
s.subject('math',40)
s.result(45)





