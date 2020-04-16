from array import array
#from sage.all import *
import numpy as numpy
import math as math

class Scheme:
    def __init__(self,arr):
        for i in range(0,len(arr)):
            assert (len(arr) == len(arr[i])),"Adjacency matrix must be square"
        self.adj = numpy.matrix(arr)

    def Adjacency(self,i):
        toReturn = numpy.matrix(numpy.zeros((len(self.adj),len(self.adj))))
        for x in range(0,len(toReturn)):
            for y in range(0,len(toReturn)):
                if self.adj[x,y] == i:
                    toReturn[x,y] = 1
                else:
                    toReturn[x,y] = 0
        return toReturn

    def  P(self,i,j,k):
        result = numpy.array(self.Adjacency(k)) * numpy.array(numpy.dot(self.Adjacency(i),self.Adjacency(j)))
        #This is a terrible way to do this
        #Godsil has numpy.sum(numpy.array(self.Adjacency(k)) * numpy.array(numpy.dot(self.Adjacency(i),self.Adjacency(j))))/vv_k
        #but what is v_k? v = 6 doesn't seem to work for any values of v_k
        for x in range(0,len(result)):
            if not (result[0,x]==0):
                return result[0,x]
        return 0
        #return numpy.trace(numpy.dot(numpy.dot(self.Adjacency(k).transpose(),self.Adjacency(i)),self.Adjacency(j)))

s66 = Scheme([[0,1,2,2,3,3],[1,0,2,2,3,3],[3,3,0,1,2,2],[3,3,1,0,2,2],[2,2,3,3,0,1],[2,2,3,3,1,0]])

s910 = Scheme([[0,1,2,3,3,4,4,5,5 ],[ 2,0,1,4,4,5,5,3,3 ],[ 1,2,0,5,5,3,3,4,4 ],[ 3,5,4,0,3,2,4,1,5 ],[ 3,5,4,3,0,4,2,5,1 ],[ 5,4,3,1,5,0,3,2,4 ],[ 5,4,3,5,1,3,0,4,2 ],[ 4,3,5,2,4,1,5,0,3 ],[ 4,3,5,4,2,5,1,3,0 ]])

s113 = Scheme([ [ 0,1,1,2,2,3,3,4,4,5,5 ],
  [ 1,0,2,1,3,2,4,3,5,4,5 ],
  [ 1,2,0,3,1,4,2,5,3,5,4 ],
  [ 2,1,3,0,4,1,5,2,5,3,4 ],
  [ 2,3,1,4,0,5,1,5,2,4,3 ],
  [ 3,2,4,1,5,0,5,1,4,2,3 ],
  [ 3,4,2,5,1,5,0,4,1,3,2 ],
  [ 4,3,5,2,5,1,4,0,3,1,2 ],
  [ 4,5,3,5,2,4,1,3,0,2,1 ],
  [ 5,4,5,3,4,2,3,1,2,0,1 ],
  [ 5,5,4,4,3,3,2,2,1,1,0 ] ])

s122 = Scheme([ [ 0,1,2,2,2,2,2,2,2,2,2,2 ],
  [ 1,0,2,2,2,2,2,2,2,2,2,2 ],
  [ 2,2,0,1,2,2,2,2,2,2,2,2 ],
  [ 2,2,1,0,2,2,2,2,2,2,2,2 ],
  [ 2,2,2,2,0,1,2,2,2,2,2,2 ],
  [ 2,2,2,2,1,0,2,2,2,2,2,2 ],
  [ 2,2,2,2,2,2,0,1,2,2,2,2 ],
  [ 2,2,2,2,2,2,1,0,2,2,2,2 ],
  [ 2,2,2,2,2,2,2,2,0,1,2,2 ],
  [ 2,2,2,2,2,2,2,2,1,0,2,2 ],
  [ 2,2,2,2,2,2,2,2,2,2,0,1 ],
  [ 2,2,2,2,2,2,2,2,2,2,1,0 ] ])

s1254 = Scheme([ [ 0,1,2,3,4,5,6,6,7,7,8,8 ],
  [ 1,0,4,5,2,3,6,6,7,7,8,8 ],
  [ 3,5,0,2,1,4,7,7,8,8,6,6 ],
  [ 2,4,3,0,5,1,8,8,6,6,7,7 ],
  [ 5,3,1,4,0,2,7,7,8,8,6,6 ],
  [ 4,2,5,1,3,0,8,8,6,6,7,7 ],
  [ 6,6,8,7,8,7,0,1,3,5,2,4 ],
  [ 6,6,8,7,8,7,1,0,5,3,4,2 ],
  [ 8,8,7,6,7,6,2,4,0,1,3,5 ],
  [ 8,8,7,6,7,6,4,2,1,0,5,3 ],
  [ 7,7,6,8,6,8,3,5,2,4,0,1 ],
  [ 7,7,6,8,6,8,5,3,4,2,1,0 ] ])


#print(numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(3))))

#print(numpy.array(s1.Adjacency(3)) * numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array(s1.Adjacency(3)) @ numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array([[0,1],[1,5]])/numpy.array([[0,2],[3,2]]))

size = len(s122.adj)
ps = numpy.zeros((size,size,size))
for i in range(0,size):
    for j in range(0,size):
        for k in range(0,size):
            ps[k,i,j] = s122.P(i,j,k)
numpy.set_printoptions(threshold=numpy.inf)
print(ps)



"""
example
[
[1 0 0 0]  [0 1 0 0]  [0 0 1 0]  [0 0 0 1]
[0 0 1 0]  [1 0 0 0]  [0 1 0 0]  [0 0 0 1]
[0 1 0 0]  [0 0 1 0]  [1 0 0 0]  [0 0 0 1]
[0 0 0 3], [0 0 0 3], [0 0 0 3], [1 1 1 0]
]


"""