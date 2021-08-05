##Bubble Sort BY Sami ##
def bubblesort(customList):  #time - 0(n^2), Space - 0(1)
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1] = customList[j+1],customList[j]
    print(customList)

samlist = [678,100,31,567,43,2,4,23]

bubblesort(samlist)