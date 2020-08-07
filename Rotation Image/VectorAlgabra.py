'''Benjamin Michael'''


import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns; sns.set()






#### PROBLEM 1 #####
p1_vector = np.array([1,-2], dtype=np.float)
print(np.linalg.norm(p1_vector))
print(p1_vector)
# p1_vector.reshape(p1_vector,(1,1))
# p1_vector_norm = preprocessing.normalize(p1_vector, norm='l2')
# print(p1_vector_norm)

#### PROBLEM 2 ####
p2_vectorv = np.array((1,-2))
p2_vectoru = np.array((2,1))
dot_vectors_p2 = (np.dot(p2_vectorv, p2_vectoru))
print(dot_vectors_p2)
a = np.array([[1,-2],[2,1]])
cos_vectors = ((dot_vectors_p2)/(np.linalg.det(a)))
print(cos_vectors)

###### PROBLEM 3 ######
p3_vectorv = np.array([1,-2,1,-2])
p3_vectoru = np.array([2,1,2,1])
inner = np.inner(p3_vectorv, p3_vectoru)
print(inner)
print(len(p3_vectorv))
print(len(p3_vectoru))
dot_vectors_p3 = (np.dot(p3_vectorv, p3_vectoru))
b = np.array([[1,-2,1,-2],[2,1,2,1]])
cos_vectors_p3 = ((dot_vectors_p3)/(len(p3_vectorv)*len(p3_vectoru)))
print(cos_vectors_p3)


##### PROBLEM 7 #######
p7_array = np.reshape([1,-2,0,3,2,-1], (3,2))
print("p7", p7_array)
A_prime = p7_array.T
print(A_prime)

##### PROBLEM 8 ######
p8_vectora = np.reshape([0,1,1,1,0,1,1,1,0], (3,3))
print(p8_vectora)
p8_vectorb = np.reshape([2,2,2,2,2,2], (3,2))
print(p8_vectorb)
print(np.matmul(p8_vectora, p8_vectorb))


##### PROBLEM 9 #######
A = np.reshape(np.array([1,2,3,4,5,6,7,8]),(4,2))
I = np.reshape(np.array([1,0,0,1]), (2,2))
U = np.matmul(A,I)
P = np.reshape(np.array([1,0,0,0]), (2,2))
D = np.matmul(A,P)
print(U)
print()
print(D)


