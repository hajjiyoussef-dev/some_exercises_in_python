def t(n):
 for i in range(n):
    t=int(input("donner element de tableou:",i+1,":"))
    for i in range(n):
        print(t(i)+"\t")
