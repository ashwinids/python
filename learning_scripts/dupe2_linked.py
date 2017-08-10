#!/usr/bin/env python

class Node(object):
   def __init__(self,data):
      self.data = data
      self.next = None
   
   def getData(self):
      return self.data
   
   def setNext(self,node):
      self.next = node
   
   def getNext(self):
      return self.next

class linkedList(object):

   def __init__(self,dataList):
      assert len(dataList) > 0
      self.head = Node(dataList[0])
      iterNode = self.head
      
      for i in range(1, len(dataList)):
         iterNode.setNext(Node(dataList[i]))
         iterNode = iterNode.getNext()
      iterNode.setNext(None)   
    
   def printList(self):
      iterNode=self.head
      
      while  iterNode is not None:
         print(iterNode.getData()) 
         iterNode = iterNode.getNext()
    
   
   def removeDuplicates(self):
      anchor = self.head
        
      if anchor is not None:
         iterator = anchor
         while iterator is not None:
            prev = iterator
            iterator = iterator.getNext()
            if iterator is None:
               break
            if iterator.getData() == anchor.getData():
               next = iterator.getNext()
               prev.setNext(next)
         anchor = anchor.getNext()

dataList = ["hello", "world", "people", "hello", "hi", "hi"]

Linked = linkedList(dataList)
Linked.printList()
Linked.removeDuplicates()
print("\n")
Linked.printList()  
          
      
