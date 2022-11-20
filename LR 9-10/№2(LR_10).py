from random import randint
n, m = 8, 6
a = [[randint(-2, 10) for j in range(m)] for i in range(n)]
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()
mass=[]
i = 0
while n>i:
  k = 0
  for j in range(m):
    if a[i][j]<0:
      k+=1
  if k !=0:
    mass.append('-1')
  else:
    mass.append('1')
  i+=1
print(mass)