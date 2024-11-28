l=[7,0,2,9,5,1]
for i in range(0,len(l)):
    for j in range((i+1),len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l[:])