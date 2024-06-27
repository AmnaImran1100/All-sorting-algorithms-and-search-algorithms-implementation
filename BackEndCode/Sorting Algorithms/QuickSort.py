def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])
    
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

array = [7, -2, 8, 5, 9, 2, 4, 10]
quickSort(array, 0, len(array) - 1)
print(array)



