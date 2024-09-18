nums = [3, 5, 7, 8, 12]
cubes = []
for num in nums:
    cubeOfTheNumber = num*num*num
    cubes.append(cubeOfTheNumber)
for num in cubes:
    print(num)
dict = {}

dict['parrot'] = 2
dict['goat'] = 4
dict['spider'] = 8
dict['crab'] = 10
sumOfLegs = 0
for item in dict.items():
    print(item)
for key in dict:
    sumOfLegs = sumOfLegs + dict[key]
print(sumOfLegs)
A = (3, 9, 4, [5, 6])
nums = [3, 6, 12, 24, 12]
del A
B = ('a', 'p', 'p', 'l', 'e')
occurrencesOfCharacter = 'p'
occurrencesSum = 0
for item in B:
    if item == occurrencesOfCharacter:
        occurrencesSum = occurrencesSum +1
print(occurrencesSum)
indexOfCharacter = 'l'
indexIs = B.index(indexOfCharacter)
print(indexIs)