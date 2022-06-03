elements_count = int(input('Введите количество элементов: '))
result = []
for i in range(elements_count):
    element_val = int(input('Введите значение элемента: '))
    result.append(element_val)

result.sort()
print(result)