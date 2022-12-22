'''li=[]
for i in range(int(input())):
	li.append(int(input()))
for j in range(n,0,-1):
	print(li)

a=[int(i) for i in input().split(" ")]
b=[]
for i in range(len(a)):
	b.append(a[len(a)-1-i])
print("Original List:", *a)
print("Reversed List:", *b)
'''

'''li=[]
n=int(input("Enter size "))
for i in range(n):
	li.append(int(input("Enter no: ")))
for j in range(n-1,-1,-1):
	print(li[j])'''


for i in range(10,0,-1):
	print(i,end=" ")