import random
import time
import math


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



def ProbablilityCalculation(Temperature, delta, listlength):
    P = math.e ** ((-(delta)) / Temperature)
    P = round(P, 5)
    Temperature = TemperatureCalculation(listlength, Temperature)

    return P, Temperature

def TemperatureCalculation(listlength, Temperature):
    n = listlength
    if Temperature < 1:
        Temperature = 0
    if n < 25:
        Temperature = int(Temperature * (.95))
    elif n >= 25 and n < 50:
        Temperature = Temperature - 5
    elif n >= 50 and n < 100:
        Temperature = Temperature - 1
    elif n >= 100:
        Temperature = (Temperature * .999)

    return Temperature



'''
Generate some problems, find some solutions.
Time it!
'''
# print("n\tBruteForce\tHillClimb_W_Restart")
# print("n\tGuesses")
#print("n\tBest Solution Sum")


def main():
    timevalues = []
    average_list = []
    length_list = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]
    length_list_short = [15, 25]
    # n = 0
    # for x in length_list:
    #     timevalues = []
    for n in length_list_short:
        print("new list length: ", n)
        timevalues = []
        Temperature = abs(300 * (n - 200))
        print("Temperature: ", Temperature)
        for x in range(10):
            #n = 300
            startTime = time.process_time()
            Temperature = abs(300 * (n - 200))
            problem_list = generate_random_problem(n)
            #print(problem_list)
            guaranteeASolution(problem_list)
            solution_problem_list = problem_list #the problem list with a zero solution possible
            randomsolution = gen_solution(solution_problem_list) # random subset of the problem list
            hold_solution = randomsolution
            BestScore = sum(randomsolution) # Initial sum of the random sublist

            #Check a Neighbor of a problem list using generate random successor#
            #Change out values if that neighbor is better################
            while Temperature > 0:
            #for i in range(1000):
                index = random.randint(0, (len(solution_problem_list) - 1)) #the index to be converted to a vector
                number = solution_problem_list[index]
                index_vector = mapIntegerToVector(number, len(solution_problem_list))
                ran_sol_vector = generateRandomSuccessor(index_vector)
                proposed_solution = mapVectorToSolution(ran_sol_vector, solution_problem_list)
                #print("The new neighbor: ", proposed_solution)
                temp_sum = sum(proposed_solution)
                #print("The Sum of that neighbor: ", temp_sum)
                if temp_sum == 0:
                    print("Found solution: ", proposed_solution)
                    print("Sum of that sublist: ", sum(proposed_solution))
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
                    prob_vals = ProbablilityCalculation(Temperature, difference, n)
                    probability = prob_vals[0]
                    Temperature = prob_vals[1]
                    #print("Temperature After: ", Temperature)
                    # print("Random Solution before simulatedA ", randomsolution)
                    # print("Bestscore: ", BestScore)
                    # print("Proposed bad neighbor: ", proposed_solution)
                    # print("Bad neighbor sum: ", sum(proposed_solution))
                    #print(Temperature, probability)
                    simulated_solution = Simulated_Annealing_Linear(probability, randomsolution, proposed_solution)
                    randomsolution = simulated_solution[0]
                    changed = simulated_solution[1]
                    if changed == True:
                        #print("Random Solution After simulatedA: ", randomsolution)
                        BestScore = sum(randomsolution)
                    # if changed == False:
                    #     x = x - 1
                        #print("Bestscore: ", BestScore)
                    # if changed == False:
                    #     print("Simulated Annealing run, No Change")


            print("Temperature: ", Temperature, "Sum: ", temp_sum)
            endTime = time.process_time()
            timevalue = (format(endTime - startTime, "6.4f"))
            #print(n)
            #print(timevalue)
            timevalues.append(float(timevalue))

        average_time = sum(timevalues)/10
        average_list.append(float(average_time))
        print(average_list)

    # print("Initial problem list: ", problem_list)
    # print(randomsolution)
    # print(BestScore)
    #print(timevalues)
    print(average_list)
    # print("Best list: ", randomsolution)
    # print("Best Solution: ", BestScore)
    # print("Initial list: ", solution_problem_list)
    # print("Initial sublist: ", hold_solution)
    # print("Initial Sum: ", sum(hold_solution))
    # print()


if __name__ == "__main__":
    main()


    # for i in problem_list:
    #     print("The problem list: ", problem_list)
    #     print("The sum before: ", sum(problem_list))
    #     ToBinary = mapIntegerToVector(i, 10)
    #     print("The number: ", i, "The convertion: ", ToBinary)
    #     ran_successor = generateRandomSuccessor(ToBinary)
    #     print("Random Successor from vector: ", ran_successor)
    #     ran_solution = mapVectorToSolution(ran_successor, problem_list)
    #     print("Random Solution: ", ran_solution)
    #     print("The sum after: ", sum(ran_solution))
    #     print()



    # for i in range(len(solution_problem_list)):
    #     n = len(solution_problem_list)
    #     print(solution_problem_list)
    #     print("The initial subset: ", randomsolution)
    #     print("The sum of random initial subset: ", BestScore)
    #     index = random.randint(0, (len(solution_problem_list) - 1))
    #     print("The initial number: ", solution_problem_list[index])
    #     vector = mapIntegerToVector(solution_problem_list[index], n)
    #     print("Vector from int: ", vector)
    #     new_vector = generateRandomSuccessor(vector)
    #     print("Vector after randomsuccessor: ", new_vector)
    #     mapped_solution = mapVectorToSolution(new_vector, solution_problem_list)
    #     print("After VectortoSolution: ", mapped_solution)
    #     new_value = sum(mapped_solution)
    #     print("The sum of the mapped solution: ", new_value)
    #     print()