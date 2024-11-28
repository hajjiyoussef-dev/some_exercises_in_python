n=int(input("donner n="))
k=0.0
if n==0:
    print("impossible")
else:
    for i in range(1,n+1):
        k=k+ round(1/i,2)
    print("la valeur de k est;",k)