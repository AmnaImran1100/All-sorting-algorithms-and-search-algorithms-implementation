def genomeSort(array):
    length = len(array)
    idx = 0 

    while idx < length:

        if idx == 0 or array[idx] >= array[idx - 1]:
            idx = idx + 1

        else:
            (array[idx], array[idx - 1]) = (array[idx - 1], array[idx])
            idx = idx - 1

    return array 

array = [9, 12, 2, 1, 11, 18, 65, 33]   
sorted = genomeSort(array)
print(sorted)