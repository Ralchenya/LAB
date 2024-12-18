sequence = [2, 4, 4, 3, 8, 10]
sum_even = 0
i = 0
while sequence[i] % 2 == 0:
    sum_even += sequence[i]
    i += 1
print("Сумма всех идущих подряд четных чисел:", sum_even)
