A = int(input('Введите число A:'))
B = int(input('Введите число B:'))
if A >= B:
    print('A должно быть меньше B')
else:
    sum = 0
    for number in range(A, B + 1):
        sum += number ** 2
    print('Сумма', A, 'до', B, 'равна:', sum)
