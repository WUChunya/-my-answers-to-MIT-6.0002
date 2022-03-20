###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    load_file = open(filename,"r")
    cow_dict = {}
    
    for line in load_file:
        cow = line.split(",")
        cow_dict[cow[0]] = int(cow[1])
        
    return cow_dict

    
# print(load_cows("ps1_cow_data.txt"))
# print(load_cows("ps1_cow_data_2.txt"))



# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # sort the dict
    dictcopy = dict(sorted(cows.items(), 
                           key=lambda item: item[1],
                           reverse = True))
    total_result = []
    
    def greedy_cow_transport_once(dictcopy,limit):
        result = []
        totalweight = 0
        for n,w in dictcopy.items():            
            if w <= limit - totalweight:
                result.append(n)
                totalweight += w
            if limit <= totalweight:
                return result
        return result

    while dictcopy != {}:
        result = greedy_cow_transport_once(dictcopy,limit)
        for n in result: del dictcopy[n]
        total_result.append(result)
    
    return total_result


#testing code
# cows1 = load_cows("ps1_cow_data.txt")
# cows2 = load_cows("ps1_cow_data_2.txt")
# print(greedy_cow_transport(cows1,limit=10))
# print(greedy_cow_transport(cows2,limit=10))

#testing code
# for partition in get_partitions(['Betsy', 'Henrietta', 'Herman', 'Maggie']):
#     print(partition)

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    N = []
    W = []
    total_result = []
    for n,w in cows.items():
        N.append(n)
        W.append(w)
    
    for partition in get_partitions(W):
        count = True
        for i in partition:
            if sum(i) > limit:
                count = False
                
        if count == True:
            for i in partition:
                result = []
                for x in i:                    
                    x = list(N)[list(W).index(x)]
                    result.append(x)
                total_result.append(result)
            return total_result
         
        
# print(brute_force_cow_transport(cows1,limit=10))
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    
    cows1 = load_cows("ps1_cow_data.txt")
    cows2 = load_cows("ps1_cow_data_2.txt")
    
    # Greedy
    start = time.time()
    print(greedy_cow_transport(cows1,limit=10))
    print(greedy_cow_transport(cows2,limit=10))
    end = time.time()
    print(end - start)
    
    # brute_force
    start = time.time()
    print(brute_force_cow_transport(cows1,limit=10))
    print(brute_force_cow_transport(cows2,limit=10))
    end = time.time()
    print(end - start)
    
print(compare_cow_transport_algorithms())
