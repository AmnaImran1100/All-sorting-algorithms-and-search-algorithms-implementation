def main():
    A = [2, 5, 3, 0, 2, 3, 0, 3]    
    B = [0 for i in range(len(A))]
    k = A[0]
    for i in range (len(A)):
        if (A[i] > k):
            k = A[i] + 1   
    array = CountingSort(A, B, k)
    print(array)
        
    
def CountingSort(A, B, k):
    C = []
    for i in range (k):
        C.append(0)
    for j in range (len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range (1, k):
        C[i] = C[i] + C[i - 1]
    for j in range (len(A), 0 , -1):
        B[(C[A[j-1]]) - 1] = A[j - 1]
        C[A[j - 1]] = C[A[j - 1]] - 1
    return B

if __name__ == "__main__":
    main()


    
        

