def BubbleSort(array, start, end):
    
    for i in range(start, end):
        
        for j in range(start, end):
            
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])

array = [7,4,3,9,6,1]
BubbleSort(array, 0, 5)
print(array)