def SelectionSort(array, start, end):
    
    len = (end - start) + 1
    
    for i in range(len):
        min = i
        
        for j in range(i + 1, len):
            
            if array[j] < array[min]:
                min = j
                
        (array[i], array[min]) = (array[min], array[i])
    
    return array