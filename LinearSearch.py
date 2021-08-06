def linearSearch(arr, val): # time - O(N) ,space - O(1)
    for i in range(len(arr)):

        if arr[i] == val:
            return i
    return -7897
print(linearSearch([34,76,45,23,59,7,89,0],23))
print(linearSearch([34,76,45,23,59,7,89,0],69))
