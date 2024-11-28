print("le nomber d anstrong sont=")
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            m=i*100+j*10+k*1
            n=i*i*i+j*j*j+k*k*k
            if m==n:
                print(m)
