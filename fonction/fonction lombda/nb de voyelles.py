ch= str(input("donner une chaine= ")).lower()
cp=0
for i in ch :
    if i=="a"or i=="e"or i=="i" or i=="o" or i=="u" or i=="y":
        cp+=1
print("la nb de voyelle est:",cp)
# methode2
v=["a","e","i","o","u","y"]
ch=str(input("donner une chaine ch= ")).lower()
cp=0
for j in v:
    cp=cp+ch.count(j)
print("le nb de voyelle est:",cp)