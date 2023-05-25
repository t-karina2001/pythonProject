# 1. Написать функцию bubble_sort или selection_sort, принимающую в качестве
# входящего параметра не отсортированный список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или
# методом сортировки выбором.
def bubble_sort(no_sorted):
    n = len(no_sorted)
    for i in range(n-1):
        for j in range(n-i-1):
            if no_sorted[j] > no_sorted[j+1]:
                no_sorted[j], no_sorted[j+1] = no_sorted[j+1], no_sorted[j]
    return no_sorted

# 3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию
no_sorted = [9, 3, 6, 2, 1, 8, 5]
sorted_list = bubble_sort(no_sorted)
print("Отсортированный список:", sorted_list)


# 4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент
# для поиска и список в котором необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
def binary_search(object, list):
    first = 0
    last = len(list) - 1
    while first < last:
        middle = (first + last) // 2
        if list[middle] == object:
            return middle
        elif list[middle] < object:
            first = middle + 1
        else:
            last = middle - 1
    return False

# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию
search_object = 2
position = binary_search(search_object, sorted_list)
if position != False:
    print(f'Элемент найден. Текущая позиция элемента: {position}')
else:
    print("Элемент не найден!")



