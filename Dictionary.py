#upload / add an element to the dictationary

samdict = {'name': 'Sami' , 'age' : 24 }
samdict['address'] = 'Dhaka'
print(samdict)
 # traverse through a dictationary

def traverseDict(dict):


    for a in dict :

        print(a,dict[a])
traverseDict(samdict)

#searching a dictationary

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value :
            return key,value
    return 'The Value does not exist'
print(searchDict(samdict,24))

#Delete and remove a dictationary

samdict.pop('name')
#sorted method
samdict= { 'ekfkja':1 ,'ahfkjdhf':2,'ddd':3}
print(sorted(samdict,key=len))