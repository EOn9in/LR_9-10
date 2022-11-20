def max_number(mass):
  num = 0
  for i in range(len(mass)):
    if abs(mass[i]) < abs(mass[num]):
      num = i
      min = mass[i]  
  print('Mинимальный по модулю элемент: ',min)
  i = 0
  pos = -1
  while i < len(mass):
    if mass[i] < 0 and pos == -1:
      pos = i
    elif mass[i] < 0 and mass[i] > mass[pos]:
      pos= i
    i += 1
  print('Mаксимальный отрицательный элемент',mass[pos])
print('Введите длину массива: ',end='')
n = int(input())
array = []
for i in range(n):
  array.append(int(input()))
print(array)
b = max_number(array)
print(b)
  