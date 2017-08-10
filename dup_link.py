#!/usr/bin/env python

class Node:
    def __init__(self,initdata):
       self.data = initdata
       self.next = None

    def getData(self):
       assert len(initdata) > 0
       for i in range(0,len(initdata)):
          data = Node(initdata[i])
          #return self.dat
          print i
          print self.data

    def getNext(self):
       return self.next
       print self.next

    def setData(self,newdata):
       self.data = newdata

    def setNext(self,newnext):
       self.next = newnext
   
    def size(self):
       current = self.head
       count = 0
       while current != None:
          count = count + 1
          current = current.getNext()

       return count
       print count

initdata = [ 34, 67, 78, 66, 99 ]
linkedList = Node(initdata)
linkedList.getData()
#linkedList.size()

