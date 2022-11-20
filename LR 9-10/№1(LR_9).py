def proiz(mass):
    result = 1
    for x in mass:
        result = result * x
    return result
print('Введите длину массива: ',end='')
n = int(input())
m = []
for i in range(n):
  m.append(int(input()))
print('Произведение элементов массива: ',proiz(m))