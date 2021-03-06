import random
import time
import math
import matplotlib.pyplot as plt

# Code for Ben Michael, Paul-Hugo Dlugy-Hegwer, and Jason Degrace ##
# Code for Part II Simulated Annealing for Subset Sum ##############
# If running code, set iterations are currently set at 100 per number#
# If left at this, this code will take a long while to run##########
# The iterations are controlled by "x" in the main ################


def generate_random_problem(n):
    '''
    Creates a list filled with "n" random numbers
    between -10*n and 10*n.
    :param n: The size of the generated list.
    :return: A list.
    '''
    extent = 30
    problem = []
    for i in range(n):
        num = random.randint(-extent * n, extent * n)
        while num == 0:
            num = random.randint(-extent * n, extent * n)
        problem.append(num)
    return problem


def guaranteeASolution(problem):
    '''
    Modify a list of numbers so that there exist at least
    one subset of that list whose sum is zero.
    :param problem: A list of numbers.
    :return: No return.  (A side effect is that problem is modified.)
    '''

    # remove one by random
    indexToRemove = random.randint(0, len(problem) - 1)
    value = problem.pop(indexToRemove)
    # print("Removed", value)

    # pick a random number between 1 and (n-1)\
    howManyToSum = random.randint(1, len(problem))
    # grabl that many numbers by random
    indicesUsed = {}
    solution = []
    for i in range(howManyToSum):
        # pick a random one
        ran = random.randint(0, len(problem) - 1)
        while ran in indicesUsed:
            ran = random.randint(0, len(problem) - 1)
        indicesUsed[ran] = ran
        solution.append(problem[ran])

    # sum them
    theSum = sum(solution)

    # add -sum to the list
    problem.append(-theSum)
    random.shuffle(problem)


def is_a_solution(solution):
    '''
    Returns True if the sum of the list is 0.  False, otherwise.
    :param solution: A list of numbers.
    :return: True or False.
    '''
    return sum(solution) == 0


def all_subsetsButEmpty(problem):
    '''
    Generate all of the subsets of a list (but exclude the empty
    list). This method generates the power set of a list (minus the empty set).
    :param problem: A list (or multiset).
    :return: The powerset of problem (minus the empty set).
    '''
    if len(problem) == 0:
        return []
    elif len(problem) == 1:
        return [problem]
    s2 = all_subsetsButEmpty(problem[1:])
    fullSuperSet = []
    for s in s2:
        sCopy = s[:]
        sCopy.append(problem[0])
        fullSuperSet.append(sCopy)
    fullSuperSet = fullSuperSet + s2
    return fullSuperSet


def mapVectorToSolution(vector, problem):
    '''
    Converts a "binary" representation of a subset to an actual subset built from problem.
    For instance, if problem = [a, b, c, d], and vector = [True, False, False, True], then
    this method will return the list [a, d].
    :param vector: The binary representation using a list of True/False values.
    :param problem: The original list.
    :return: A subset of the list.
    '''
    solution = []
    for index in range(len(vector)):
        if vector[index]:
            solution.append(problem[index])

    return solution


def mapIntegerToVector(number, bits):
    '''
    Converts a decimal number to binary list representation where True/False stand for 1/0.
    For instance if number is 5, and bits is 4, then the returned value will be
    [False, True, False, True]

    :param number:  The number to convert.
    :param bits: How many binary digts
    :return: A list of True/False values corresponding to 1/0 binary bits.
    '''

    inBinary = format(number, '0' + str(bits) + "b")
    vector = []
    for bit in inBinary:
        if bit == '0':
            vector.append(False)
        else:
            vector.append(True)

    return vector


def gen_solution(problem):
    '''
    Generates a random subset of problem.
    :param problem: A list (or multiset).
    :return: A subset of problem.
    '''
    solution = []
    howMany = random.randint(2, len(problem))
    indicesUsed = {}
    for i in range(howMany):
        # pick a random one
        ran = random.randint(0, len(problem) - 1)
        while ran in indicesUsed:
            ran = random.randint(0, len(problem) - 1)
        indicesUsed[ran] = ran
        solution.append(problem[ran])
    return solution


def gen_a_true_random(problemSize):
    solution = []
    for i in range(problemSize):
        randomBit = math.floor(random.uniform(0, 2))
        if (randomBit == 1):
            solution.append(True)
        else:
            solution.append(False)
    return solution


def generateRandomSuccessor(vector):
    # either add one, subtract one, swap in/swap out one,
    # Then with some probablity do it again
    successor = vector[:]
    numOpt = math.floor(random.uniform(1, 4))
    currentTrueIndex = []
    currentFalseIndex = []
    for i in range(len(successor)):
        if (successor[i]):
            currentTrueIndex.append(i)
        else:
            currentFalseIndex.append(i)
    if (numOpt == 1):
        # intIndex = math.floor(random.uniform(0, len(currentFalseIndex)))
        # print(len(currentFalseIndex))
        if (len(currentFalseIndex) > 0):
            boolToAdd = currentFalseIndex[math.floor(random.uniform(0, len(currentFalseIndex)))]
            successor[boolToAdd] = True
    elif (numOpt == 2):
        if (len(currentTrueIndex) > 2):
            boolTosub = currentTrueIndex[math.floor(random.uniform(0, len(currentTrueIndex)))]
            successor[boolTosub] = False
    elif (numOpt == 3):
        if (len(currentTrueIndex) != 0 and len(currentFalseIndex) != 0):
            boolTosub = currentTrueIndex[math.floor(random.uniform(0, len(currentTrueIndex)))]
            boolToAdd = currentFalseIndex[math.floor(random.uniform(0, len(currentFalseIndex)))]
            successor[boolTosub] = False
            successor[boolToAdd] = True
    # print(successor)

    return successor



def Simulated_Annealing_Linear(probability, best_sublist, proposed_sublist):

    #### Method to say whether a bad neighbor should be accepted or not. Takes a probability out of one, converts
    #### it to a percentage of the time the bad neighbor should be accepted and then return a 0 or 1. 0 means do not
    #### accept the bad neighbor, one means accept the bad neighbor
    P = probability
    P = str(P)
    neighbor_to_use = best_sublist
    #print(P)
    temp_list = []
    for i in P:
        temp_list.append(i)
    temp_list.pop(0)
    temp_list.pop(0)
    #print(temp_list)
    string_P = ""
    exponential_modifier = 0
    swap = 0
    for i in temp_list:
        string_P += i
        exponential_modifier += 1
    #print(string_P)
    Upper_Bound = 1 * (10 ** exponential_modifier)
    #print(Upper_Bound)
    dice_roll = random.randint(0, Upper_Bound)
    #print(dice_roll)
    if dice_roll <= int(string_P):
        swap = 1
    #print(swap)
    ######################################################################################
    ####### best sublist is the "good neighbor". proposed_sublist is the "bad neighbor"
    if swap == 0:
        changed = False
        neighbor_to_use = best_sublist
    if swap == 1:
        changed = True
        neighbor_to_use = proposed_sublist

    return neighbor_to_use, changed





def VarientTemperatureCalculation(listlength, Temperature):
    n = listlength
    if Temperature < 1:
        Temperature = 0
    if n < 25:
        Temperature = int(Temperature * (.98))
    elif n >= 25 and n < 50:
        Temperature = Temperature - 5
    elif n >= 50 and n < 100:
        Temperature = Temperature - (listlength * .1)
    elif n >= 100:
        Temperature = (Temperature * .999)

    return Temperature

def ExponentialRoot(Temperature):
    Temperature = Temperature - (Temperature ** (1/4))
    if Temperature < 0.1:
        Temperature = 0
    return Temperature

def LinearandProbability(Temperature, P, x):
    Temperature = Temperature * P
    return Temperature

def MultiplicativeTemperature(Temperature, multiplicative):
    Temperature = Temperature * multiplicative
    if Temperature < 0.1:
        Temperature = 0
    return Temperature

def ExponentialTemperature(Temperature, listlength, exponent):
    Temperature = Temperature - (Temperature * (1/(listlength ** int(exponent))))
    return Temperature

def LinearTemperatureCalculation(Temperature, x):
    Temperature = Temperature - x
    return Temperature

def LogrithmicTemperatureCalculation(Temperature, listlength, P, timestep):
    log_val_length = math.log(listlength, 10)
    log_val_temp = math.log(Temperature, 10)
    Temperature2 = listlength * (log_val_temp// log_val_length)
    # if round(Temperature) == round(Temperature2):
    #     listlength = listlength * (.50)
    #     Temperature2 = (listlength) * (math.log(Temperature, 10))
    return Temperature2

def ProbablilityCalculation(Temperature, delta, listlength, CoolingMethod):
    P = math.e ** ((-(delta)) / Temperature)
    P = round(P, 5)
    if CoolingMethod == "Linear":
        Temperature = LinearTemperatureCalculation(Temperature, 1)
    if CoolingMethod == "ExponentialRoot":
        Temperature = ExponentialRoot(Temperature)
    if CoolingMethod == "Multiplicative":
        Temperature = MultiplicativeTemperature(Temperature, 0.999)
    if CoolingMethod == "Size_Dependent":
        Temperature = VarientTemperatureCalculation(listlength, Temperature)

    #Temperature = VarientTemperatureCalculation(listlength, Temperature)
    #Temperature = LogrithmicTemperatureCalculation(Temperature, listlength, P, timestep)
    #Temperature = LinearandProbability(Temperature, P, 1)
    #Temperature = ExponentialRoot(Temperature)
    #Temperature = MultiplicativeTemperature(Temperature, 0.99)

    return P, Temperature


'''
Generate some problems, find some solutions.
Time it!
'''
# print("n\tBruteForce\tHillClimb_W_Restart")
# print("n\tGuesses")
#print("n\tBest Solution Sum")


def main():

    ####Lists for the Graphs###########
    LinearTimeList = []
    ExponentialTimeList = []
    MultiplicativeTimeList = []
    LengthDependentTimeList = []


    LinearGuessList = []
    ExponentialGuessList = []
    MultiplicativeGuessList = []
    LengthDependentGuessList = []

    FailList = []
    #####################################
    length_list = [15, 35, 55, 75, 95, 115, 135]
    method_list = ["Linear", "Multiplicative", "ExponentialRoot", "Size_Dependent"]
    for type in method_list:
        type = type
        print("Changing Types: ", type)
        average_list = []
        length_list = [15, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]
        length_list_short = [35]
        # n = 0
        # for x in length_list:
        #     timevalues = []
        #for n in length_list_short:
        for n in length_list:
            print("new list length: ", n)
            timevalues = []
            successfull_finds = 0
            guess = 0
            if n < 50:
                Temperature = 2000 * n
            else:
                Temperature = 1000 * n
            #print("Temperature: ", Temperature)
            x = 100
            #for x in range(a):
            while x > 0:
                skip = False
                startTime = time.process_time()
                #Temperature = abs(300 * (n - 200))
                if n < 50:
                    Temperature = 3000 * n
                else:
                    Temperature = 1000 * n
                problem_list = generate_random_problem(n)
                guaranteeASolution(problem_list)
                solution_problem_list = problem_list #the problem list with a zero solution possible
                #print(solution_problem_list)
                randomsolution = gen_solution(solution_problem_list) # random subset of the problem list
                hold_solution = randomsolution
                BestScore = sum(randomsolution) # Initial sum of the random sublist

                #Check a Neighbor of a problem list using generate random successor#
                #Change out values if that neighbor is better################
                while Temperature > 0:
                    index = random.randint(0, (len(solution_problem_list) - 1)) #the index to be converted to a vector
                    number = solution_problem_list[index]
                    index_vector = mapIntegerToVector(number, len(solution_problem_list))
                    ran_sol_vector = generateRandomSuccessor(index_vector)
                    proposed_solution = mapVectorToSolution(ran_sol_vector, solution_problem_list)
                    #print("The new neighbor: ", proposed_solution)
                    temp_sum = sum(proposed_solution)
                    #print("The Sum of that neighbor: ", temp_sum)
                    if temp_sum == 0:
                        print()
                        print("Listsize: ", n)
                        print("Type: ", type)
                        print("x: ", x)
                        print("Temperature: ", Temperature)
                        print("Found solution: ", proposed_solution)
                        print("Sum of that sublist: ", sum(proposed_solution))
                        successfull_finds = successfull_finds + 1
                        # print("Successful_finds: ", successfull_finds)
                        # print()
                        randomsolution = proposed_solution
                        BestScore = sum(randomsolution)
                        break
                    elif abs(temp_sum) < abs(BestScore):
                        #print("Changed value, new sum: ", temp_sum)
                        BestScore = temp_sum
                        #print("The Better Neighbor: ", proposed_solution)
                        randomsolution = proposed_solution
                    elif abs(temp_sum) > abs(BestScore):
                        difference = abs(abs(temp_sum) - abs(BestScore))
                        #print("Temperature Before: ", Temperature)
                        prob_vals = ProbablilityCalculation(Temperature, difference, n, type)
                        probability = prob_vals[0]
                        #print("The probability: ", probability)
                        #print(type)
                        Temperature = prob_vals[1]
                        #print(Temperature)
                        simulated_solution = Simulated_Annealing_Linear(probability, randomsolution, proposed_solution)
                        guess = guess + 1
                        randomsolution = simulated_solution[0]
                        changed = simulated_solution[1]
                        if changed == True:
                            #print("Random Solution After simulatedA: ", randomsolution)
                            BestScore = sum(randomsolution)

                #print("Temperature: ", Temperature, "Sum: ", temp_sum)
                if Temperature == 0:
                    #print()
                    skip = True
                    #print("Temperature zeroed out without finding solution")
                    FailList.append([type, n, x])
                if skip == True:
                    x = x + 1
                    endTime = time.process_time()
                else:
                    endTime = time.process_time()
                    timevalue = (format(endTime - startTime, "6.4f"))
                    #print(timevalue)
                    timevalues.append(float(timevalue))
                x = x - 1

            average_time = sum(timevalues)/100
            average_guess = guess//100

            if type == "Linear":
                LinearTimeList.append(average_time)
                LinearGuessList.append(average_guess)
            if type == "Multiplicative":
                MultiplicativeTimeList.append(average_time)
                MultiplicativeGuessList.append(average_guess)
            if type == "ExponentialRoot":
                ExponentialTimeList.append(average_time)
                ExponentialGuessList.append(average_guess)
            if type == "Size_Dependent":
                LengthDependentTimeList.append(average_time)
                LengthDependentGuessList.append(average_guess)

            average_list.append(float(average_time))
    print()
    print()
    print("Linear Time: ", LengthDependentTimeList)
    print("Linear Guess: ", LengthDependentGuessList)
    print("Multiplicative Time: ", MultiplicativeTimeList)
    print("Multiplicative Guess: ", MultiplicativeGuessList)
    print("ExponentialRoot Time: ", ExponentialTimeList)
    print("ExponentialRoot Guess: ", ExponentialGuessList)
    print("Length Dependent Time: ", LengthDependentTimeList)
    print("Length Dependent Guess: ", LengthDependentGuessList)
    print("Zeroes List: ", FailList)
    print("Average List: ", average_list)

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

    plt.plot(length_list, MultiplicativeTimeList, label="Multiplicative Time")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('TIME(seconds)')
    plt.title('Multiplicative Cooling Time')
    plt.show()

    plt.plot(length_list, MultiplicativeGuessList, label="Multiplicative Guesses")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('Guesses')
    plt.title('Multiplicative Guesses')
    plt.show()

    plt.plot(length_list, ExponentialTimeList, label="Exponential Time")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('TIME(seconds)')
    plt.title('Exponential Cooling Time')
    plt.show()

    plt.plot(length_list, ExponentialGuessList, label="Exponential Guesses")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('Guesses')
    plt.title('Exponential Guesses')
    plt.show()

    plt.plot(length_list, LengthDependentTimeList, label="Length Dependent Time")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('TIME(seconds)')
    plt.title('Length Dependent Cooling Time')
    plt.show()

    plt.plot(length_list, LengthDependentGuessList, label="Length Dependent Guesses")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('Guesses')
    plt.title('Length Dependent Guesses')
    plt.show()



if __name__ == "__main__":
    main()

