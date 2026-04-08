class underageException(Exception):
    pass

class overageException(Exception):
    pass

age = int(input('enter a age'))

try:
    if age<18:
        raise underageException('age must greater than 18')
    elif age>60:
        raise  overageException('age must less than 60')
    else:
        print('licence can given')

except underageException as e:
    print(e)
except overageException as e1:
    print(e1)
