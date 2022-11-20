from random import randint
n, m = 8, 8
a = [[randint(1, 10) for j in range(m)] for i in range(n)]
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()
mass=[]
i = 0
while n>i:
  min = a[i][j]
  for j in range(m):
    if a[i][j]<min:
      min = a[i][j]
  mass.append(min)
  i+=1
print(mass)
print('Среднее арифметическое: ',sum(mass)//8)