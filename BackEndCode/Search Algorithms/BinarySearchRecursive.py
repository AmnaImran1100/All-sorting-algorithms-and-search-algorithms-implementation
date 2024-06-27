def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1
 
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
 
    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")

array = ["abc", "bcd", "mno", "mno", "vst"]
element = "mno"
result = binarySearch(array, element)
 
if (result == -1):
    print("Not Found")
else:
    print("Found")