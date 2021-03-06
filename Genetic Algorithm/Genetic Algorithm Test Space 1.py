import random
import time
import math
import matplotlib.pyplot as plt




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



##def Simulated_Annealing_Linear(probability, best_sublist, proposed_sublist):
##
##    #### Method to say whether a bad neighbor should be accepted or not. Takes a probability out of one, converts
##    #### it to a percentage of the time the bad neighbor should be accepted and then return a 0 or 1. 0 means do not
##    #### accept the bad neighbor, one means accept the bad neighbor
##    P = probability
##    P = str(P)
##    neighbor_to_use = best_sublist
##    #print(P)
##    temp_list = []
##    for i in P:
##        temp_list.append(i)
##    temp_list.pop(0)
##    temp_list.pop(0)
##    #print(temp_list)
##    string_P = ""
##    exponential_modifier = 0
##    swap = 0
##    for i in temp_list:
##        string_P += i
##        exponential_modifier += 1
##    #print(string_P)
##    Upper_Bound = 1 * (10 ** exponential_modifier)
##    #print(Upper_Bound)
##    dice_roll = random.randint(0, Upper_Bound)
##    #print(dice_roll)
##    if dice_roll <= int(string_P):
##        swap = 1
##    #print(swap)
##    ######################################################################################
##    ####### best sublist is the "good neighbor". proposed_sublist is the "bad neighbor"
##    if swap == 0:
##        changed = False
##        neighbor_to_use = best_sublist
##    if swap == 1:
##        changed = True
##        neighbor_to_use = proposed_sublist
##
##    return neighbor_to_use, changed




def Genetic_Algorithm(n):

    #START
    #Generate the population
    #Compute Fitness
    #REPEAT
        #Selectin
        #Crossover
        #Mutation
        #Compute Fitness
    #UNTIL population has converged
    #STOP
    '''
    This is the overall function which the other function below will feed into ultimantly
    :param n: Size of the Overall List
    :return: The solution sublist
    '''
    test_population = Produce_Initial_Population(100, n)
    # print("test_population: ", test_population)
    #food_chain(test_population, n)
    # print("test_population post sort: ", test_population)
    #test_population = survival_o_the_fittest(test_population)
    #test_selection = Selection(test_population, .50)
    #print("test_selection: ", test_selection)
    solutionNotFound = True

    # for j in range(len(test_population)//4):
    best_fitness = 1000000
    best_fit = 0
    parent_population = []
    iterator = 0
    refresh = 0
    while best_fitness != 0:
        if iterator > 1000:
            ####### a random restart of sorts############
            parent_population = []
            refresh = refresh + 1
        while solutionNotFound == True:
            next_gen = []
            while len(parent_population) < 100:
                parentA, parentB = simpleSelection(test_population)
                parent_population.append(parentA)
                parent_population.append(parentB)
                # print("parentA: ", parentA, sum(parentA))
                # print("parentB: ", parentB, sum(parentB))
            while len(next_gen) < 100:
                parentA = parent_population[random.randint(0, len(parent_population) - 1)]
                parentB = parent_population[random.randint(0, len(parent_population) - 1)]
                childA,childB = simple_reproduction(parentA,parentB)
                next_gen.append(childA)
                next_gen.append(childB)

                # test_population.append(childA)
                # test_population.append(childB)
                #print("The entire breeding population: ", test_population)


            #this part iterates through the new generation and check for a zero and also selects the best encountered sublist

            for i in range(1, (len(next_gen)//4)):
                index = random.randint(1, len(next_gen) - 1)
                compare_child = next_gen[index]
                child_to_mutate = compare_child.copy()
                mutated_child = Individual_Mutation(child_to_mutate, n)
                if abs(sum(mutated_child)) < abs(sum(compare_child)):
                    next_gen[index] = mutated_child
                    # print("unmutated child value: ", abs(sum(compare_child)))
                    # print("mutated child value: ", abs(sum(mutated_child)))





            best_fitness = 1000000
            best_fit = 0
            for i in next_gen:
                if abs(sum(i)) == 0:
                    solutionNotFound = False
                    best_fitness = abs(sum(i))
                    best_fit = i
                    print("The initial problem set: ", n)
                    print("The Solution set is: ", best_fit)
                    print("The Solution score is: ", best_fitness)
                    print("The number of generations: ", iterator)
                    print()

                    break
                if abs(sum(i)) < best_fitness:
                    best_fitness = abs(sum(i))
                    best_fit = i


            #print("Most fit Timmy out of the 100 parents: ", best_fitness, best_fit)
            if best_fitness == 0:
                solutionNotFound = False
            else:
                parent_population = next_gen
                iterator = iterator + 1
                # print("This generations best individual: ", best_fit)
                # print("This generations best Score: ", best_fitness)
                # print("The cound: ", iterator)
                # print()

    return best_fit, best_fitness

def Produce_Initial_Population(population_size, problem_list):
    #An intial set of potential solutions#
    '''
    Produces a list of lists, each list being a Parent, which in this case means a potential solution sublist
    :param population_size: How many sublists (Parents) do we want in the initial population
    :param problem_list: The Overall list
    :return: A list of list, each list being a "Parent" to be used in reproduction
    '''
    n = population_size
    population = []
    for i in range(n):
        individual = gen_solution(problem_list)
        population.append(individual)

    return population

def simpleSelection(population):
    '''Baby simplification for selection. Literally selects two parents to bread'''
    theRand = random.randint(0, len(population)-1)
    theRandB = random.randint(0, len(population)-1)
    parentA = population[theRand]

    while theRand == theRandB:
        theRandB = random.randint(0, len(population)-1)
    parentB = population[theRandB]
    bestScoreA = abs(sum(parentA))
    bestScoreB = abs(sum(parentB))

    return parentA, parentB

def food_chain(population, n):
    population.sort(key=lambda x: abs(sum(n)))
def survival_o_the_fittest(population):
    return population[0:len(population)//4]




def Selection(population, fitness_modifier):
    #Selects the "fittest" of the solutions so tha they can pass their genes along#
    '''
    The function is meant for selecting the "fittest" individuals in a population. These individuals will then be passed
    on to create offspring.
    :param population: The current population
    :param fitness_modifier: The idea here is a decimal value that will be used as a percentage. All the members of the
    population that fit within this percentage range will be allowed to continue on to reproduce
    :return: The individuals in the population that have been deemed 'fit enough' to reproduce and create children
    '''
    ##### NOTE: CURRENTLY THIS FUNCTION DOES NOT DO AN INITIAL CHECK FOR A ZERO SUM. IT MIGHT BE A GOOD IDEA TO PUT ONE
    ##### IN THE BEGINNING SOMEWHERE########
    print("In selection")
    fitness_tracker = []
    fittest_individual_fittness = abs(sum(population[0]))
    fittest_individual_index = 0
    for i in range(len(population)):
        fitness = sum(population[i])
        fitness_tracker.insert(i, fitness)
        if abs(fitness) < abs(fittest_individual_fittness):
            fittest_individual_fittness = abs(sum(population[i]))
            fittest_individual_index = i
            fittest_individual = population[i]
    print("ft: ", fitness_tracker)
    least_fit_individual_fittness = min(fitness_tracker)
    least_fit_individual_index = fitness_tracker.index(least_fit_individual_fittness)
    least_fit_individual = population[least_fit_individual_index]

    fittness_difference = fittest_individual_fittness - least_fit_individual_fittness

    acceptable_fittness = fittness_difference * fitness_modifier
    Upper_Bound = fittest_individual_fittness + acceptable_fittness
    Lower_bound = fittest_individual_fittness - acceptable_fittness

    selected_fittness_indices = []

    for i in range(len(fitness_tracker)):
        if fitness_tracker[i] > Lower_bound and fitness_tracker[i] < Upper_Bound:
            selected_fittness_indices.append(i)
    print("sfi: ", selected_fittness_indices)
    selected_population = []

    for index in selected_fittness_indices:
        individual = population[index]
        selected_population.append(individual)
    print("vox_populi: ", selected_population)
    return selected_population

def simple_reproduction(parentA,parentB):
    first_half_A = parentA[0:(len(parentA)//2)]
    last_half_A = parentA[(len(parentA)//2):len(parentA)]
    first_half_B = parentB[0:(len(parentB)//2)]
    last_half_B = parentB[(len(parentB)//2):len(parentB)]
    firstChild = []
    secondChild = []
    firstChild = first_half_A + last_half_B
    secondChild = first_half_B + last_half_A
    return firstChild, secondChild


def Produce_Offspring(selected_population, population_size):
    '''
    Takes the parent population and selects random parents to be used in the creation of children. Takes half of each
    parent and puts those elements into the child.
    :param selected_population: The selected or fitter population from the Selection function
    :param population_size: The size that each generation is supposed to be. Set by the Initial Population
    :return: The new generation of offspring, prior mutation
    '''
    #### NOTE: I think currently this method may allow extra elements into the overall available elements, as defined by
    ### the initial problem list. Since there is nothing currently keeping parents from having similiar elements from
    ### the overall problem list, there is nothing that would keep two parents with nearly identical genes from reproducing
    ### and creating a doubling effect. This could potentially be resolved through sorting the parents elements before
    ### reproducing.
    population = []
    offspring = []
    while len(offspring) < population_size:
        parent1 = selected_population[random.randint()]
        parent2 = selected_population[random.randint()]
        first_half = parent1[0:(len(parent1)//2)]
        second_half = parent2[(len(parent2//2)):-1]
        for x in first_half:
            offspring.append(x)
        for y in second_half:
            offspring.append(y)
        population.append(offspring)

    return population




def Mutation(offspring_population, problem_list):
    '''
    The function takes each member of the produced offspring population and mutates a random number of genes (numbers)
    by either deleting the number or adding a new number from the problem_list.
    :param offspring_population: The population produced from the above Offspring function
    :param problem_list: The Overall Problem List
    :return: The mutated population
    '''
    ### NOTE: AS NOTED IN ABOVE FUNCTION, BEFORE MUTATION A STEP SHOULD BE IMPLEMENTED TO CHECK FOR AN EXISTING ZERO
    ### IN THE OFFSPRING POPULATION
    for individual in offspring_population:
        number_genes_to_modify = random.randint(1, len(individual))
        for i in range(number_genes_to_modify):
            chance = random.random()
            if chance == 1:
                index = random.randint(1, len(problem_list))
                gene = problem_list[index]
                individual.append(gene)
            elif chance == 0:
                index = random.randint(1, len(individual))
                gene = individual[index]
                individual.remove(gene)


    return offspring_population

def Individual_Mutation(child, problem_list):
    if len(child) > 10:
        number_genes_to_modify = random.randint(1, len(child) // 2)
    elif len(child) <= 3:
        return child
    else:
        number_genes_to_modify = 2

    for i in range(number_genes_to_modify):
        chance = random.randint(0, 1)
        if len(child) < len(problem_list):
            if chance == 1:
                index = random.randint(1, len(problem_list) - 1)
                gene = problem_list[index]
                if gene not in child:
                    child.append(gene)
            elif chance == 0:
                index = random.randint(1, len(child) - 1)
                gene = child[index]
                child.remove(gene)
        else:
            index = random.randint(1, len(child) - 1)
            gene = child[index]
            child.remove(gene)


    return child



def main():

    test_vals = []
    length_list = []

    for i in range(20, 50):
        length_list.append(i)
        startTime = time.process_time()
        problem_list = generate_random_problem(i)
        guaranteeASolution(problem_list)
        # print("Problem_List: ", problem_list)
        test = Genetic_Algorithm(problem_list)
        # print(test)
        endTime = time.process_time()
        timevalue = (format(endTime - startTime, "6.4f"))
        test_vals.append(timevalue)

    print(test_vals)

    plt.plot(length_list, test_vals, label="Time")
    plt.legend(loc='upper right')
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title('Genetic Algorithm Time')
    plt.show()


if __name__ == "__main__":
    main()
