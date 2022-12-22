num=int(input("Enter a number "))
n,c,i=num,0,1
while(i<=n):
    if(n%i==0):
        c=c+1
    i+=1
if(c==2):
    print("Prime")
else:
    print("Not Prime")