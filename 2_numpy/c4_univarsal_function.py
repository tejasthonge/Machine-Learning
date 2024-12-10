#Univrsel Funtions

import numpy as np;
np1 = np.array([-3,-4,-1,10, 2, 3, 4, 5]);

#1 find the squreroot of each item
print(np.square(np1))
#[100   4   9  16  25]


#2 absolute
print(np.absolute(np1)) # it covert the -ve to absolute 
#[ 3  4  1 10  2  3  4  5]

#3 exponents 

print(np.exp(np1))
'''[4.97870684e-02 1.83156389e-02 3.67879441e-01 2.20264658e+047.38905610e+00 2.00855369e+01 5.45981500e+01 1.48413159e+02]'''


#4min / max
print(np.min(np1))
print(np.max(np1))
'''
-4
10
'''

#5 to find the sign of each item
print(np.sign(np1))
'''
[-1 -1 -1  1  1  1  1  1]
-1 ->for the -ve values
 1 -> for the +ve values
'''




#7 to find the log 
print(np.log(np1))
'''
[       nan        nan        nan 2.30258509 0.69314718 1.09861229 1.38629436 1.60943791]
'''