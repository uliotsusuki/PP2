n=int(input())
a=0
for i in range(n):
    a+=1
    if(a%3==0 and a%4==0):
        print(a, end=", ")
    else:
        continue
