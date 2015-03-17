def gather(transport, unit_list, value):
    """
    Finds the maximum possible "value" of troops that can be loaded
    in to the remaining space of a transport.

    Input:
     transport - The transport unit to be loaded.
     unit_list - The list of units that can be loaded onto transport.
       You may assume that these units are non-transport ground units
       that are already on the same team as the transport, have not
       moved this turn, and can reach the transport with a single move.
     value - a function that maps a unit to some value

    Output:
     A list of units from unit_list. Do NOT load them into the transport
     here, just compute the list of units with maximum possible value whose
     total size is at most the remaining capacity of the transport.

     The calling function from gui.py will take care of loading them.

    Target Complexity:
     It is possible to implement this method to run in time
     O(n * C) where n is the number of units in unit_list and C
     is the remaining capacity in the transport. Remember, the capacity
     of a transport and the sizes of the units are all integers.
    """

    gathered = list()

    # the unused capacity of the transport
    remain = transport.capacity

    #the number of eligible units
    numUnits = len(unit_list)
 
    #create a 2d array with dimensions remain*numUnits, initialize to 0
    Matrix = [[0 for i in range(numUnits)] for x in range(remain)]

    #dynamic programming algorithm to find highest value possible to store
    #iterate over every entry in the matrix.
    #Run time is O(n*C) where n is numUnits and C is transport capacity because we 
    #iterate over the aray only once for every entry and the array is of size n*C
    for u in range(numUnits):
        for w in range(remain):
            #calculate space left if we add unit u to the transport
            remaining_space = w-unit_list[u].unit_size+1

            #if unit cant fit, go to next iteration
            if remaining_space < 0:
                continue
            #if unit number is < 1, go to next iteration
            if u < 1:
                continue

            #store the value of unit u in the matix if it is greater than the value of the
            #previous unit. Otherwise, inherit the value of the previous unit
            Matrix[w][u] = max(Matrix[w][u-1], Matrix[remaining_space][u-1] + value(unit_list[u]))

    i = numUnits - 1
    j = remain - 1

    #trace back which units were put in transport
    while (i > 0 and j >= 0):
        #get value at i,j in array
        value1 = Matrix[j][i]
        #get value to the left of value 1
        value2 = Matrix[j][i-1]

        #if value isnt same, save the ith unit into gathered
        if not (value1 == value2):
            gathered.append(unit_list[i])
            print(unit_list[i])
            j = j - unit_list[i].unit_size
            i = i - 1
        else:
            #if value was same but the value of unit at i is less than previous value, also gather it
            if not (unit_list[i].unit_size < value2):
                gathered.append(unit_list[i])
                j = j - unit_list[i].unit_size

            #otherwise go to next unit
            i = i - 1


    # return the list of units from an optimal solution
    # note, in particular, that we have not actually loaded them here
    return gathered
