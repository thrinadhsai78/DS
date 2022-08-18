class maxHeap:

    def __init__(self,A,n):
        self.A = A
        self.n = n

    def print(self):
        for i in range(self.n) : print(self.A[i],end=" ")
        print()

    def heapify(self,i=0):  
        l = 2*i+1
        r = 2*i+2
        b = l if l<self.n and self.A[l]>self.A[i] else i
        if r<self.n and self.A[b]<self.A[r] : b=r
        if b!=i : 
            self.A[b],self.A[i] = self.A[i],self.A[b]
            self.heapify(b)

    def buildHeap(self):
        def ceilf(num,factor):
            val = num//factor
            return val if val==num/factor else val+1 

        for i in range(ceilf(self.n,2)-1,-1,-1) :
            self.heapify(i)
            pass

    def extract(self):
        if self.n==0 : return -1
        b = self.A[0]
        self.A[0] = self.A[self.n-1]
        self.n-=1
        self.heapify()
        return b

    def kthel(self,k):
        for _ in range(k-1):
            self.extract()
        return self.extract() 


'''
arr = [3, 6, 5, 0, 8, 2, 1, 9]
n = len(arr)
heap1 = maxHeap(arr,n)
heap1.print()
heap1.buildHeap()
heap1.print()
print(heap1.extract())
heap1.print()
print(heap1.kthel(4))
heap1.print()
'''
