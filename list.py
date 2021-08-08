#Accessing or Traversing the list

samList = ['Milk','cheese','Butter']

for i in range(len(samList)):
    samList[i] = samList[i]+"+"

    print(samList[i])
empty = []
for i in empty:
    print("I am empty")
#update/Insert - List

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,13)
myList.append(232)

newlist = [11,12,13,14,15,16,17]
myList.extend(newlist)
print(myList)

#searching for an element in the list

myList = [10,20,30,50,40,60]
def searchList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
        return 'The value does not exist in the list'
print(searchList(myList,40))

#List operations/ Functions

total = 0
count = 0
while(True):
    inp = input('ENter a Number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total /count
print('Average:' , average)

numlist = list()
while (True):
    inp = input('ENter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)