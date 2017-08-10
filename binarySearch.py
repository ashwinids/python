#!/usr/bin/env python

# Logic to extract search term with binary search
def binarySearch():
   print"Finding the input value",numToFind, "using binary search from the list", sortedList
   startIndex=0
   endIndex = len(sortedList) - 1
   isFound=0
   while(startIndex <= endIndex):
      mid=(startIndex+endIndex)/2
      midval=sortedList[mid]
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
sortedList = [2, 4, 5, 7, 9, 11, 15]
numToFind = int(raw_input("Enter number to be searched: "))
binarySearch()
