f=open("DELETE.INP")
f1=open("DELETE.OUT","w")
n=int(f.readline())
a=[0]+list(map(int,f.readline().split()))
num1=[0]*(n+1)
num3=[0]*(n+2)
for i in range(1,n+1):
    if a[i]==1:
        num1[i]=num1[i-1]+1
    else:num1[i]=num1[i-1]
for i in range(n,0,-1):
    if a[i]==3:
        num3[i]=num3[i+1]+1
    else:
        num3[i]=num3[i+1]
result=0
id2=0
for i in range(1,n+1):
    if a[i]==2:

        result+=(num1[id2]+num1[i])*num3[i]
        num1[i]+=num1[id2]
        num1[i]+=num1[id2]
        id2=i
        
print(result)
f.close()
f1.close()