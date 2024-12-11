import math
x = float(input('Введите значение x:'))
y = float(input('Введите значение y:'))
if (x < 0 and y < 0) or (x > 0 and y > 0):
    s = math.sqrt(x * y)
    print('Среднее геометрическое:', s)
else:
    s = (x + y) / 2
    print('Среднее арифметическое:', s)
