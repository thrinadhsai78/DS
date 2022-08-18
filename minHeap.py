class minHeap:

    def __init__(self,A,n):
        self.A = A
        self.n = n

    def print(self):
        for i in range(self.n) : print(self.A[i],end=" ")
        print()

    def heapify(self,i=0):  
        l = 2*i+1
        r = 2*i+2
        s = l if l<self.n and self.A[l]<self.A[i] else i
        if r<self.n and self.A[s]>self.A[r] : s=r
        if s!=i : 
            self.A[s],self.A[i] = self.A[i],self.A[s]
            self.heapify(s)

    def buildHeap(self):
        def ceilf(num,factor):
            val = num//factor
            return val if val==num/factor else val+1 

        for i in range(ceilf(self.n,2)-1,-1,-1) :
            self.heapify(i)
            pass

    def extract(self):
        if self.n==0 : return -1
        s = self.A[0]
        self.A[0] = self.A[self.n-1]
        self.n-=1
        self.heapify()
        return s

    def kthel(self,k):
        for _ in range(k-1):
            self.extract()
        return self.extract() 

    


'''
arr = [3, 6, 5, 0, 8, 2, 1, 9]
n = len(arr)
heap1 = minHeap(arr,n)
heap1.print()
heap1.buildHeap()
heap1.print()
print(heap1.extract())
heap1.print()

print(heap1.kthel(4))
heap1.print()
'''

'''
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
heap1 = minHeap(arr,n)
heap1.print()
print(heap1.kthel(k))
'''
