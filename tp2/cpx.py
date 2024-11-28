a=int(input("donner a="))
b=int(input("donner b="))
c=int(input("donner c="))
if a==b and b==c:
    print("egalite")
elif a>b and a>c :
    sup=a
    print("le pluis grand est:",sup)
elif b>c:
    sup=b
    print("le pluis grand est:",sup)
else:
    sup=c
    print("le pluis grand est:", sup)