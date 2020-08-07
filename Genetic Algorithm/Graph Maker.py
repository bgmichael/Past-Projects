import random
import time
import math
import matplotlib.pyplot as plt



plt.plot(length_list, LengthDependentTimeList, label="Linear Time")
plt.legend(loc='upper right')
plt.xlabel('Input Size')
plt.ylabel('TIME(seconds)')
plt.title('Linear Cooling Time')
plt.show()

plt.plot(length_list, LengthDependentGuessList, label="Linear Guesses")
plt.legend(loc='upper right')
plt.xlabel('Input Size')
plt.ylabel('Guesses')
plt.title('Linear Cooling Guesses')
plt.show()