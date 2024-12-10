



import numpy as np; # type: ignore

print(type(np));


scalarVector = np.array([1, 5, 3, 4, 5]);
print(scalarVector.ndim);


matrixT = np.array([[1, 2, 3],[3,2,3]]);
print(matrixT.ndim);


tensor3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],]);
print(tensor3D.ndim);

tensor3D1 = np.array([[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]],[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]]);
print(tensor3D1.ndim);
print(scalarVector.sort);
print(scalarVector);


'''
op:
<class 'module'>
1
2
3
4
'''

#means the output is depending opon the depth of an array
 
