a=int(input("donner a="))
b=int(input("donner b="))
chaix=str(input("donner chaix="))
if chaix == "somme":
    s=a+b
    print("la somme est:",s)
elif chaix =="produit":
    s=a*b
    print(" le produit est :",s)
elif chaix =="soutraction":
    s=a-b
    print("le resulhast;",s)
elif chaix =="divison":
    if b==0:
        print(" divison imposible")
    else:
        s= round(a/b,2)
        print("la divison:",s)
