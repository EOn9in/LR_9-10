from random import randint
n, m = 6, 8
a = [[randint(1, 10) for j in range(m)] for i in range(n)]
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()
mass=[]  
while n>0:
  j = 0
  for i in range(n):
    if abs(a[i][j]) > 4:
      mass.append(a[i][j])
      n-=1
    else:
      mass.append('0')
      n-=1
print(mass)