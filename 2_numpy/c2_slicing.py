

#Slicing the the array

import numpy as np;


np1 = np.array([1,2,3,4,5,6,7,8,9]);
print(np1[2:6]);

#it dost include the last item

#to returen something to the end 
print(np1[6:])

#to return something from the start
print(np1[:5]);


##steps 
print(np1[0:np1.size:2]);
#or 
print(np1[::2]);
#to return something in reverse order
print(np1[::-1]); 



