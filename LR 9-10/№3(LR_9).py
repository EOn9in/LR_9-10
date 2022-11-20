def last_minus(mass):
  index = len(mass)
  while(index>0):
    index-=1
    if mass[index]<0 :
      break
  if index==0:
    print('0')
  else:
    print('Номер последнего отрицательного числа: ',index)
print('Введите длину массива: ',end='')
n = int(input())
m = []
for i in range(n):
  m.append(int(input()))
last_minus(m)