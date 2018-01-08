'''
Riddler Prompt for Jan 5, 2018

Each of the seven dwarfs sleeps in his own bed in a shared dormitory.
Every night, they retire to bed one at a time, always in the same sequential
order, with the youngest dwarf retiring first and the oldest retiring last.
On a particular evening, the youngest dwarf is in a jolly mood. He decides not
to go to his own bed but rather to choose one at random from among the other
six beds. As each of the other dwarfs retires, he chooses his own bed if it
isn't occupied, and otherwise chooses another unoccupied bed at random.

1. What is the probability that the oldest dwarf sleeps in his own bed?

2. What is the expected number of dwarfs who do not sleep in their own beds?
'''

import random

'''
Simulation function for one round of this game of dwarven musical beds.
Input:
    num_dwarves   : int  (the number of dwarves w beds being simulated)
    verbose       : bool (whether or not you want to print out all details)
Output:
    dwarfInOwnBed : bool (whether or not the last dwarf is in his own bed)
    num_displaced : int  (how many dwarves are displaced from their beds)
'''

def dwarfSimulation(num_dwarves=7, verbose=False):
    # Initializes a list of dwarves.
    # Dwarves are identified by their numbers (1, ..., num_dwarves)
    dwarfList    = [x+1 for x in range(num_dwarves)]
    # w.l.o.g. say that each dwarf 1 owns bed 0, ..., dwarf k owns bed k-1
    # initially, all beds are empty
    emptyBedList = [x for x in range(num_dwarves)]
    bedList      = ["Empty"] * num_dwarves

    # First Dwarf Chooses Randomly a Bed that Isn't His Own
    rand_bed = random.sample(emptyBedList[1:], k=1)[0]
    bedList[rand_bed] = "Dwarf{}".format(1)

    # Here we keep track, using a set, all remaining empty beds
    emptyBedSet = set(emptyBedList)
    emptyBedSet.remove(rand_bed)

    # Iterates over remaining dwarves
    for dwarf_num in dwarfList[1:]:
        bed_num = dwarf_num - 1
        # If a dwarf's bed is empty, he sleeps in it
        if bedList[bed_num] == "Empty":
            bedList[bed_num] = "Dwarf{}".format(dwarf_num)
            emptyBedSet.remove(bed_num)
        # Otherwise, he picks a bed at random to sleep in
        else:
            rand_bed = random.sample(emptyBedSet, k=1)[0]
            bedList[rand_bed] = "Dwarf{}".format(dwarf_num)
            emptyBedSet.remove(rand_bed)

    # Checks to see if the last dwarf is in his own bed
    lastDwarf = dwarfList[-1]
    LastDwarfInOwnBed = (bedList[-1] == "Dwarf{}".format(lastDwarf))


    # Counts the number of displaced dwarves in this particular sim run
    num_displaced_dwarves = 0
    for bedIndex in range(len(bedList)):
        if "Dwarf{}".format(bedIndex+1) != bedList[bedIndex]:
            num_displaced_dwarves += 1
            
    if verbose:
        print('Dwarves: {}'.format(dwarfList))
        print('Beds: {}'.format(bedList))
        print('# Displaced Dwarves: {}'.format(num_displaced_dwarves))

    return (LastDwarfInOwnBed, num_displaced_dwarves)

'''
Function for iterating dwarfSimulation many times
Input:
    num_iter    : int  (# of times you want to simulate dwarf beds)
    num_dwarves : int  (# dwarves simulated)
    verbose     : bool (whether of not you want to print out all details)
    SEED        : int  (the seed of the simulation)

Output:
    probLastDwarfInOwnBed : float (the probability of last dwarf in his bed)
    expectedNumDisplaced  : float (the expected number of bed-displaced dwarves)
'''
def iterateDwarfSim(num_iter, num_dwarves=7, verbose=False, SEED=1):
    print("Running Dwarven Bed Simulations w {} dwarves, {} iterations".format(
        num_dwarves, num_iter
    ))
    random.seed(SEED)

    num_last_dwarf_own_bed = 0
    for x in range(num_iter):
        if x % 1000 == 0:
            print("Running Dwarf Sim {}".format(x))
        lastDwarf, num_displaced = dwarfSimulation(num_dwarves, verbose=verbose)


iterateDwarfSim(num_iter=10000, num_dwarves=7, verbose=False)
