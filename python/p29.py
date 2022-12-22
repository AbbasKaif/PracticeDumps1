#Sum of digits
num=int(input("Enter a number: "))
sum=0
while(num>0):
    p,q=divmod(num,10)
    sum=sum+q
    num=p
print("sumof digits= ",sum)