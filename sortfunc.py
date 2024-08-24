nums = [5, 6, 2, 1, 3, 4]


def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls


print(bubble_sort(nums))


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(len(ls) - 1):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
        return ls


print(selection_sort(nums))


def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


print(insertion_sort(nums))
