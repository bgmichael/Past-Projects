
import random
import time


problem = [5, 4, 3, 2, -8, -4]


def generate_random_problem(n):
    '''
    Creates a list filled with "n" random numbers
    between -10*n and 10*n.
    :param n: The size of the generated list.
    :return: A list.
    '''
    problem = []
    for i in range(n):
        num = random.randint(-200, 200)
        while num == 0:
            num = random.randint(-200, 200)
        problem.append(num)
    return problem


def generate_random_subset(problem_list):
    sub_list = []
    problem_index_list = []
    sub_index_list = []
    problem_length = (len(problem_list) - 1)
    length2 = random.randint(2, problem_length)
    for i in range(problem_length):
        problem_index_list.append(i)
    iterator = 0
    while iterator < length2:
        value = random.choice(problem_list)
        index = problem_list.index(value)
        if problem_list[index] not in sub_list:
            sub_list.append(value)
            iterator = iterator + 1

        #
        # problem_length = len(problem_list) - 1
        # available_index_values = len(problem_index_list) - 1
        # problem_index = random.randint(0, available_index_values)
        # if problem_index_list[problem_index] not in sub_index_list:# and problem_index_list[problem_index] in problem_index_list:
        #     value_to_add = problem_list[problem_index]
        #     sub_list.append(value_to_add)
        #     iterator = iterator + 1
        #     problem_index_list.remove(problem_index_list[problem_index])
        #     sub_index_list.append(problem_index_list[problem_index])

    return sub_list


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

    theSum = sum(solution)

    problem.append(-theSum)


def gen_solution(problem):
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

def generateRandomSuccessor(sublist, problem_list, previous_point):

    # either add one, subtract one, swap in/swap out one,
    # Then with some probablity do it again
    ### what if this returns a new sublist after the check neighbors function is run##############33
    ##successor = vector[:] this was his code
    #left blank for your enjoyment
    ############# I added a second parameter to
    point_to_check = random.choice(sublist)
    if point_to_check == previous_point:
        point_to_check = random.choice(sublist)
        point_to_check_against = random.choice(sublist)
        if point_to_check == point_to_check_against:
            loop_check = 1
        if len(sublist) == 1 and loop_check == 1:
            sublist.append(random.choice(problem_list))
            point_to_check = random.choice(sublist)
    values = Check_neighbors(problem_list, sublist, point_to_check)
    new_sub_list = values[1]
    successor = new_sub_list

    return successor, point_to_check



def Basic_Swap(List, value1, value2):
    '''
    Swaps two values in the same list
    :param List: The List containing the two values
    :param value1: first value to swap
    :param value2: second value to swap
    :return: The new list with the values in their new positions
    '''
    changed_list = List
    val1 = value1
    val2 = value2
    index1 = changed_list.index(val1)
    index2 = changed_list.index(val2)
    changed_list[index1] = val2
    changed_list[index2] = val1
    return changed_list


def Between_List_Swap(problem_list, sub_list, problem_list_value, sub_list_value):
    '''
    Meant to swap a value from the Larger problem list into the sublist which we are trying to use to get zero
    :param problem_list: The whole list
    :param sub_list: The sublist being looked at for subset sum problem
    :param problem_list_value: Value to be put into the sub-list
    :param sub_list_value: value to be swapped out of the sub-list
    :return: The changed Sublist
    '''
    changed_problem_list = problem_list.copy()
    changed_sub_list = sub_list.copy()
    val1 = problem_list_value
    val2 = sub_list_value
    index1 = problem_list.index(val1)
    index2 = sub_list.index(val2)
    changed_problem_list[index1] = val2
    changed_sub_list[index2] = val1
    return changed_sub_list


def Index_List_Checker(problem_list, sub_list):
    sub_list_index = []
    for i in sub_list:
        if i in problem_list:
            sub_list_index.append(problem_list.index(i))

    return sub_list_index


def Check_neighbors(problem_list, sub_problem_list, point_to_check):
    '''
    Takes a point from the sublist and checks its neighbors in the overall list. Tests to see if any of them improve the
    sum value. If so, it swaps them out or adds the new value, depending on which operation gets the sum closer to zero.
    :param problem_list: The overall list
    :param sub_problem_list: The subset in question
    :param point_to_check: The point in the Subset that is being swapped with a point in the problem list
    :return: There are several return meant to provide functionality in the Check_All_Sublists function
    '''
    changed_values = False
    temp_sub_list = sub_problem_list.copy()
    #print("Point being checked by Check_Neighbors: ", point_to_check)
    orig_sum = abs(sum(sub_problem_list))
    #print("Sum heading into this check: ", orig_sum)
    #####Making two lists to hold the index values for later use###########
    problem_list_index_list = []
    sub_list_index_list = []
    for i in range(len(problem_list)):
        problem_list_index_list.append(i)  # To make sure we don't check for a neighbor that is already in the sub-list
    #########Index list checker meant for updating the various index lists##################
    sub_list_index_list = Index_List_Checker(problem_list, sub_problem_list)

    point_index = problem_list.index(
        point_to_check)  # Point to check is the value in the sub-list being tested for swap
    # print("the index being checked: ", point_index)
    rght_neighbor_index = abs(point_index + 1)  # The point's right neighbor

    #if rght_neighbor_index < len(problem_list):
        # print("the right neighbor is : ", problem_list[rght_neighbor_index])

    if rght_neighbor_index > len(problem_list) - 1:
        rght_neighbor_index = -2  # meant to accound for edge cases
    lft_neighbor_index = abs(
        point_index - 1)  # The point's left neighbor, abs used to keep from indexing a negative in edge case
    lft_neighbor_index =  point_index - 1
    #if lft_neighbor_index > 0:
        # print("the left neighbor is : ", problem_list[lft_neighbor_index])

    if lft_neighbor_index < 0:
        lft_neighbor_index = -2  # meant to account for edge cases

    ######################################################################
    if rght_neighbor_index not in sub_list_index_list and rght_neighbor_index < (
            len(problem_list) + 1) and rght_neighbor_index > 0:
        orig_sum = abs(sum(sub_problem_list))
        swap_sum = abs((sum(sub_problem_list) - point_to_check) + problem_list[
            rght_neighbor_index])  # is swapping closer to zero?
        add_sum = abs(sum(sub_problem_list) + problem_list[rght_neighbor_index])  # Is adding closer to zero?
        ###### check to see if swapping or adding gets us closer to zero#########

        #############
        if abs(swap_sum) < abs(add_sum):
            case = 0  # case 0 means that the values should be swapped between lists
            lesser_sum = swap_sum
        else:
            case = 1  # case 1 means the value from problem list should be added
            lesser_sum = add_sum

        ############
        if abs(swap_sum) < abs(orig_sum) and case == 0:
            ###### swap the value between the sublist and the problem list############
            temp_sub_list = sub_problem_list.copy()
            # print("Swapping with Right Neighbor, right neighbor, point: ", problem_list[rght_neighbor_index],
            #       point_to_check)
            swap = Between_List_Swap(problem_list, temp_sub_list, problem_list[rght_neighbor_index], point_to_check)
            temp_sub_list = swap
            # print("sublist now is: ", temp_sub_list)
            # print("the sum is now, ", sum(temp_sub_list))
            # print()
            sub_list_index_list = Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True  # this is meant to break the loop in the next function
        elif abs(add_sum) < abs(orig_sum) and case == 1:
            ######### add the value from the problem list to the sublist#############
            # print("adding the right neighbor: ", problem_list[rght_neighbor_index])
            temp_sub_list.append(problem_list[rght_neighbor_index])
            # print("sublist now is: ", temp_sub_list)
            # print("the sum is now, ", sum(temp_sub_list))
            # print()
            sub_list_index_list = Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True

    elif rght_neighbor_index < -1 and changed_values == False and len(sub_problem_list) > 1:
        orig_sum = abs(sum(sub_problem_list))
        edge_sum = abs(sum(sub_problem_list) - sub_problem_list[len(sub_problem_list) - 1])
        if abs(edge_sum) < abs(orig_sum):
            # print("removing the rightmost value: ", temp_sub_list[-1])
            temp_sub_list = sub_problem_list.copy()
            last_index = len(sub_problem_list) - 1
            temp_sub_list.pop(last_index)
            # print("sublist now is: ", temp_sub_list)
            # print("the sum is now, ", sum(temp_sub_list))
            # print()

    ############## repeat for other neighbor ##############################
    if lft_neighbor_index not in sub_list_index_list and lft_neighbor_index > -1 and changed_values == False:

        orig_sum = sum(sub_problem_list)
        swap_sum = (sum(sub_problem_list) - point_to_check) + problem_list[lft_neighbor_index]
        add_sum = sum(sub_problem_list) + problem_list[lft_neighbor_index]

        #############
        if abs(swap_sum) < abs(add_sum):
            case = 0
            lesser_sum = swap_sum
        else:
            case = 1
            lesser_sum = add_sum

        if abs(swap_sum) < abs(orig_sum) and case == 0:
            # print("Swapping with Right Neighbor, left neighbor, point: ", problem_list[lft_neighbor_index],
            #       point_to_check)
            swap = Between_List_Swap(problem_list, sub_problem_list, problem_list[lft_neighbor_index], point_to_check)
            temp_sub_list = swap
            # print("sublist now is: ", temp_sub_list)
            # print("the sum is now, ", sum(temp_sub_list))
            # print()
            sub_list_index_list = Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True  # this is meant to break the loop in the next function
        elif abs(add_sum) < abs(orig_sum) and case == 1:
            # print("Adding the left neighbor to sublist: ", problem_list[lft_neighbor_index])
            temp_sub_list.append(problem_list[lft_neighbor_index])
            # print("sublist now is: ", temp_sub_list)
            # print("the sum is now, ", sum(temp_sub_list))
            # print()
            sub_list_index_list = Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True
    elif lft_neighbor_index < -1 and changed_values == False and len(sub_problem_list) > 1:
        temp_sub_list = sub_problem_list.copy()
        orig_sum = sum(temp_sub_list)
        edge_sum = sum(temp_sub_list) - temp_sub_list[0]
        if abs(edge_sum) < abs(orig_sum):
            # print("Removing the leftmost value: ", temp_sub_list[0])
            temp_sub_list.pop(0)
    #         print("sublist now is: ", temp_sub_list)
    #         print("the sum is now, ", sum(temp_sub_list))
    #         print()
    # print()

    if "[]" in temp_sub_list:
        temp_sub_list.remove("[]")

    sub_problem_list = temp_sub_list
    sub_list_index_list = Index_List_Checker(sub_problem_list, problem_list)
    lval = lft_neighbor_index
    Left = problem_list[lval]
    rval = rght_neighbor_index
    Right = problem_list[rval]

    ######## This should just check the left and right neighbors of a single value and then return the changed lists#
    ######## that may or may not have been changed#
    return problem_list, sub_problem_list, changed_values, sub_list_index_list, Left, Right, point_to_check


# def Check_All_Sublist(problem_list, sub_list):
#     '''
#     Should check all the potential neighbors of a sublist
#     :param problem_list: The whole list
#     :param sub_list: The sublist to be checked and changed
#     :return: The changed lists
#     '''
#     guess_check_counter = 0
#
#     if sum(sub_list) == 0:
#         return sub_list
#     stop = False
#     temp_sub_list = sub_list.copy()
#     iterator = 0
#     ######################## Trying to Account for opposite values#####################
#     sorted_sub_list = sorted(sub_list)
#     abs_pos_sub_list = []
#     abs_neg_sub_list = []
#     for x in sorted_sub_list:
#         if x < 0:
#             new_entry = abs(x)
#             abs_neg_sub_list.append(new_entry)
#         if x > 0:
#             new_entry = abs(x)
#             abs_pos_sub_list.append(new_entry)
#     for i in abs_pos_sub_list:
#         if i in abs_neg_sub_list:
#             opposite_list = [i, (i * (-1))]
#             return opposite_list
#     #################################################################
#
#     for i in range(len(temp_sub_list)):
#         j = i + 1
#         if j >= len(temp_sub_list):
#             j = j - 1
#         elif sub_list[i] + sub_list[j] == 0:
#             opposite_list = [sub_list[i], sub_list[j]]
#             return opposite_list
#
#     ##################################################
#     second_loop = 0
#     loop_val = (len(problem_list) * 15)
#     while second_loop < loop_val:
#         # point_to_check_index = (random.randint(1, 100)) % (len(temp_sub_list))
#         length = len(temp_sub_list)
#         if length < 2:
#             length = length + 1
#         point_to_check_index = random.randint(0, length)
#         if point_to_check_index == len(temp_sub_list):
#             point_to_check_index = point_to_check_index - 1
#         print("point_to_check_index: ", point_to_check_index)
#         point_to_check = temp_sub_list[point_to_check_index]
#         new_vals = Check_neighbors(problem_list, temp_sub_list, point_to_check)
#         guess_check_counter = guess_check_counter + 1
#         temp_sub_list = new_vals[1]
#         second_loop = second_loop + 1
#         if sum(temp_sub_list) == 0:
#             second_loop = loop_val
#
#     return temp_sub_list, guess_check_counter
#

def Hill_Climber_Main(length_of_problem_list):
    length = length_of_problem_list
    problem_list = generate_random_problem(length)
    start_subset_list = generate_random_subset(problem_list)
    values = Check_All_Sublist(problem_list, start_subset_list)
    return values, problem_list, start_subset_list


def main():
    # for n in range(3, 20):
    #     problem1 = generate_random_problem(n)
    #     guaranteeASolution(problem1)
    #     print("The problem list after guarenteeASolution: ", problem1)

    for n in range(8, 9):
        problem1 = generate_random_problem(n)
        guaranteeASolution(problem1)
        print()
        print("The problem list after guarenteeASolution: ", problem1)
        startHill = time.perf_counter()
        foundSolution = False
        noImprovementPossible = False
        theSolution = None
        randomSolution = generate_random_subset(problem1)
        print("The initial random sublist before Guinn's while loop: ", randomSolution)
        # print("Random Solution: ", randomSolution)
        currentScore = abs(sum(randomSolution))
        while not foundSolution and not noImprovementPossible:
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
                point_just_checked = 0
                bestScore = currentScore
                i = 0
                #while bestScore != 0:
                for i in range(250):
                    i = i + 1
                    if bestScore == 0:
                        break
                    print()
                    print("The problem1 before shuffle: ", problem1)
                    random.shuffle(problem1)
                    print("Shuffles performed: ", i)
                    print("The problem list is now: ", problem1)
                    print("Current sublist: ", randomSolution)
                    print()
                    for _ in range(howManyNeighbors):  # this picks the best neighbor
                        # print()
                        # print("Problem List B4: ", problem1)
                        # print("Sublist Before RandomSucessor ", randomSolution)
                        values = generateRandomSuccessor(randomSolution, problem1, point_just_checked)
                        successor = values[0]
                        # print("Sublist After RS: ", successor)
                        point_just_checked = values[1]
                        successorScore = abs(sum(successor))
                        # print("Neighbor just tried: ", point_just_checked)
                        # print("Successor Score: ", successorScore)
                        # print()
                        if successorScore == 0:
                            print("Found better with score: ", 0)
                            print("the sublist now is: ", successor)
                            foundSolution = True
                            theSolution = successor
                            noImprovementPossible = False
                            bestSuccessor = theSolution
                            bestScore = 0
                            break
                        elif abs(successorScore) < bestScore:
                            bestSuccessor = successor
                            print("the sublist now is: ", bestSuccessor)
                            randomSolution = bestSuccessor
                            bestScore = abs(successorScore)
                if bestSuccessor == None:
                    noImprovementPossible = True
                else:
                    if bestScore == 0:
                        print("Found solution: ", bestScore)
                        print("Found the solution with sublist: ", bestSuccessor)
                        break
                    else:
                        print("Found this score for checking", howManyNeighbors , " neighbors: ", bestScore)
                        randomSolution = bestSuccessor
                        print("The sublist after this number of checks: ", bestSuccessor)
                        noImprovementPossible = True# I added this to try and break the neighbor loop after a
                        #certain number of neighbor checks. Otherwise it loops infinitely b/c it never reaches zero
                        #but also bestSuccessor has been changed
                        print()
        #
        if noImprovementPossible:
            print("NO FURTHER IMPROVEMENT POSSIBLE WITHOUT SHUFFLE")
            print()

        endHill = time.perf_counter()

            #print(n, "\t", end - start, '\t', endHill - startHill)

    # loop_count = 0
    # while loop_count < 3:
    #     test = Hill_Climber_Main(7)
    #     print("the new sublist: ", test[0])
    #     sum_new_sublist = sum(test[0])
    #     print("the sum of the new sublist: ", sum_new_sublist)
    #     print("the problem_list: ", test[1])
    #     print("the original sublist: ", test[2])
    #     sum_orig_sublist = sum(test[2])
    #     print("the sum of the orig sublist: ", sum_orig_sublist)
    #     loop_count = loop_count + 1
    #     print("the loop count is: ", loop_count)
    #     print()

    # loop = 0
    # while loop < 10:
    #     test3 = generate_random_problem(12)
    #     test3_sublist = generate_random_subset(test3)
    #     testvalues = Check_All_Sublist(test3, test3_sublist)
    #     print("the original proglem set: ", test3)
    #     print("the original subset: ", test3_sublist)
    #     print("after running Check_All_Sublist: ", testvalues)
    #     print("the original sum: ", sum(test3_sublist))
    #     print("the new sum: ", sum(testvalues))
    #     loop = loop + 1

    # for i in range(10):
    #     test3 = generate_random_problem(10)
    #     test3_sublist = generate_random_subset(test3)
    #     testvalues = Check_All_Sublist(test3, test3_sublist)
    #     print()
    #     print()
    #     print("the original proglem set: ", test3)
    #     print("the original subset: ", test3_sublist)
    #     print("after running Check_All_Sublist: ", testvalues)
    #     print("the original sum: ", sum(test3_sublist))
    #     print("newvals:, ", testvalues)
    #     print("the new sum: ", sum((testvalues[0])))
    #     print("the number of guesses: ", testvalues[1])
    #     print()

    # test4 = [7, 6, -13, 12, 7, 9, 15, 17, 82, -100, 19, 23, -19]
    # test4_sublist = [-13, 7, 15, 9]
    # print("the original list: ", test4)
    # print("the original sublist:, ", test4_sublist)
    # print("the original sum: ", sum(test4_sublist))
    # test4_values = Check_neighbors(test4, test4_sublist, -17)
    # print(test4_values[0])
    # print(test4_values[1])
    # print(test4_values[2])
    # print(test4_values[3])
    # print(test4_values[4])
    # print(test4_values[5])
    # CheckAll = Check_All_Sublist(test4, test4_sublist)
    # print("the checkall function results: ", CheckAll[0])
    # print("the sum is now, ", sum(CheckAll[0]))
    # print("the number of guesses: ", CheckAll[1])

    # Check_All_Sublist: [-17, 67, -125, 49, 45]

    # return problem_list, sub_problem_list, changed_values, sub_list_index_list, Left, Right
    # for i in range(100):
    #     testlist = generate_random_problem(15)
    #     test_sub = generate_random_subset(testlist)
    #     print(testlist)
    #     print(test_sub)
    #     print(i)


if __name__ == "__main__":
    main()