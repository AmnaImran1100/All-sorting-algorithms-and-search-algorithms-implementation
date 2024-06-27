def maxHeapify(A, length, i):

    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2

    if l < length and A[l] > A[i]:
        largest = l

    if r < length and A[r] > A[largest]:
        largest = r

    if largest != i:
        (A[i], A[largest]) = (A[largest], A[i])
        maxHeapify(A, length, largest)

def buildMaxHeapify(A, length):

    for i in range(length // 2, -1, -1):
        maxHeapify(A, length, i)

def heapSort(A):

    length = len(A)
    buildMaxHeapify(A, length)

    for i in range(length - 1, 0, -1):
        (A[i], A[0]) = (A[0], A[i])
        length = length - 1
        maxHeapify(A, i, 0)


A = [12, 5, 23, 16, 8, 90, 45, 2]
heapSort(A)
print(A)
