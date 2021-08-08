#hashing function for integer data
def mod (number,cellNumber):
    return number % cellNumber

print(mod(400,241))

#hash function for string data

def modASCII(string,cellNumber):
    total = 0
    for i in string:
        total += ord(i)
        return total % cellNumber

print(modASCII("ABC",12))