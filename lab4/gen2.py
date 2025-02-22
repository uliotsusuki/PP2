n=int(input())
a=0
for i in range(n):
    a+=1
    if(a%2!=0):
        continue
    print(a,end=", ")
