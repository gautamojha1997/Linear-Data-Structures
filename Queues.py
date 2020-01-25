# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:52:51 2020

@author: ojhag
"""

class Queue:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        return self.arr == []
    
    def enqueue(self,item):
        self.arr.insert(0, item)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.arr.pop()
    
    def showQ(self):
        return self.arr
    
q = Queue()
print("Is the Queue Empty:",q.isEmpty())
print("Adding 2 to the Queue")
q.enqueue(2)
print("Adding String to the Queue")
q.enqueue("Cold")
print("Adding 3.14 to the Queue")
q.enqueue(3.14)
print("The Queue is : ",q.showQ())
print("Is the Queue Empty:",q.isEmpty())
print("\n")
print("Dequeue from the Queue")
q.dequeue()
print("The Queue is : ",q.showQ())
print("Dequeue from the Queue")
q.dequeue()
print("The Queue is : ",q.showQ())
print("Dequeue from the Queue")
q.dequeue()
print("The Queue is : ",q.showQ())
print("Dequeue from the Queue")
print(q.dequeue())

