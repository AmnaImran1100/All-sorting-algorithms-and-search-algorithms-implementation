def insertionSort(array, start, end):
    i = 0
    key = 0

    for j in range(start, end):
        key = array[j]
        i = j - 1
        
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1 
            array[i + 1] = key

def merge (array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range (n1):
        L.append( array[p + i] )
    for j in range (n2):
        R.append( array[q + j + 1] )
    L.append( 999999999 )
    R.append( 999999999 )
    i = 0
    j = 0
    for k in range (p, r + 1):
        if (L[i] < R[j]):            
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1

def timSort(array):
    length = len(array)
    minRun = 32

    for p in range(0, length, minRun):
        r = min(p + minRun - 1, length -1)
        insertionSort(array, p, r)

    size = minRun
    while size < length:
        for p in range(0, length, 2 * size):
            q = min(length - 1, p + size - 1)
            r = min((p + 2 * size - 1), (length - 1))

            if q < r:
                merge(array, p, q, r)        

        size = 2 * size

array = [7, -2, 8, 5, 9, 2, 4, 10]
timSort(array)
print(array)

    