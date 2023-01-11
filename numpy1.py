import numpy
# print(help(numpy.genfromtxt))
import numpy as np
from numpy import pi

vector = numpy.array([1, 2, 3, 4, 5, 6])
matrix = numpy.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
print(matrix.shape)
vector = numpy.array(['1','2','3'])
print(vector.dtype)
vector = vector.astype(float)
print(vector.min())

print(matrix.sum(axis=0))
print(matrix.sum(axis=1))

a = np.arange(15).reshape(3,5)
print(a.ndim)

#a.size
#a.dtype.name


np.ones((2,3,4))
np.zeros((3,4),dtype = np.int32)
A = np.random.random((2,3)) #[-1,1]

np.linspace(0,2*pi,100)

B = np.ones((3,4))
print(a**2)
print(A.dot(B))
print(np.dot(A,B))

C = np.zeros((3,3),dtype=np.int32)
print(C)
print(np.hsplit(A,3))
print(np.vstack((A,C)))

print(A.ravel())
print(A.T)

np.floor(A)

np.exp(A)
np.sqrt(A)

D = A.copy()

index = A.argmax(axis = 0)
data_max = A[index,range(A.shape[1])]
print(data_max)

E = np.tile(A,(2,3))

A = np.random.random((2,3)) #[-1,1]
A.sort(axis = 1)
print(A)

B = np.array([4,5,3,8])
J = np.argsort(B)
print(B[J])


