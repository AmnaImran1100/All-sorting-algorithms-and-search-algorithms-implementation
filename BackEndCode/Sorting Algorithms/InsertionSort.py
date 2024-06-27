def InsertionSort(array, start, end):
    i = 0
    key = 0

    for j in range(start, end):
        key = array[j]
        i = j - 1
        
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1 
            array[i + 1] = key

array = [7,4,3,9,6,1]
InsertionSort(array, 1, 6)
print(array)