n=int(input("donner n"))
print("la serie de syracus de",n,"est;")
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=(3*n)+1
    print(n,end="")