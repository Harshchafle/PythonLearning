import numpy as np
import sys


#this makes arrays
arr1d = np.array([1, 2, 3, 4],np.int16);
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
#print(arr1d);
#print(arr2d);
#print(arr1d.shape);
#print(arr1d.dtype);
#print(arr1d.size);    

#this makes array of zeroes 2 rows and 3 columns
zeroes = np.zeros((2,5), dtype=np.int16);
#print("zeroes = ",zeroes);
#print("dtype :",zeroes.dtype);
#print("size :",zeroes.size);
#print("shape :",zeroes.shape);

# arange function
rng = np.arange(12)
#print("rng = ",rng);

#linspace function
linsp = np.linspace(1,10,5)
#print("linsp = ",linsp);

#identity function
iden = np.identity(4)
#print("iden = ",iden);

#reshape function
reshaped = rng.reshape(3,4)
#print("reshaped = ",reshaped);
reshaped = reshaped.reshape(2,6)
#print("reshaped = ",reshaped)
reshaped.ravel();
#print("reshaped : ",reshaped);

#Axis0 and Axis1 
x = [[1,2,3],[4,5,6],[7,8,9]];
#print("x : ",x);
arr = np.array(x);
#print("sum along axis 0 : ",np.sum(arr, axis=0));
#print("sum along axis 1 : ",np.sum(arr, axis=1));

#Broadcasting
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
#print("c : ",c);

#stacking
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.stack((a,b), axis=0)
#print("c : ",c);
d = np.stack((a,b), axis=1)

#transpose
a = np.array([[1,2,3],[4,5,6]])
b = a.T   # or we can use np.transpose(a) instead
#print("a : ", a)
#print("b : ", b)

#for in loop
#for item in a:
    #print(item)

# iterator using flat
#for item in a.flat:
    #print(item)

# to print dimensions
#print("a.ndim : ", a.ndim)
#print("a.shape : ", a.shape)
#print("a.size : ", a.size)
#print("a.dtype : ", a.dtype)
#print("a.itemsize : ", a.itemsize)
#print("a.nbytes : ", a.nbytes)

# to find max and min elem indexes
#print("a.argmax() : ", a.argmax())
#print("a.argmin() : ", a.argmin())

# to get indices after sorting array
a = np.array([3, 1, 2, 4, 5])
#print("a.argsort() : ", a.argsort())

# to sort array
a.sort()
#print("a.sort() : ", a)

#to get max elem index in row
#print("a.argmax(axis=1) : ", a.argmax(axis=1))

#to get max elem index in column
#print("a.argmax(axis=0) : ", a.argmax(axis=0))

# to perform basic operation on matrix
ar1 = np.array([[0,1,2],[3,4,5],[6,7,8]])
ar2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

#print("ar1: ", ar1)
#print("ar2: ", ar2)
#
#print("np.add(ar1+ar2) : ", np.add(ar1, ar2))
#print("ar1+ar2: ", ar1+ar2)
#
#print("np.subtract(ar1,ar2) : ", np.subtract(ar1, ar2))
#print("ar1-ar2: ", ar1-ar2)
#
#print("np.multiply(ar1,ar2) : ", np.multiply(ar1, ar2))
#print("ar1 * ar2 : ", ar1*ar2)
#
#print("np.divide(ar1,ar2) : ", np.divide(ar1, ar2))
#print("ar1 / ar2 : ", ar1/ar2)

#print("np.sqrt(ar1) : ", np.sqrt(ar1))

# to find elems
print((np.where(ar1==4)))  # its a type of tuple

py_ar = [0,3,6,9]
np_ar = np.array(py_ar)
print(sys.getsizeof(1) * len(py_ar))
print(np_ar.itemsize * np_ar.size) 