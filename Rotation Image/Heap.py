'''Benjamin Michael 6/21/2019'''




class minHeap:
    def __init__(self):
        self.__size = 0
        self.__theHeap = [None] ### position 0, which will not be filled

    def __len__(self):
        return self.__size

    def findMin(self):
        '''Looks at the top of the heap for the minimum value'''
        if self.__size > 0:
            return self.__theHeap[1]
        else:
            return None

    def __swap(self, x, y):
        '''

        :param x: The position of the first node to be swapped
        :param y: The position of the second node to be swapped
        :return: returns the list with the two values swapped and re-arranged
        '''
        if x >= 1 and x <= self.__size and y >= 1 and x != y:
            temp = self.__theHeap[x] ### store the value before changing it below
            self.__theHeap[x] = self.__theHeap[y] #Swap the values

    def __getParent(self, x):
        '''

        :param x: the position of the node whose parent you are looking for
        :return: The parent's position
        '''
        return x // 2 #remember, x is the index value, not the actual payload value

    def __getLeftChild(self, x):
        '''

        :param x: position of the node whose Left Child is wanted
        :return: The position of the left child
        '''
        return x * 2

    def __getRightChild(self, x):
        '''

        :param x: position of the node whose Right Child is wanted
        :return: The position of the Right Child
        '''
        return (x * 2) + 1

    def getValue(self, x):
        '''

        :param x: The postion of the node whose value is desired
        :return: The value of the requested node's payload
        '''
        return self.__theHeap[x]

    def setValue(self, x, data):
        '''

        :param x: The position where you want the new value input
        :param data: The new data
        :return: returns the new heap
        '''
        self.__theHeap.insert(x, data)

    def isEmpty(self):
        '''

        :return: returns true of false if the heap is empty
        '''
        return self.__size == 0

    def __percalateUp(self, x):
        '''

        :param x: The position of the node to be percalated up
        :return: returns the re-arranged list
        '''
        parent = self.__getParent(x) ### still getting an index value
        while parent > 0 and self.__theHeap[parent] > self.__theHeap[x]:
            self.__swap(parent, x)
            x = parent
            parent = self.__getParent(x)

    def __percaltateDn(self, x):
        '''

        :param x: The position of the node to be percalated down
        :return: returns the newly arranged heap
        '''
        LChild = self.__getLeftChild(x) #save the values
        RChild = self.__getRightChild(x)
        while LChild <= self.__size: #this checks to see if the Left child exists
            min = LChild # you know  you have a Left Child so start there
            if RChild <= self.__size and self.__theHeap[RChild] < self.__theHeap[LChild]:
                min = RChild
            if self.__theHeap[x] > self.__theHeap[min]:
                self.__swap(x, min)
                x = min
                LChild = self.__getLeftChild(x)
                RChild = self.__getRightChild(x)
            else:
                LChild = (self.__size) + 1

    def insert(self, data):
        '''

        :param data: The new data to be added to the heap
        :return: The new heap with the added value
        '''
        self.__theHeap.append(data)
        self.__size += 1
        self.__percalateUp(self.__size)

    def deleteMin(self):
        '''

        :return: Deletes the minimum value, in a heap that is the top spot
        '''
        returnValue = self.findMin()
        if returnValue is None:
            return None
        self.__theHeap[1] = self.__theHeap[self.__size]
        self.__size -= 1
        self.__theHeap.pop()
        self.__percaltateDn(1)
        return returnValue

    def __str__(self):
        result = ""
        for i in range(len(self.__theHeap)):
            result += "Node" + str(i) + ": " + str(self.__theHeap[i]) + " \n"
        return result





