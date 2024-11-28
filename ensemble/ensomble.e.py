e = {12, 10, "Ali", "sara"}
e.add("Ayoub")
for i in e:
    print(i)
e.update([13, 11, "Ahmed"])
print("affichege apre update")
for element in e:
    print(element)
e.remove("sara")
print("affichege apre remove")
for element in e:
    print(element)
e.pop()
print("affichege apre pop")
for element in e:
    print(element)
long = len(e)
print("lengeur de e est :", long)
e1 = {12, 10}
e2 = {"amin", "sara", "ahmed"}
u = e1.union(e2)
print("l enselbe de e1 et e2")
print(u)
e.clear()
print(e)