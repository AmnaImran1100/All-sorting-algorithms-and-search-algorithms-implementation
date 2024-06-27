def cocktailSort(array):
    length = len(array)

    for i in range(length - 1, 0, -1):

        for j in range(i):
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])

        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                (array[j], array[j - 1]) = (array[j - 1], array[j]) 

array = [-1, 9, 6, 10, 33, 12, -2, 77]
cocktailSort(array)
print(array)