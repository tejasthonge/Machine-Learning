


import numpy as np
#funtions of numepy


#arange() function
np1 = np.arange(10);

np2=  np.arange(0,11,2);
print(np1);
print(np2);
'''[0 1 2 3 4 5 6 7 8 9]
[ 0  2  4  6  8 10]'''


#zrange() function
np5 = np.zeros(10);
print(np5);
'''[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]'''

np6 = np.zeros((7,3));  #multi-dimensional ,that thee
print(np6);
print(np6.shape)
print(np6.ndim)

'''[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
(7, 3)
2'''
#linspace() function

np3 = np.linspace(0,10,2); # divied the aray in 2 parts
print(np3);
'''[ 0. 10.]'''
np4 = np.linspace(0,10,5);# divied the aray in 5 parts
print(np4);
'''[ 0.   2.5  5.   7.5 10. ]'''


#random.randint() function
np7 = np.random.randint(0,10,10);
print(np7);
'''[2 7 6 6 5 7 7 1 8 9]'''
np8 = np.random.randint(0,10,5);
print(  np8);
'''[6 5 7 4 8]'''


#full() function

np8 = np.full(8,9);  #(number of elements ,value)
print(np8);
'''
[9 9 9 9 9 9 9 9]'''

np9 = np.full((3,4),9);  #(shape,value)-->((row,column),value)
print(np9);
'''[[9 9 9 9]
 [9 9 9 9]
 [9 9 9 9]]'''


#conveting the array (list) into the numpay array

my_list = [4,2,1,6,1,9];

my_array = np.array(my_list);
print(type(my_list));
print(type(my_array));
'''<class 'list'>
<class 'numpy.ndarray'>'''

#sort
sortedArray= np.sort(my_array)  
print(sortedArray);