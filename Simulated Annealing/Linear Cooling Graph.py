import random
import time
import math
import matplotlib.pyplot as plt




Linear_Guess = [1207, 9676, 9262, 8215, 7060, 8333, 10247, 9434, 15121, 14669, 17485, 20694, 19109, 18632]
length_list = [15, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]

plt.plot(length_list, Linear_Guess, label="Linear Guesses")
plt.legend(loc='upper right')
plt.xlabel('Input Size')
plt.ylabel('Guesses')
plt.title('Linear Cooling Guesses')
plt.show()