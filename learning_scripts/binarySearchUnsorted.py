#!/usr/bin/env python


#Logic to sort the unsorted list
def sortedList():
   length = len(numList)
   for Index1 in range(1,length):
      value = numList[Index1]
      Index2 = Index1 - 1 
      while Index2 >= 0:
         if(value < numList[Index2]):
            numList[Index2 + 1] = numList[Index2]
            numList[Index2] = value
            Index2 = Index2 -1
         else: 
            break 
   return(numList) 
      
   
# Logic to extract search term with binary search
def binarySearch():
   print"Finding the input value",numToFind, "using binary search from the list", numList
   startIndex=0
   endIndex = len(numList) - 1
   isFound=0
   while(startIndex <= endIndex):
      mid=(startIndex+endIndex)/2
      midval=numList[mid]
      if(midval == numToFind):
         print numToFind, "is present"
         isFound=1
         break
      elif(numToFind > midval):
         startIndex = mid + 1
      elif(numToFind < midval):
         endIndex = mid - 1
   if (isFound == 0):
      print numToFind, "is not present"   

    
# Program startIndexs here.
numList = [15, 2, 4, 7, 11, 9, 5]

#numList = [2, 4, 5, 7, 9, 11, 15]
numToFind = int(raw_input("Enter number to be searched: "))
sortedList()
binarySearch()
