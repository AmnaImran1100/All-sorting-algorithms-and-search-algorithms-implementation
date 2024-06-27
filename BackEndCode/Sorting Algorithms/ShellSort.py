def shellSort(array):
    arrayLenght = len(array)
    gap = arrayLenght // 2

    while gap > 0:

        for i in range(gap, arrayLenght):
            j = array[i]
            idx = i

            while idx >= gap and j < array[idx - gap]:
                array[idx] = array[idx - gap]
                idx = idx - gap 

            array[idx] = j

        gap = gap - 1

array = [7, -2, 8, 5, 9, 2, 4, 10]
shellSort(array)
print(array)