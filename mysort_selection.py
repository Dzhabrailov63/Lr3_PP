from tqdm import tqdm

# вес паспорт снилс возраст


"""def bubble_sort(lst: list, name_field: str):

    n = len(lst)
    check = True
    while check:
        check = False
        for i in tqdm(range(n - 1)):
            if lst[i][name_field] > lst[i + 1][name_field]:
                c = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = c
                check = True"""


def selection_sort(lst: list, flag: str):
    for i in tqdm(range(len(lst))):
        minimum = i

        for j in range(i + 1, len(lst)):
            # Выбор наименьшего значения
            if lst[j][flag] < lst[minimum][flag]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        lst[minimum][flag], lst[i][flag] = lst[i][flag], lst[minimum][flag]

    return lst