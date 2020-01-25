# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:06:56 2020

@author: ojhag
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_LL(self):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        else:
            n = self.start_node
            while n is not None:
                if n.ref == None:
                    print(n.val)
                else:
                    print(n.val, end="->")
                n = n.ref
                
    def insert_at_begin(self,val):
        new_node = Node(val)
        new_node.ref = self.start_node
        self.start_node = new_node
        
    def insert_at_end(self,val):
        new_node = Node(val)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    
    def insert_after_node(self,x,val):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        n = self.start_node
        while n is not None:
            if n.val == x:
                break
            n = n.ref
        
        if n is None:
            print("Node after which you want to insert is not found!")
            return 
        else:
            new_node = Node(val)
            new_node.ref = n.ref
            n.ref = new_node
        
    def insert_before_node(self,x,val):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        if x == self.start_node.val:
            new_node = Node(val)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.val == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node before which you want to insert is not found!")
            return 
        else:
            new_node = Node(val)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_specific_index(self,index,val):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        if index == 1:
            new_node = Node(val)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        i = 1
        n = self.start_node
        while i < index-1:
            n = n.ref
            i += 1
        if n is None:
            print("Index out of Bound")
            return 
        else:
            new_node = Node(val)
            new_node.ref = self.start_node
            self.start_node = new_node
    
    def count_nodes(self):
        if self.start_node is None:
            print("Number of Nodes: 0")
            return 
        counter = 0
        n = self.start_node
        while n is not None:
            counter += 1
            n = n.ref
        return counter
    
    def delete_begin(self):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        self.start_node = self.start_node.ref
    
    def delete_from_end(self):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def del_after_Node(self,x):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        n = self.start_node
        while n is not None:
            if n.val == x:
                break
            n = n.ref
        
        if n is None:
            print("Node after which you want to insert is not found!")
            return 
        if n.ref is None:
            print("You reached the end of the list no node found after the specified node!")
            return
        else:
            n.ref = n.ref.ref
            
    def del_before_Node(self,x):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        if x == self.start_node.val:
            print("You have Entered the value of the first node there are no nodes before the first node")
            return
        n = self.start_node
        #n1 = n.ref
        prev = None
        while n.ref is not None:
            if n.ref.val == x:
                break
            prev = n
            n = n.ref
            #n1 = n1.ref
        if n.ref is None:
            print("Node before which you want to delete not found")
            return
        if n.val == self.start_node.val:
            self.start_node = self.start_node.ref
            return
        else:
            prev.ref = n.ref
        
    def del_specific_node(self,x):
        if self.start_node is None:
            print("Linked List is Empty")
            return 
        if x == self.start_node.val:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n is not None:
            if n.val == x:
                break
            n = n.ref
        if n is None:
            print("The Node to be deleted not found")
            return 
        else:
            n.ref.val,n.val = n.val,n.ref.val
            n.ref = n.ref.ref
    
    def rev_LL(self):
        prev = None
        curr = self.start_node
        while curr is not None:
            nextp = curr.ref
            curr.ref = prev
            prev = curr
            curr = nextp
        self.start_node = prev
        
    def create_LL(self):
        nums = int(input("Number of Nodes:"))
        if nums == 0:
            print("No Nodes created")
            return 
        for i in range(nums):
            #j = i+1
            value = input("Value of Node:")
            self.insert_at_end(value)
        
        
list = LinkedList()
list.delete_begin()
list.create_LL()
list.traverse_LL()
# print(list.traverse_LL())
# print("Start with adding elements to the list:")
# print("\n")
# list.start_node = Node("1")
# node2 = Node("2")
# node3 = Node("3")
# list.start_node.ref = node2
# node2.ref = node3

# list.insert_at_end("4")
# list.insert_at_begin("0")
# print("Intial Linked List")
# list.traverse_LL()
# print("\n")
# print("Inserting After 4 Node")
# list.insert_after_node("4","6")
# list.traverse_LL()
# print("\n")
# print("Inserting Before 6 Node")
# list.insert_before_node("6","5")
# list.traverse_LL()
# print("\n")

# print("\n")
# print("Insert at Index 1")
# list.insert_at_specific_index(1,"-1")
# list.traverse_LL()
# print("\n")
# print("Number of Nodes: ",list.count_nodes())
# print('\n')
# list.delete_begin()
# list.traverse_LL()

# list.delete_from_end()
# list.traverse_LL()

# print("Reverse a LL()")
# list.rev_LL()
# list.traverse_LL()
# list.del_after_Node("3")
# list.traverse_LL()

# list.del_before_Node("1")
# list.traverse_LL()

# list.del_specific_node("5")
# list.traverse_LL()




        
        
        