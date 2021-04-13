import random       # import random lib

numberList = list() # or [] ; type(numberList) --> Return type of Object

for i in range(30):
  numberList.append(random.randint(1,86))

def numberGroups(numberList, divider):
  '''receive a integer number and return a set'''
  setGroup = set()
  for number in numberList:
    if number % divider == 0:
      setGroup.add(number)
  return setGroup

twoMult = numberGroups(numberList,2)
threeMult = numberGroups(numberList,3)
fiveMult = numberGroups(numberList,5)

#print( " ".join(map(str,twoMult)))

# Math 
twoMult.intersection(threeMult)
twoMult.union(threeMult)
twoMult.union(threeMult).intersection(fiveMult)
fiveMult.difference(twoMult)
 
