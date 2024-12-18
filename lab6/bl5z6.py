def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A <= 0 or B <= 0:
    print("Ошибка! Числа должны быть натуральными")
else:
    nod = gcd(A, B)
    nok = lcm(A, B)
    print("Наибольший общий делитель (НОД):", nod)
    print("Наименьшее общее кратное (НОК):", nok)
