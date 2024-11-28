p=int(input("donner p="))
if p<=20:
    p1=p+p*0.10
elif 20<p<=40:
    p1=p+(p*0.20)
elif 40<p<=60:
    p1=p+(p*0.30)
else:
    p1=p+(p*0.40)
print("le prix de prodoit est:",p1)