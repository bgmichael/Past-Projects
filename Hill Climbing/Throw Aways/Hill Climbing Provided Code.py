import random
import time





def generate_random_problem(n):
    '''
    Creates a list filled with "n" random numbers
    between -10*n and 10*n.
    :param n: The size of the generated list.
    :return: A list.
    '''
    extent = 1000
    problem = []
    for i in range(n):
        num = random.randint(-extent*n, extent*n)
        while num == 0:
            num = random.randint(-extent*n, extent*n)
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
    #print("Removed", value)

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
        return [  ]
    elif len(problem) == 1:
        return [problem]
    s2 = all_subsetsButEmpty(problem[1:])
    fullSuperSet = []
    for s in s2:
        sCopy  = s[:]
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

def generateRandomSuccessor(vector):

    # either add one, subtract one, swap in/swap out one,
    # Then with some probablity do it again

    successor = vector[:]

    #left blank for your enjoyment


    return successor


'''
Generate some problems, find some solutions.
Time it!
'''
# for n in range(3, 20):
#     problem1 = generate_random_problem(n)
#     guaranteeASolution(problem1)
#
#     # brute force
#     start = time.perf_counter()
#     foundSolution = False
#     for vectorNumber in range(1, 2**n): # all possible subsets
#         vector = mapIntegerToVector(vectorNumber, n)
#         possibleSolution = mapVectorToSolution(vector, problem1)
#         if is_a_solution(possibleSolution):
#             #print("YES", possibleSolution)
#             foundSolution = True
#             break
#         # else:
#         #     print("NO")
#
#     if not foundSolution:
#         print("There is no solution.")
#     end = time.perf_counter()

    # hill climbing
# for n in range(3, 20):
#     startHill = time.perf_counter()
#     foundSolution = False
#     noImprovementPossible = False
#     theSolution = None
#     randomSolution = mapIntegerToVector(random.randint(2, n), n) #[F, F, T, T]
#     #print("Random Solution: ", randomSolution)
#
#     while not foundSolution and not noImprovementPossible:
#         problem1 = generate_random_problem(n)
#         currentScore = abs(sum(mapVectorToSolution(randomSolution, problem1)))
#         if currentScore == 0:
#             foundSolution = True
#             theSolution = randomSolution
#             bestSuccessor = theSolution
#             bestScore = 0
#             print("Found better with score: ", 0)
#         else:
#             # pick the best of x neighbors
#             howManyNeighbors = 100  # how many neighbors do you want to try?
#             bestSuccessor = None
#             bestScore = currentScore
#             for _ in range(howManyNeighbors): # this picks the best neighbor
#                 successor = generateRandomSuccessor(randomSolution)
#                 successorScore = sum(mapVectorToSolution(successor, problem1))
#                 if successorScore == 0:
#                     print("Found better with score: ", 0)
#                     foundSolution = True
#                     theSolution = successor
#                     noImprovementPossible = False
#                     bestSuccessor = theSolution
#                     bestScore = 0
#                     break
#                 elif abs(successorScore) < bestScore:
#                     bestSuccessor = successor
#                     bestScore = abs(successorScore)
#             if bestSuccessor == None:
#                 noImprovementPossible = True
#             else:
#                 print("Found better with score: ", bestScore)
#                 randomSolution = bestSuccessor
#     #
#     if noImprovementPossible:
#        print("NO IMPROVEMENT")
#
#     endHill = time.perf_counter()
#
#     print(n, "\t", end - start, '\t', endHill - startHill)





def main():

    # test4 = [7, 6, -13, 12, 7, 9, 15, 17, 82, -100, 19, 23, -19]
    # test4_sublist = [-13, 7, 15, 9]
    # print("the original list: ", test4)
    # print("the original sublist:, ", test4_sublist)
    # print("the original sum: ", sum(test4_sublist))

    for n in range(3, 20):
        problem1 = generate_random_problem(n)
        guaranteeASolution(problem1)

        for n in range(3, 20):
            startHill = time.perf_counter()
            foundSolution = False
            noImprovementPossible = False
            theSolution = None
            randomSolution = mapIntegerToVector(random.randint(2, n), n) #[F, F, T, T]
            #print("Random Solution: ", randomSolution)

            while not foundSolution and not noImprovementPossible:
                currentScore = abs(sum(mapVectorToSolution(randomSolution, problem1)))
                if currentScore == 0:
                    foundSolution = True
                    theSolution = randomSolution
                    bestSuccessor = theSolution
                    bestScore = 0
                    print("Found better with score: ", 0)
                else:
                    # pick the best of x neighbors
                    howManyNeighbors = 100  # how many neighbors do you want to try?
                    bestSuccessor = None
                    bestScore = currentScore
                    for _ in range(howManyNeighbors): # this picks the best neighbor
                        successor = generateRandomSuccessor(randomSolution)
                        successorScore = sum(mapVectorToSolution(successor, problem1))
                        if successorScore == 0:
                            print("Found better with score: ", 0)
                            foundSolution = True
                            theSolution = successor
                            noImprovementPossible = False
                            bestSuccessor = theSolution
                            bestScore = 0
                            break
                        elif abs(successorScore) < bestScore:
                            bestSuccessor = successor
                            bestScore = abs(successorScore)
                    if bestSuccessor == None:
                        noImprovementPossible = True
                    else:
                        print("Found better with score: ", bestScore)
                        randomSolution = bestSuccessor
            #
            if noImprovementPossible:
               print("NO IMPROVEMENT")

            endHill = time.perf_counter()

            print(n, "\t", end - start, '\t', endHill - startHill)




    #
    # x = mapIntegerToVector(3, 4)
    # list1 = [-150, -172, -150, 300]
    # print(mapVectorToSolution(x, list1))
    #

if __name__ == "__main__":
    main()


# for n in range(3, 8):
#     print(n, mapIntegerToVector(n, 8))