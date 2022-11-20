import numpy as np
def dwa_massiva(mass1,mass2):

  for i in range(len(mass1)):
    pol1 = 0
    if mass1[i] % 5 == 0:
      pol1 = i
      break
  for i in range(len(mass2)):
    pol2 = 0
    if mass2[i] % 5 == 0:
      pol2 = i
      break
  if pol1 < pol2:
    max = 0
    for i in range(len(mass1)):
      if mass1[i]>max:
        max = mass1[i]
        k = i
    mass1[k] = mass1[k]*0
    print('Массив 1, больший элемент заменён на 0: ',mass1)
    min = 0;p1=0
    for i in range(len(mass2)):
      if mass2[i]<min:
        min = mass2[i]
        p1 = i
    if p1<len(mass2):
      z_d  = mass2[:p1]  
      z_p = 2*np.array(mass2[p1:])
      print('Массив 2, элементы после min умножены на 2: ',*z_d,*z_p)
    else:
      print(mass2)
      
    
  else:
    max = 0
    for i in range(len(mass2)):
      if mass2[i]>max:
        max = mass2[i]
        k = i
    mass2[k] = mass2[k]*0 
    print('Массив 2, больший элемент заменён на 0: ',mass2)
    min = 0;p2=0
    for i in range(len(mass1)):
      if mass1[i]<min:
        min = mass1[i]
        p2 = i
    if p2<len(mass1):
      z_d  = mass1[:p2]  
      z_p = 2*np.array(mass1[p2:])
      print('Массив 1, элементы после min умноржены на 2: ',*z_d,*z_p)
    else:
      print(mass1)
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