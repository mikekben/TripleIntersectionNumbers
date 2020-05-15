from array import array
#from sage.all import *
import numpy as numpy
import math as math

class Scheme:
    def __init__(self,arr):
        for i in range(0,len(arr)):
            assert (len(arr) == len(arr[i])),"Adjacency matrix must be square"
        self.adj = numpy.matrix(arr)
        self.degree = len(arr)
        self.rank = numpy.amax(arr)+1

    def Adjacency(self,i):
        toReturn = numpy.matrix(numpy.zeros((len(self.adj),len(self.adj))))
        for x in range(0,len(toReturn)):
            for y in range(0,len(toReturn)):
                if self.adj[x,y] == i:
                    toReturn[x,y] = 1
                else:
                    toReturn[x,y] = 0
        return toReturn

    def IsSymmetric(self):
        if (not numpy.all(self.adj==self.adj.T)):
            return False
        if (not numpy.array_equal(numpy.identity(self.degree),self.Adjacency(0))):
            return False
        sum = numpy.zeros((self.degree,self.degree))
        for i in range(0,self.rank):
            sum = numpy.add(sum,self.Adjacency(i))
        if (not numpy.all(sum==1)):
            return False
        for i in range(0,self.rank):
            for j in range(0,self.rank):
                if (not numpy.array_equal(numpy.dot(self.Adjacency(i),self.Adjacency(j)),numpy.dot(self.Adjacency(j),self.Adjacency(i)))):
                    return False
        return True

    def InverseRelation(self, r):
        for i in range(0,self.rank):
            if self.P(r,i,0)>0:
                return i
        assert(False)

    def  P(self,i,j,k):
        assert (i<self.rank) and (j<self.rank) and (k <self.rank),"The requested structure constant does not exist"

        result = numpy.array(self.Adjacency(k)) * numpy.array(numpy.dot(self.Adjacency(i),self.Adjacency(j)))
        for x in range(0,len(result)):
            if not (result[0,x]==0):
                return result[0,x]
        return 0

    def Valency(self,i):
        return self.P(i,self.InverseRelation(i),0)

    def StructureConstants(self):
        ps = numpy.zeros((self.rank,self.rank,self.rank))
        for i in range(0,self.rank):
            for j in range(0,self.rank):
                for k in range(0,self.rank):
                    ps[k,i,j] = self.P(i,j,k)
        return ps


    #VERTICES ARE 1-INDEXED!
    #RELATIONS ARE 0-INDEXED!
    def RelationBetween(self, v1, v2):
        return self.adj[v1-1,v2-1]

    def TripleIntersectionNumber(self, v1,v2,v3, r1,r2,r3):
        count = 0
        for vertex in range(1,self.degree+1):
            if self.RelationBetween(v1,vertex)==r1 and self.RelationBetween(v2,vertex)==r2 and self.RelationBetween(v3,vertex)==r3:
                count+=1
        return count



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

s105 = Scheme([ [ 0,1,2,2,2,2,3,3,3,3 ],
  [ 1,0,2,2,2,2,3,3,3,3 ],
  [ 2,2,0,1,3,3,2,2,3,3 ],
  [ 2,2,1,0,3,3,2,2,3,3 ],
  [ 2,2,3,3,0,1,3,3,2,2 ],
  [ 2,2,3,3,1,0,3,3,2,2 ],
  [ 3,3,2,2,3,3,0,1,2,2 ],
  [ 3,3,2,2,3,3,1,0,2,2 ],
  [ 3,3,3,3,2,2,2,2,0,1 ],
  [ 3,3,3,3,2,2,2,2,1,0 ] ])

s106 = Scheme([ [ 0,1,2,2,2,2,3,3,3,3 ],
  [ 1,0,3,3,3,3,2,2,2,2 ],
  [ 2,3,0,2,2,2,1,3,3,3 ],
  [ 2,3,2,0,2,2,3,1,3,3 ],
  [ 2,3,2,2,0,2,3,3,1,3 ],
  [ 2,3,2,2,2,0,3,3,3,1 ],
  [ 3,2,1,3,3,3,0,2,2,2 ],
  [ 3,2,3,1,3,3,2,0,2,2 ],
  [ 3,2,3,3,1,3,2,2,0,2 ],
  [ 3,2,3,3,3,1,2,2,2,0 ] ])

s209 = Scheme([ [ 0,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3 ],
  [ 1,0,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2 ],
  [ 2,3,0,2,2,2,2,2,2,2,2,1,3,3,3,3,3,3,3,3 ],
  [ 2,3,2,0,2,2,2,2,2,2,2,3,1,3,3,3,3,3,3,3 ],
  [ 2,3,2,2,0,2,2,2,2,2,2,3,3,1,3,3,3,3,3,3 ],
  [ 2,3,2,2,2,0,2,2,2,2,2,3,3,3,1,3,3,3,3,3 ],
  [ 2,3,2,2,2,2,0,2,2,2,2,3,3,3,3,1,3,3,3,3 ],
  [ 2,3,2,2,2,2,2,0,2,2,2,3,3,3,3,3,1,3,3,3 ],
  [ 2,3,2,2,2,2,2,2,0,2,2,3,3,3,3,3,3,1,3,3 ],
  [ 2,3,2,2,2,2,2,2,2,0,2,3,3,3,3,3,3,3,1,3 ],
  [ 2,3,2,2,2,2,2,2,2,2,0,3,3,3,3,3,3,3,3,1 ],
  [ 3,2,1,3,3,3,3,3,3,3,3,0,2,2,2,2,2,2,2,2 ],
  [ 3,2,3,1,3,3,3,3,3,3,3,2,0,2,2,2,2,2,2,2 ],
  [ 3,2,3,3,1,3,3,3,3,3,3,2,2,0,2,2,2,2,2,2 ],
  [ 3,2,3,3,3,1,3,3,3,3,3,2,2,2,0,2,2,2,2,2 ],
  [ 3,2,3,3,3,3,1,3,3,3,3,2,2,2,2,0,2,2,2,2 ],
  [ 3,2,3,3,3,3,3,1,3,3,3,2,2,2,2,2,0,2,2,2 ],
  [ 3,2,3,3,3,3,3,3,1,3,3,2,2,2,2,2,2,0,2,2 ],
  [ 3,2,3,3,3,3,3,3,3,1,3,2,2,2,2,2,2,2,0,2 ],
  [ 3,2,3,3,3,3,3,3,3,3,1,2,2,2,2,2,2,2,2,0 ] ])

s814 = Scheme([ [ 0,1,2,3,4,4,5,5 ],
  [ 1,0,3,2,4,4,5,5 ],
  [ 2,3,0,1,5,5,4,4 ],
  [ 3,2,1,0,5,5,4,4 ],
  [ 5,5,4,4,0,1,2,3 ],
  [ 5,5,4,4,1,0,3,2 ],
  [ 4,4,5,5,2,3,0,1 ],
  [ 4,4,5,5,3,2,1,0 ] ])

s64 = Scheme([ [ 0,1,2,3,3,3 ],
  [ 2,0,1,3,3,3 ],
  [ 1,2,0,3,3,3 ],
  [ 3,3,3,0,1,2 ],
  [ 3,3,3,2,0,1 ],
  [ 3,3,3,1,2,0 ] ])




#print(numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(3))))

#print(numpy.array(s1.Adjacency(3)) * numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array(s1.Adjacency(3)) @ numpy.array(numpy.dot(s1.Adjacency(3),s1.Adjacency(0))))
#print(numpy.array([[0,1],[1,5]])/numpy.array([[0,2],[3,2]]))

"""
size = len(s122.adj)
ps = numpy.zeros((size,size,size))
for i in range(0,size):
    for j in range(0,size):
        for k in range(0,size):
            ps[k,i,j] = s122.P(i,j,k)
"""
numpy.set_printoptions(threshold=numpy.inf)

constants66 = s66.StructureConstants()


file = open("scheme813TINs.txt","w") 
 
 

currentScheme = s814



currentTIN = 0
print("started")
counts = numpy.zeros(currentScheme.degree)
for v1 in range(1,currentScheme.degree+1):
    for v2 in range(1,currentScheme.degree+1):
        for v3 in range(1,currentScheme.degree+1):
            for r1 in range(0,currentScheme.rank):
                for r2 in range(0,currentScheme.rank):
                    for r3 in range(0,currentScheme.rank):
                        currentTIN = currentScheme.TripleIntersectionNumber(v1,v2,v3,r1,r2,r3)
                        counts[currentTIN]+=1
                        file.write("[%c %c %c]\n" % (chr(64+v1),chr(64+v2),chr(64+v3)))
                        file.write("[%d %d %d] = %d\n" % (r1,r2,r3,currentTIN))
                        file.write("\n")

file.close()

print("done")
print(currentScheme.IsSymmetric())
print(counts)
print(sum(counts))
print(counts[0]/sum(counts))


#print(s66.TripleIntersectionNumber(1,2,3,0,1,3))

"""
print("n=6,#=6------------------")
print(s66.IsSymmetric)
#print(s66.StructureConstants())
print("n=9,#=10-----------------")
print(s910.IsSymmetric())
#print(s910.StructureConstants())
print("n=11,#=3-----------------")
print(s113.IsSymmetric())
#print(s113.StructureConstants())
print("n=12,#=2-----------------")
print(s122.IsSymmetric())
#print(s66.StructureConstants())
print("n=12,#=54----------------")
print(s1254.IsSymmetric())
#print(s1254.StructureConstants())
myScheme = drg.ASParameters(113.StructureConstants())
print("done with scheme")
print(myScheme)
print(s113.StructureConstants())
"""

"""
example
[
[1 0 0 0]  [0 1 0 0]  [0 0 1 0]  [0 0 0 1]
[0 0 1 0]  [1 0 0 0]  [0 1 0 0]  [0 0 0 1]
[0 1 0 0]  [0 0 1 0]  [1 0 0 0]  [0 0 0 1]
[0 0 0 3], [0 0 0 3], [0 0 0 3], [1 1 1 0]
]


"""