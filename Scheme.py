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
        result = numpy.array(self.Adjacency(k)) * numpy.array(numpy.dot(self.Adjacency(i),self.Adjacency(j)))/self.Adjacency(k)
        #This is a terrible way to do this
        #Godsil has numpy.sum(numpy.array(self.Adjacency(k)) * numpy.array(numpy.dot(self.Adjacency(i),self.Adjacency(j))))/vv_k
        #but what is v_k? v = 6 doesn't seem to work for any values of v_k
        for x in range(0,len(result)):
            for y in range(0,len(result)):
                if not math.isnan(result[x,y]):
                    return result[x,y]
        assert False
        #return numpy.trace(numpy.dot(numpy.dot(self.Adjacency(k).transpose(),self.Adjacency(i)),self.Adjacency(j)))

s1 = Scheme([[0,1,2,2,3,3],[1,0,2,2,3,3],[3,3,0,1,2,2],[3,3,1,0,2,2],[2,2,3,3,0,1],[2,2,3,3,1,0]])

print(s1.Adjacency(3))

#print(numpy.array(s1.Adjacency(3)) * numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array(s1.Adjacency(3)) @ numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array([[0,1],[1,5]])/numpy.array([[0,2],[3,2]]))

ps = numpy.zeros((4,4,4))
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            ps[i,j,k] = s1.P(i,j,k)
print(ps)
