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
    extent = 100000
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
    numOpt = math.floor(random.uniform(1, 4));
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


'''
Generate some problems, find some solutions.
Time it!
'''
# print("n\tBruteForce\tHillClimb_W_Restart")
# print("n\tGuesses")
print("n\tBest Solution Sum")


def main(n):
    problem1 = generate_random_problem(n)
    guaranteeASolution(problem1)
    BruteForce_totalTime = 0
    HillClimb_totalTime = 0
    daCount = 0
    for i in range(10):
        # brute force
        start = time.perf_counter()
        foundSolution = False
        for vectorNumber in range(1, 2 ** n):  # all possible subsets
            vector = mapIntegerToVector(vectorNumber, n)
            possibleSolution = mapVectorToSolution(vector, problem1)
            if is_a_solution(possibleSolution):
                # print("YES", possibleSolution)
                foundSolution = True
                break
            # else:
            #     print("NO")

        if not foundSolution:
            print("There is no solution.")
        end = time.perf_counter()

        # hill climbing
        startHill = time.perf_counter()
        foundSolution = False
        noImprovementPossible = False
        theSolution = None
        # randomSolution = mapIntegerToVector(random.randint(2, n), n)
        trueCount = 0;
        while trueCount < 2:
            randomSolution = mapIntegerToVector(random.randint(2, n), n)
            trueCount = 0;
            for i in randomSolution:
                if (i): trueCount = trueCount + 1
        while not foundSolution:  # and counter < 10: #Add not noImprovementPossible
            trueCount = 0
            if noImprovementPossible:  # this can be commented out.
                while trueCount < 2:
                    randomSolution = gen_a_true_random(len(problem1))
                    trueCount = 0;
                    for i in randomSolution:
                        if (i): trueCount = trueCount + 1
                noImprovementPossible = False
                daCount += 1
            currentScore = abs(sum(mapVectorToSolution(randomSolution, problem1)))

            if currentScore == 0:
                foundSolution = True
                theSolution = randomSolution
                bestSuccessor = theSolution
                bestScore = 0
                # print("Found better with score: ", 0)
            else:
                # pick the best of x neighbors
                howManyNeighbors = 10000  # how many neighbors do you want to try?
                bestSuccessor = None
                bestScore = currentScore
                for _ in range(howManyNeighbors):  # this picks the best neighbor
                    successor = generateRandomSuccessor(randomSolution)
                    daCount += 1
                    successorScore = sum(mapVectorToSolution(successor, problem1))
                    if successorScore == 0:
                        # print("Found better with score: ", 0)
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
                    # print("NO IMPROVEMENT")
                elif not foundSolution:
                    randomSolution = bestSuccessor
        endHill = time.perf_counter()

        BruteForce_totalTime += end - start
        HillClimb_totalTime += endHill - startHill
        # print(n, "\t", end - start, '\t', endHill - startHill)
    BruteForce_totalTime /= 10
    HillClimb_totalTime /= 10
    daCount /= 10
    # print(n, "\t", BruteForce_totalTime, "\t", HillClimb_totalTime)
    print(n, "\t", daCount)


def main_no_reset(n):
    problem1 = generate_random_problem(n)
    guaranteeASolution(problem1)
    BruteForce_totalTime = 0
    HillClimb_totalTime = 0
    daCount = 0
    solutionTotal = 0
    averageGuessList = [] # list of the averages of values from guessing from each run
    answerList = [] # list of best guess for each run
    for i in range(10):
        # brute force
        start = time.perf_counter()
        foundSolution = False
        for vectorNumber in range(1, 2 ** n):  # all possible subsets
            vector = mapIntegerToVector(vectorNumber, n)
            possibleSolution = mapVectorToSolution(vector, problem1)
            if is_a_solution(possibleSolution):
                # print("YES", possibleSolution)
                foundSolution = True
                break
            # else:
            #     print("NO")

        if not foundSolution:
            print("There is no solution.")
        end = time.perf_counter()

        # hill climbing
        startHill = time.perf_counter()
        foundSolution = False
        noImprovementPossible = False
        theSolution = None
        # randomSolution = mapIntegerToVector(random.randint(2, n), n)
        trueCount = 0;
        neighborGuessCounter = 0 # how many guesses neighbor went through, normally 100
        neighborTotal = 0 # total sum of neighbor guesses
        while trueCount < 2:
            randomSolution = mapIntegerToVector(random.randint(2, n), n)
            trueCount = 0;
            for i in randomSolution:
                if (i): trueCount = trueCount + 1
        while not foundSolution:  # and counter < 10: #Add not noImprovementPossible
            trueCount = 0
            if noImprovementPossible:  # this can be commented out.
                while trueCount < 2:
                    randomSolution = gen_a_true_random(len(problem1))
                    trueCount = 0;
                    for i in randomSolution:
                        if (i): trueCount = trueCount + 1
                noImprovementPossible = False
                daCount += 1
            currentScore = abs(sum(mapVectorToSolution(randomSolution, problem1)))

            if currentScore == 0:
                foundSolution = True
                theSolution = randomSolution
                bestSuccessor = theSolution
                bestScore = 0
                # print("Found better with score: ", 0)
            else:
                # pick the best of x neighbors
                howManyNeighbors = 100  # how many neighbors do you want to try?
                bestSuccessor = None
                bestScore = currentScore
                for _ in range(howManyNeighbors):  # this picks the best neighbor
                    successor = generateRandomSuccessor(randomSolution)
                    daCount += 1
                    successorScore = sum(mapVectorToSolution(successor, problem1))
                    neighborTotal += abs(successorScore)
                    neighborGuessCounter += 1
                    if successorScore == 0:
                        # print("Found better with score: ", 0)
                        foundSolution = True
                        theSolution = successor
                        noImprovementPossible = False
                        bestSuccessor = theSolution
                        bestScore = 0
                        averageGuessList.append(neighborTotal / neighborGuessCounter)
                        break
                    elif abs(successorScore) < bestScore:
                        bestSuccessor = successor
                        bestScore = abs(successorScore)
                if bestSuccessor == None:
                    noImprovementPossible = True
                    # print("NO IMPROVEMENT")
                foundSolution = True
                averageGuessList.append(neighborTotal / neighborGuessCounter)

        answerList.append(bestScore)
        solutionTotal += bestScore

        endHill = time.perf_counter()

        BruteForce_totalTime += end - start
        HillClimb_totalTime += endHill - startHill
        # print(n, "\t", end - start, '\t', endHill - startHill)
    BruteForce_totalTime /= 10
    HillClimb_totalTime /= 10
    daCount /= 10
    solutionTotal /= 10
    # print(n, "\t", BruteForce_totalTime, "\t", HillClimb_totalTime)
    # print(n, "\t", daCount)
    print(averageGuessList)#average answer from neighbor
    print(sum(averageGuessList)/10)
    print(answerList) #best answer with no reset
    print(sum(answerList)/10)
    print(n, "\t", solutionTotal)


mylist = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in mylist:
    main_no_reset(int(i))

