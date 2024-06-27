import numpy as np

def main():
    A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    result = BucketSort(A)
    print (result)

def InsertionSort(array):
    for j in range (len(array)):   
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i] > key):
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key  
    return array

def BucketSort(A):
    B = []
    n = len(A)
    for i in range (n):
        B.append([])
    for i in range (n):
        B[int(n * A[i])].append(A[i])
    for i in range (n):
        B[i] = InsertionSort(B[i])
    B = np.concatenate(B)
    return B

if __name__ == "__main__":
    main()
        
        
    
