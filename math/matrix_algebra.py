# Matrix Algebra

import numpy as npy

#matrix definitions
A = npy.matrix([[1, 2, 3], [2, 7, 4]])
B = npy.matrix([[1, -1], [0, 1]])
C = npy.matrix([[5, -1], [9, 1], [6, 0]])
D = npy.matrix([[3, -2, -1], [1, 2, 3]])

#vector definitions
u = npy.array([6, 2, -3, 5])
v = npy.array([3, 5, -1, 4])
w = npy.array([[1], [8], [0], [5]])

# dimensions
print ' 1.1) dimensions of A:',npy.shape(A)
print ' 1.2) dimensions of B:',npy.shape(B)
print ' 1.3) dimensions of C:',npy.shape(C)
print ' 1.4) dimensions of D:',npy.shape(D)
print ' 1.5) dimensions of u:',npy.shape(u)
print ' 1.6) dimensions of v:',npy.shape(v)

# vector operations
print ' 2.1) vector u + vector v', u + v
print ' 2.2) vector u - vector v', u - v
print ' 2.3) alpha times vector u', 6 * u
print ' 2.4) vector u . vector v - dot product', npy.dot(u,v)
print ' 2.5) norm of vector u', npy.linalg.norm(u)

# Matrix Operations
print ' 3.1) A + C: this will give an error as dimensions are different'

print ' 3.2) A - transpose of C:'
print A - C.transpose()

print ' 3.3) transpose of C + 3 times D:'
print C.transpose() + 3*D

print ' 3.4) B + A : this will give an error as dimensions are different'

print ' 3.5) B + A: this will give an error as dimensions are different'


print ' 3.6) B + C: this will give an error as dimensions are different'

print ' 3.7) CB:'
print C*B

print ' 3.8) B to the power of 4:'
print B**4

print ' 3.9) A times transpose of A:'
print A * A.transpose()


print ' 3.10) transpose of D times D :'
print D.transpose() * D

print 'All answers on scratchpad match with python.'