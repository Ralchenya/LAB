array = [10, 20, 5, 30, 14, 8, 22, 12]
for i in range(len(array)):
    if array[i] < 15:
        array[i] = array[i] * 2
print("Преобразованный массив:", array)
