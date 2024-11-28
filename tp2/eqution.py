a=int(input("donner a="))
b=int(input("donner b="))
if a==0 and b==0:
    print("lensemble R")
elif a==0 and b!=0:
    print("pas de solution")
else:
    s=round(-b/a,2)
    print("la solution est ",s)