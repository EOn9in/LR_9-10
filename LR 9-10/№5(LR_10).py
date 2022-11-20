from random import randint
n, m = 8, 8
a = [[randint(1, 10) for j in range(m)] for i in range(n)]
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()
mass=[]
i=0
while n>i:
  k = 0
  max = 0
  for j in range(m):
    if a[i][j]>max:
      max = a[i][j]
      k = 0
    elif a[i][j]==max:
      k+=1
  if k == 0:
    mass.append('1')
  else:
    mass.append('-1')
  i+=1
print(mass)