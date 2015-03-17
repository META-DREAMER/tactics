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
    print("list of eligible units")
    print(unit_list)
    # the unused capacity of the transport
    remain = transport.capacity

    # Just a greedy algorithm that looks at each unit
    # and selects them if they will fit (ignoring their value).
    #
    # This will NOT always find the optimum solution.
    # (e.g. running this on the cluster of troops in the lower-left corner
    # of the level many.lvl will find a sub-optimal solution
    # when value(unit) is the remainnig health of the unit)
    """
    for u in unit_list:
        if u.unit_size <= remain:
            gathered.append(u)
            remain -= u.unit_size
    """
    numUnits = len(unit_list)
    print("num units:")
    print(numUnits)
    Matrix = [[0 for i in range(numUnits)] for x in range(remain)]
    for u in range(numUnits):
        for w in range(transport.capacity):
            print("item no. in unit list")
            print(u)
            print("capacity of transport")
            print(w)
            print(int(Matrix[u-1][w]))
            Matrix[u][w] = max(Matrix[u-1][w], Matrix[u-1][w-unit_list[u].unit_size] + Matrix[u][w])

    print("Max. no. of units to load")
    print(max(Matrix[len(unit_list)][remain]))		
	
    # return the list of units from an optimal solution
    # note, in particular, that we have not actually loaded them here
    return gathered
