#Bucket Sami #
import math
from InsertionSort import insertionSort


def bucketSort(customlist):
    n_buckets = round(math.sqrt(len(customlist)))
    max_value = max(customlist)

    temp_arr = []
    for i in range (n_buckets):
        temp_arr.append([]) #buckets

    for j in customlist:
        indexofBucket = math.ceil(j* n_buckets / max_value)
        temp_arr[indexofBucket-1].append(j)

        #print(indexofBucket)

    for j in range(n_buckets):
        temp_arr[i] = insertionSort(temp_arr[i])

    for i in range(n_buckets):
        temp_arr[i] = insertionSort(temp_arr[i])

    ##SAMI RADIX ##

    # A function to do counting sort of arr[] according to
    # the digit represented by exp.
    def countingSort(arr, exp1):

        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i] / exp1)
            count[int((index) % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

            # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] / exp1)
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

            # Method to do Radix Sort

    def radixSort(arr):

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            countingSort(arr, exp)
            exp *= 10

    # Driver code to test above
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)

    for i in range(len(arr)):
        print(arr[i]),

    #merge sorted buckets
    #this one are another method .btw didnt completed .
    k= 0
    for i in range(n_buckets):
        for j in range(len(temp_arr[i])):
            customlist[k] = temp_arr[i][j]
            k+=1
    return customlist

    #print(n_buckets)
    #print(max_value)

x = [1,45,44,5,77,3,32,56,77,88]
print(bucketSort(x))