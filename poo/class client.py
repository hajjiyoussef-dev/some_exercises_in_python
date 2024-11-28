class client:
    def __init__(self ,c,n,p,v):
        self.code=c
        self.nom=n
        self.prenom=p
        self.ville=v
    def affiche(self):
        print(self.code,self.nom,self.prenom,self.ville)
    def get_code(self):
        return self.code
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_ville(self):
        return self.ville
    def set_code(self,c):
        self.code=c
    def set_ville(self,v):
        self.ville=v
c= client (0," ","","")
c1 =client (10,"ahmad","alami","khouribga")
c1.set_code(60)
c1.set_ville("casablanc")
print(c1.affiche(),sep="\t")
print("le code est;",c1.get_code(),"\n","le nom est;",c1.get_nom(),"\n","le prenom est;",c1.get_prenom(),"\n","le code est;",c1.get_ville())
print("--------------------------------------------------------------------------------------------")
c.set_code(69)
c.set_ville("khouribga")
print("le code est;",c.get_code(),"\n","le nom est;",c.get_nom(),"\n","le prenom est;",c.get_prenom(),"\n","le code est;",c.get_ville())



