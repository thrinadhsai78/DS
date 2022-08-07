
'''
class B:
    def __init__(self):
        self.a = 78
        print('class B initialized') 

class A(B):
    def func(self):
        ob1 = super().__init__()
        print(ob1.a)

ob = A()



class b:
    def __init__(self):
        print('haii')
class a(b):
    def printa():
        print('wow')
ob=a()



class a1:

    class b1:
        def __init__(self): 
            self.num = 78
            print('b1')

    def fun(self):
        ob1 = self.b1()
        print(ob1.num)

ob = a1()
ob.fun()
'''

import minHeap

arr = [1,5,4,7,8,9,6,4,2,3]
heap1 = minHeap(arr,len(arr))
heap1 = minHeap(arr,n)
heap1.print()
heap1.buildHeap()
heap1.print()
print(heap1.extract())
heap1.print()

print(heap1.kthel(4))
heap1.print()
