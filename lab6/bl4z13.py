array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_index = array.index(max(array))
min_index = array.index(min(array))
array[max_index], array[min_index] = array[min_index], array[max_index]
print("Массив после замены максимального и минимального элементов:")
print(array)
