a=int(input("donner a="))
if (a%4==0 and a%100!=0 or a%400==0):
    print( a,"est  bessectille")
else:
    print(a,"est  simple ")