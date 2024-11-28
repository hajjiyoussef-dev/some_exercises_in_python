naissauce=lambda j,m,a:j+"/"+m+"/"+a
j=int(input("donnerb la jour j="))
if j<1 or j>31:
    print("jour invalide")
else:
    j=str(j)
    m=int(input("donnerbl mois m="))
    if m<1 or m>12:
        print("mois invalide")
    else:
        m=str(m)
        a=int(input("donner annes a="))
        if a<1900 or a>2022:
            print("annes invalide")
        else:
            a=str(a)
            print("date naissauce est;",naissauce(j,m,a))
