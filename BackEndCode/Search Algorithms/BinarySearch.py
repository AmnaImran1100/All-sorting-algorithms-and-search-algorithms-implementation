def binarySearch(array, element):
    start = 0
    end = len(array)
    while (start <= end):
        mid = start + ((end - start) // 2)
 
        result = (element == array[mid])

        if (result == 0):
            return mid - 1

        if (result > 0):
            start = mid + 1
 
        else:
            end = mid - 1
 
    return -1
 

array = ["abc", "bcd", "mno", "vst"]
element = "mno"
result = binarySearch(array, element)
 
if (result == -1):
    print("Not Found")
else:
    print("Found")
 