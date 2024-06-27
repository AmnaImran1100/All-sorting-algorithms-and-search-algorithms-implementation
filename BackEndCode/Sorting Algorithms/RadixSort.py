def main():
    A = [110, 45, 65, 50, 90, 602, 24, 2, 66]   
    d = max(A)      
    result = RadixSort(A, d)
    print (result)    
    
def CountingSort(A, B, n):
    C = [0] * 10
    for j in range (len(A)):
        temp = A[j] // n
        C[temp % 10] = C[temp % 10] + 1
    print (C)
    for i in range (1, 10):
        C[i] = C[i] + C[i - 1]
    print (C)
    i = len(A) - 1
    while (i >= 0):
        temp = A[i] // n
        B[C[temp % 10] - 1] = A[i]
        C[temp % 10] = C[temp % 10] - 1
        i = i - 1
    for i in range (len(A)):
        A[i] = B[i]
    return A

def RadixSort(A, d):
    B = [0 for i in range(len(A))]
    n = 1
    while (d // n > 0):
        A = CountingSort(A, B, n)
        n = n * 10
    return A

if __name__ == "__main__":
    main()
    

