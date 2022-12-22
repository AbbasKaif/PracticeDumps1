'''print range(10)
print range(1,10)
print range(0,30,5)
print range(0,10,3)
print range(0,-10,-1)
print range(0)
print range(1,0)
print range(10,0,-1)
print range(-1,-10,-1)
print range(-10,-1)
x=2
print range(0,25,x**2)'''

'''for x in range(10):
 print x'''

'''for x in range(0,10,2):
 print x'''

'''for x in range(10):
 if x%2==0:
  print x,'is even'
 else:
  print x,'is odd'
'''

'''z='A'
p=9
for x in range(1,11):
  print z*x
  print p*' '
  for y in range(1,x):
   print z
  p=p-1'''

z='a'
p=10
for y in range(1,10):
 for m in range(1,y):
  print z,
 print p*' ',
 p=p-1
 for n in range(1,y):
  print z,
 print '\n'