import math
import random
import time
import sys


problem = [5,4,3,2,-8, -4]

def generate_random_problem(n):
    '''
    Creates a list filled with "n" random numbers
    between -10*n and 10*n.
    :param n: The size of the generated list.
    :return: A list.
    '''
    problem = []
    for i in range(n):
        num = random.randint(-20, 20)
        while num == 0:
            num = random.randint(-20, 20)
        problem.append(num)
    return problem

def generate_random_subset(problem_list):
    sub_list = []
    length = random.randint(2, len(problem_list) -1)
    iterator = 0
    while iterator < length:
        problem_index = random.randint(1, len(problem_list) - 1)
        if problem_list[problem_index] not in sub_list:
            sub_list.append(problem_list[problem_index])
            iterator = iterator + 1

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

    #####Making two lists to hold the index values for later use###########
    problem_list_index_list = []
    sub_list_index_list = []
    for i in range(len(problem_list)):
        problem_list_index_list.append(i) #To make sure we don't check for a neighbor that is already in the sub-list

    sub_list_index_list = Index_List_Checker(problem_list, sub_problem_list)
    point_index = problem_list.index(point_to_check) #Point to check is the value in the sub-list being tested for swap
    rght_neighbor_index = abs(point_index + 1) #The point's right neighbor
    if rght_neighbor_index > len(problem_list) - 1:
        #rght_neighbor_index = rght_neighbor_index - 1
        rght_neighbor_index = -2
    lft_neighbor_index = abs(point_index - 1) #The point's left neighbor, abs used to keep from indexing a negative in edge case
    if lft_neighbor_index < 0:
        #lft_neighbor_index = lft_neighbor_index + 1
        lft_neighbor_index = -2

    ######################################################################
    if rght_neighbor_index not in sub_list_index_list and rght_neighbor_index < (len(problem_list) + 1) and rght_neighbor_index > 0:

        orig_sum = sum(sub_problem_list)
        swap_sum = (sum(sub_problem_list) - point_to_check) + problem_list[rght_neighbor_index]# is swapping closer to zero?
        add_sum = sum(sub_problem_list) + problem_list[rght_neighbor_index] # Is adding closer to zero?
        ###### check to see if swapping or adding gets us closer to zero#########

        #############
        if abs(swap_sum) < abs(add_sum):
            case = 0
            lesser_sum = swap_sum
        else:
            case = 1
            lesser_sum = add_sum


        ############
        if abs(swap_sum) < abs(orig_sum) and case == 0:
            ###### swap the value between the sublist and the problem list############
            swap = Between_List_Swap(problem_list, sub_problem_list, problem_list[rght_neighbor_index], point_to_check)
            temp_sub_list = swap
            sub_list_index_list = Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True #this is meant to break the loop in the next function
        elif abs(add_sum) < abs(orig_sum) and case == 1:
            ######### add the value from the problem list to the sublist#############
            temp_sub_list.append(problem_list[rght_neighbor_index])
            sub_list_index_list = Index_List_Checker(problem_list, sub_problem_list)
            changed_values = True

    ###############################
    elif rght_neighbor_index < -1:
        orig_sum = sum(sub_problem_list)
        edge_sum = sum(sub_problem_list) - sub_problem_list[len(sub_problem_list) - 1]
        if abs(edge_sum) < abs(orig_sum):
            temp_sub_list = sub_problem_list.copy()
            last_index = len(sub_problem_list) - 1
            temp_sub_list.pop(last_index)

    ############## repeat for other neighbor ##############################
    elif lft_neighbor_index not in sub_list_index_list and lft_neighbor_index > 0:

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
            swap = Between_List_Swap(problem_list, sub_problem_list, problem_list[lft_neighbor_index], point_to_check)
            temp_sub_list = swap
            sub_list_index_list =  Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True  # this is meant to break the loop in the next function
        elif abs(add_sum) < abs(orig_sum) and case == 1:
            temp_sub_list.append(problem_list[lft_neighbor_index])
            sub_list_index_list =  Index_List_Checker(problem_list, temp_sub_list)
            changed_values = True
    elif lft_neighbor_index < -1:
        temp_sub_list = sub_problem_list.copy()
        orig_sum = sum(temp_sub_list)
        edge_sum = sum(temp_sub_list) - temp_sub_list[0]
        if abs(edge_sum) < abs(orig_sum):
            temp_sub_list.pop(0)



    sub_problem_list = temp_sub_list
    lval = lft_neighbor_index
    Left = problem_list[lval]
    rval = rght_neighbor_index
    Right = problem_list[rval]

    ######## This should just check the left and right neighbors of a single value and then return the changed lists#
    ######## that may or may not have been changed#
    return problem_list, sub_problem_list, changed_values, sub_list_index_list, Left, Right

def Check_All_Sublist(problem_list, sub_list):
    '''
    Should check all the potential neighbors of a sublist
    :param problem_list: The whole list
    :param sub_list: The sublist to be checked and changed
    :return: The changed lists
    '''
    if sum(sub_list) == 0:
        return sub_list
    stop = False
    temp_sub_list = sub_list.copy()
    iterator = 0
    ######################## Trying to Account for opposite values#####################
    sorted_sub_list = sorted(sub_list)
    abs_pos_sub_list = []
    abs_neg_sub_list = []
    for x in sorted_sub_list:
        if x < 0:
            new_entry = abs(x)
            abs_neg_sub_list.append(new_entry)
        if x > 0:
            new_entry = abs(x)
            abs_pos_sub_list.append(new_entry)
    for i in abs_pos_sub_list:
        if i in abs_neg_sub_list:
            opposite_list = [i, (i * (-1))]
            return opposite_list
#################################################################

    for i in range(len(temp_sub_list)):
        j = i + 1
        if j >= len(temp_sub_list):
            j = j - 1
        elif sub_list[i] + sub_list[j] == 0:
            opposite_list = [sub_list[i], sub_list[j]]
            return opposite_list

    ##########################
    while stop == False and iterator < 3:         #len(temp_sub_list):
        ### stop signifies that a change has occured in the Check_Neighbors function######
        sub_list_length = (len(temp_sub_list) - 1)
        if sub_list_length == 0:
            sub_list_length = sub_list_length + 1
            print()
            print(sub_list_length)
            print()
        index_num = random.randint(0, sub_list_length)
        point = temp_sub_list[index_num]
        # print("point being fed into the Check_neighbors: ", point)
        # print("the problem list being fed into check_neighbors: ", problem_list)
        # print("The sublist: ", temp_sub_list)
        checked = Check_neighbors(problem_list, temp_sub_list, point)
        # print("The Left Neighbor: ", checked[4])
        # print("The Right Neighbor: ", checked[5])
        stop = checked[2]
        temp_sub_list = checked[1]
        iterator = iterator + 1
        # print("The iterator is: ", iterator)
        # print()
    if stop == False:
        # print("All of sublist was checked, the best solution found was: ")
        return temp_sub_list
    if stop == True:
        new_problem_list = problem_list
        new_sub_list = checked[1]
        if is_a_solution(new_sub_list) == True:
            return new_sub_list
        elif is_a_solution(new_sub_list) != True:
            iterator = 0
            y = Check_All_Sublist(new_problem_list, new_sub_list)
            return y


def Hill_Climber_Main(length_of_problem_list):
    length = length_of_problem_list
    problem_list = generate_random_problem(length)
    start_subset_list = generate_random_subset(problem_list)
    values = Check_All_Sublist(problem_list, start_subset_list)
    return values, problem_list, start_subset_list


def main():
    loop_count = 0
    while loop_count < 15:
        test = Hill_Climber_Main(7)
        print("the new sublist: ", test[0])
        sum_new_sublist = sum(test[0])
        print("the sum of the new sublist: ", sum_new_sublist)
        print("the problem_list: ", test[1])
        print("the original sublist: ", test[2])
        sum_orig_sublist = sum(test[2])
        print("the sum of the orig sublist: ", sum_orig_sublist)
        loop_count = loop_count + 1
        print("the loop count is: ", loop_count)
        print()

    #
    # test3 =  [13, -1, -9, 20, 17, 2, 14]
    # test3_sublist = [14, -9, -1, 17, 2]
    # testvalues = Check_All_Sublist(test3, test3_sublist)
    # print("the original proglem set: ", test3)
    # print("the original subset: ", test3_sublist
    # print("after running Check_All_Sublist: ", testvalues)
    testvalueshill = Hill_Climber_Main(6)


    # test3 = [16, 15, 1, 10, -19, 18, -20]
    # test3_sublist = [16, 15, 1]
    # print(test3)
    # print(test3_sublist)
    # test_values = Check_All_Sublist(test3, test3_sublist)
    # print(test_values)




if __name__ == "__main__":
    main()