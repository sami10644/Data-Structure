samtuple = ('m','b','c','d','e')
samtuple2 = tuple('copiu')

print(samtuple2)

#Access Tuple elements

print(samtuple[0])

#Traverse through tuple

for i in samtuple2:
    print(i)

for index in range(len(samtuple)):
    print(samtuple[index])
#How to search for an element in Tuple?

print('m' in samtuple)

def searchInTuple(pTuple,element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'
print(searchInTuple(samtuple,'a'))

#tuple operations / functions

mytuple = (1,2,3,4,5,6)
mytuple1 = (1,2,3,34,5,4)

print (mytuple+mytuple1)
print(mytuple *4)
print(2 in mytuple1)

mytuple1.count(0)
mytuple.index(6)