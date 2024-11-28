import random
tsg = []
tn = ["ahmi","badri","charafi","dahbi","el kamali","el majidi","fadili","jamali","karmi","maliki","naidi","sarraji"]
tp = ["aya","ahmed","malak","mehdi","hajar","ayoud","karim","mohamed","samira","ayman","wafaa","salah","zahira"]
tf = ["DD","ID","commerce","gestion","finace"]
email = lambda nom,prenom : nom+"."+prenom+"@gmail"
def remplire(n):
    for i in range(n):
        nom = random.choice(tn)
        prenom = random.choice(tp)
        filed = random.choice(tf)
        age = random.randint(18,25)
        numMode = random.randint(3,6)
        em = email(nom,prenom)
        tnote = []
        for _ in range(numMode):
            note = random.randint(0,20)
            tnote.append(note)
        s = {"nom":nom,"prenom":prenom,"filire":filed,"age":age,"note":tnote,"email":em}
        tsg.append(s)
def moy(t):
    s = 0
    for x in t:
        s += x
    m = round(s/len(t),2)
    return m
def affich():
    for x in tsg:
        print(x["nom"],x["prenom"],x["filire"],x["email"],x["age"],moy(x["note"]),sep="\t\t")
def trier():
    for i in range(len(tsg)-1):
        for j in range(i+1,len(tsg)):
            if moy(tsg[i]["note"]) < moy(tsg[j]["note"]):
                temp = tsg[i]
                tsg[i] = tsg[j]
                tsg[j] = temp
def serialiser():
    f = open("tsg.txt","w")
    for x in tsg:
        ch = x["nom"],x["prenom"],x["filire"],str(x["email"]),str(x["age"]),moy(x["note"])
        f.write(f"{ch}\n")
    f.close()
remplire(10)
trier()
affich()
serialiser()