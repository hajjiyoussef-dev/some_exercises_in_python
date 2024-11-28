naissance =lambda m,j,a:j+"/"+m+"/"+a
x=int(input("donner le jouer x="))
if x>31:
    print("jouer incorrect")
else:
    x=str(x)
    y=int(input("donner le mois y="))
    if 12 < y < 1:
        print("mois est incorrect")
    else:
        y=str(y)
        z=int(input("donner la anner z="))
        