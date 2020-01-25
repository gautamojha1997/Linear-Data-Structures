# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:18:14 2020

@author: ojhag
"""

class Stack:
    def __init__(self):
        self.arr = []
    
    def pushitem(self,item):
        self.arr.append(item)
    
    def popitem(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.arr.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.arr[len(self.arr)-1]
    
    def isEmpty(self):
        return self.arr == []
    
    def showStack(self):
        return self.arr

s = Stack()
print("Is the Stack Empty: ",s.isEmpty())
print("Adding 2 and 3 in stack")
s.pushitem(2)
s.pushitem(3)
print(s.showStack())
print("Is the Stack Empty:",s.isEmpty())
print("\n")
print("Pop 3 from stack")
s.popitem()
print(s.showStack())
print("Adding string and integer to the stack")
s.pushitem("Gautam Ojha")
s.pushitem(555)
print(s.showStack())
print("Peek the stack top")
print(s.peek())
print("Pop every element from the stack")
print("Item Pop",s.popitem())
print("Item Pop",s.popitem())
print("Item Pop",s.popitem())
print("Is the stack empty:",s.isEmpty(),s.showStack())