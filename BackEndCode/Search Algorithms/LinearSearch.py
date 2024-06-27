def LinearSearch(list, element):
    length = len(list)
    flag = False
    idx = -1

    for i in range(0, length):

        if list[i] == element:
            flag = True
            idx = i

    if flag == True:
        return idx
    else:
        return -1 

array = [50, 89, 70, 55, 45]
element = 1
result = LinearSearch(array, element)
if result == -1:
    print("Not Found")
else:
    print("Found")


