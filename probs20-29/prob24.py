nums = [0,1,2,3,4,5,6,7,8,9]

def remove_item(someList, item):
    newList = []
    for i in someList:
        if i != item:
            newList.append(i)
    return newList

def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if len(inputList) == 0:
        return [[]]
    if len(inputList) == 1:
        return [inputList]
    permutations = []
    for item in inputList:
        smallerPermutations = permute(remove_item(inputList,item))
        for i in range(len(smallerPermutations)):
            smallerPermutations[i].append(item)
        permutations += smallerPermutations
    permutations.sort()
    return permutations

print(permute(nums)[999999])