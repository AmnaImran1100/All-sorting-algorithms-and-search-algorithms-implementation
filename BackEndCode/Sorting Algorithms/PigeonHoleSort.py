def main():
    A = [8, 9, 10, 6, 5, 2, 4, 7, 3, 1]      
    result = PigeonHoleSort(A)
    print (result)

def PigeonHoleSort(A):
    sortedArray = []
    Smallest = min(A)
    Largest = max(A)
    NumberOfHoles = Largest - Smallest + 1
    Holes = []

    for i in range (NumberOfHoles):
        Holes.append(0)

    for j in A:
        Holes[j - Smallest] = Holes[j - Smallest] + 1
        
    for x in range (NumberOfHoles):
        while (Holes[x] > 0):
            Holes[x] = Holes[x] - 1
            sortedArray.append(x + Smallest)
    return sortedArray

if __name__ == "__main__":
    main()
