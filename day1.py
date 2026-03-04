
#-------------------------------convert small letters to capital letters using ascii values--------------
s = input("enter a value:  ")
i =0
news = ""
while i <= len(s)-1:
    data = s[i]
    asci = ord(data)
    if asci>=97 and asci<=122:
        newasci = asci - 32
        con = chr(newasci)
        news = news + con

    elif asci>=65 and asci<=90:
        nn = asci + 32
        vv = chr(nn)
        news = news + vv
    else:
        news = news + data
    i = i + 1

print(news)