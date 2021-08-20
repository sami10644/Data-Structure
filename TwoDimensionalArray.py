import numpy as np

samiarray = np.array([[1,2,3,4],[12,12,131434,23],[3,6,9,54],[34,4,7,3],[3,345,343,5645]])
print(samiarray)
sami2array = np.insert(samiarray,1,[[3,4,6,3]],axis =0)
print(sami2array)
print(len(sami2array))
print(len(sami2array[0]))

def accessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])
accessElements(sami2array,1,3)

def traverse2DarrayJ(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2DarrayJ(samiarray)
def searchTDarray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return'The value is located in index '+str(i)+" "+str(j)
    return 'The Element not found'
print(searchTDarray(samiarray,30))

newsamiarray = np.delete(samiarray,1,axis = 1)
print(newsamiarray)