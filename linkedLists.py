from http.client import NotConnected


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head: 
            temp = self.head
            while temp.next:
                temp = temp.next 
            temp.next = node; return
        self.head = node 

    def print(self):
        if self.head is None : print('empty')
        temp = self.head
        while temp.next:
            print(temp.data,end='-->')
            temp = temp.next 
        print(temp.data)

    def reverse(self):
        if self.head is None : return self
        if self.head.next is None : return self 
        prev = self.head
        curr = prev.next
        prev.next = None
        while curr:  
            curr.next, curr, prev = prev, curr.next, curr
        self.head = prev

    def isPal(self):
        if self.head is None or self.head.next is None : return True
        if self.head.next.next is None : return self.head.data==self.head.next.data 
        self.head2 = None
        slow = self.head
        fast = self.head
        pass

arr = [12,56,78]
ll1 = LinkedList()
for i in arr:
    ll1.insert(i)
ll1.print()
ll1.reverse()
ll1.print()

print(ll1.isPal())
