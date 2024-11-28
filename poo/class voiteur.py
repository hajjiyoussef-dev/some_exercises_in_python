import datetime
class voiteur:
    def __init__(self,code,marque,modele,puissance):
        self.code = 0
        self.marque = " "
        self.modele = 0
        self.puissance = 0
        self.code = code
        self.marque = marque
        self.modele = modele
        self.puissance = puissance
    def affiche(self):
        print(self.code,self.marque,self.modele,self.puissance,sep="\t",end="\t")
    def etat(self):
        if self.modele >= 2018 :
            print("nouvelle")
        else:
            print("ancienne")
    def calcul(self):
        age=datetime.datetime.now().year-self.modele
        return age
v1 = voiteur(100,"fiat",2019,7)
v2 = voiteur(200,"mercede",2016,8)
v = voiteur(0," ",0,0)
#v1
print(v1.affiche())
print(v1.etat())
print(v1.__dict__ )
print(v1.__module__)
print(v1.__class__)
#v2
print(v2.affiche())
print(v2.etat())
print(v2.__dict__ )
print(v2.__module__)
print(v2.__class__)
#v3
print(v.affiche())
print(v.etat())
print(v.__dict__ )
print(v.__module__)
print(v.__class__)
#vv
print("l age de cette voture est ",v1.calcul(),"ans")
print("____________________________________________")
# ____________________________________________________
class Voteur:
    def __init__(self, code, marque, modele, puissance):
        self.__code = code
        self.__marque = marque
        self.__modele = modele
        self.__puissance = puissance

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_puissance(self):
        return self.__puissance

    def set_puissance(self, puissance):
        self.__puissance = puissance

    def calcul(self):
        age = datetime.datetime.now().year-self.__modele
        return age

v3 = Voteur(300,"fiat",2004,9)
print("la code est :",v3.get_code())
print("la marque est :",v3.get_marque())
print("la modele est :",v3.get_modele())
print("la puissance est :",v3.get_puissance())
v3.set_code(60)
v3.set_marque("mercede")
v3.set_modele(2010)
print("le nouveau code",v3.get_code())
print("le nouveau marque",v3.get_marque())
print("le nouveau modele",v3.get_modele())
print("l age de cette voture est ",v3.calcul(),"a")
