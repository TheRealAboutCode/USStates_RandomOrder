from random import randint

f = open("/Users/macuser/AboutCode/1__ListOfUSStatesInRandomOrder/data/primaryList.txt", "r")


myList = []
for x in f:
#  print(x)
#   print(x)
#   x = x.strip()
   if (len(x) == 0):
      continue
   y = x.split()

#   print(y)

   if(y[0] == "IGNORE"):
      continue
   myList.append(y[2])

#print(myList)

myListOfStates_Sorted = myList

myListLen = len(myList)

#print(myListLen)

myListOfNumbers = []
for index in range(myListLen):
#   print index
    myListOfNumbers.append(index)
#    continue  

#print(myListOfNumbers)

currLengthOfList = myListLen

myrandomList = []

for index in range(myListLen):
   # pick a random number in the range (0, currLengthOfList)
    my_random_num = randint(0, currLengthOfList - 1)
    currLengthOfList = (currLengthOfList - 1)
    
    # pop that number
    popped_number = myListOfNumbers.pop(my_random_num)
    
    myrandomList.append(popped_number)

#print(myrandomList)
myListOfStates_Random = []


for index in range(myListLen):
    myListOfStates_Random.append(None);

for index in range(myListLen):
    whichIndex = myrandomList[index]
    myListOfStates_Random[index] = myListOfStates_Sorted[whichIndex]

print myListOfStates_Random
