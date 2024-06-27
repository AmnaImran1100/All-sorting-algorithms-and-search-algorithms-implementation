import random
import time 

def Merge (array, p, q, r):
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


       
def MergeSort (array, start, end):
    p = start
    r = end
    if (p < r): 
        q = int((p + r) / 2)
        MergeSort (array, p, q)
        MergeSort (array, q + 1, r)
        Merge (array, p, q, r)


array = [7, 8, 5, 9, 2, 4, 10, 1]
MergeSort(array, 0 , 7)
print(array)
