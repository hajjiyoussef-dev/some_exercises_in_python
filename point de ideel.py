t= int(input("donner la taille t="))
if t < 140:
    print("taille invalide ")
else:
    genre = (str("donner le genre"))
    if genre == "h":
        pi = (t - 100) * 0.90
    else:
        pi = (t - 100) * 0.85
    print("le poid ideal est", pi, "kg")
