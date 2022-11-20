def dwa_massiva(mass1,mass2):
  for i in range(len(mass1)):
    sum1 = 0
    if mass1[i]>0:
      sum1+=mass1[i]
  for i in range(len(mass2)):
    sum2 = 0
    if mass2[i]>0:
      sum2+=mass2[i]
  if sum1 < sum2:
    for i in range(len(mass1)):
      mass1[i] = mass1[i]*10
    print('Массив 1 * 10: ',mass1)
  else:
    for i in range(len(mass2)):
      mass2[i] = mass2[i]*10
    print('Массив 2 * 10: ',mass2)
  return mass1
  return mass2

print('Введите длину массива 1: ',end='')
n = int(input())
m_1 = []
for i in range(n):
  m_1.append(int(input()))
print(m_1)
print('Введите длину массива 2: ',end='')
m = int(input())
m_2 = []
for i in range(m):
  m_2.append(int(input()))
print(m_2)
dwa_massiva(m_1,m_2)