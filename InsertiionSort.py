##InsertionSort By Sami ##
def insertionSort (customList):
    for i in range (1,len(customList)):
        key = customList[i]
        j= i-1
        while j>=0  and key < customList[j]:
            customList[j+1] = customList[j]
            j -=1
        customList[j+1] = key
        print(customList)
saua = [32,3,40,5,6,345,35676,50,54]
insertionSort(saua)
