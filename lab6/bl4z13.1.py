array = [1, 2, 3, 2, 5, 1, 6, 3, 7]
elements_dict = {}
for index, value in enumerate(array):
    if value in elements_dict:
        elements_dict[value].append(index)
    else:
        elements_dict[value] = [index]
duplicates_found = False
for value, indices in elements_dict.items():
    if len(indices) > 1:
        print(f"Элемент {value} повторяется на индексах: {indices}")
        duplicates_found = True
if not duplicates_found:
    print("Повторяющихся элементов не найдено.")
