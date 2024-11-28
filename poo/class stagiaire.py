class stagiaire:
    def __init__(self):
        self.code =0
        self.nom = ""
        self.prenom =""
        self.age = 0
class stagiaire:
    def __init__ (self,c,n,p,a):
        self.code=c
        self.nom=n
        self.prenom=p
        self.age=a
    def affiche(self):
        print(self.code,self.nom,self.prenom,self.age,sep="\t",end="\t")
    def decision(self):
        if  self.age >= 18:
            return("majour")
        else:
            return ("mineur")
s1=stagiaire(10,"alami","ali",20)
print(s1.affiche())
print(s1.decision())
print(s1.__dict__ )
print(s1.__module__)
print(s1.__class__)

