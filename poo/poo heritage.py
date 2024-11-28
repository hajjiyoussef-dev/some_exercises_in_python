class animal:
    def __init__(self ,c,n,a):
        self.code=c
        self.nom=n
        self.age=a
    def affich(self):
        print(self.code,self.nom,self.age,sep="\t")
class chine(animal):
    def __init__(self ,c,n,a,o,r):
       super(chine, self).__init__(c,n,a)
       self.couleur =o
       self.race = r
    def affich(self):
        animal.affich(self)
        print(self.couleur,self.race ,sep="\t")
dog = animal (1,"fido",5)
dog1 = chine ("Fido", 1, 3, "black", "Labrador")
print(dog.affich(),dog1.affich())
