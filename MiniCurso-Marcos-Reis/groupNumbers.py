import random       # import random lib

twoMult = set()
threeMult = set() 
fourMult = set() 
fiveMult = set()
numberList = list() # or [] ; type(numberList) --> Return type of Object

for i in range(12300):
  numberList.append(random.randint(1,10000))

def numberGroups(numberList, divider):
  '''receive a integer number and return a set'''
  setGroup = set()
  for number in numberList:
    if number % divider == 0:
      setGroup.add(number)
    return setGroup

twoMult = numberGroups(numberList,2)
threeMult = numberGroups(numberList,3)
fourMult = numberGroups(numberList,4)
fiveMult = numberGroups(numberList,5)
