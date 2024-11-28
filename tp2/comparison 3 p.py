x=int(input("donner x="))
y=int(input("donner y="))
z=int(input("donner z="))
if x==y and y==z:
    print("egalite")
elif x<y and x<z :
    inf=x
    print("le pluis petit est:",inf)
elif y<z:
    inf=y
    print("le pluis petit est:",inf)
else:
    inf=z
    print("le pluis petit est:",inf)