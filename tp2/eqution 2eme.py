import math
a=int(input("donner a="))
b=int(input("donner b="))
c=int(input("donner c="))
if a==0 and b==0 and c==0:
    print("infinite de solution")
elif a==0:
    x=-c/b
    print("la solution est;",x)
else:
    d=b*b-4*a*c
    if d<0:
      print("pas de solution")
    elif d==0:
        x1=-b/(2*a)
        print("la solution est;",x1)
    else:
        x1= (-b-math.sqrt(d)) /(2*a)
        x2= (-b+math.sqrt(d))/(2*a)
        print("les solution est x1;",x1,"est la solution x2",x2)