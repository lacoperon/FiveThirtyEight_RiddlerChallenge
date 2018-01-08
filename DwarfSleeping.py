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
'''

def DwarfSimulation(numDwarves=7):
    # Initializes a list of dwarves.
    # Dwarves are identified by their numbers (1, ..., numDwarves)
    dwarfList    = [x+1 for x in range(numDwarves)]
    # w.l.o.g. say that each dwarf 1 owns bed 0, ..., dwarf k owns bed k-1
    # initially, all beds are empty
    emptyBedList = [x for x in range(numDwarves)]
    bedList      = ["Empty"] * numDwarves

    # First Dwarf Chooses Randomly a Bed that Isn't His Own
    rand_bed = random.sample(emptyBedList[1:], k=1)[0]
    bedList[rand_bed] = "Dwarf{}".format(1)

    emptyBedSet = set(emptyBedList)
    emptyBedSet.remove(rand_bed)

    print('Dwarves: {}'.format(dwarfList))
    print('Beds: {}'.format(bedList))
    print('EmptyBedSet: {}'.format(emptyBedSet))

    # Iterates over remaining dwarves
    for dwarf_num in dwarfList[1:]:
        print(dwarf_num)
        bed_num = dwarf_num - 1
        if bedList[bed_num] == "Empty":
            bedList[bed_num] = "Dwarf{}".format(dwarf_num)
            emptyBedSet.remove(bed_num)
        else:
            rand_bed = random.sample(emptyBedSet, k=1)[0]
            bedList[rand_bed] = "Dwarf{}".format(dwarf_num)
            emptyBedSet.remove(rand_bed)

    print('Dwarves: {}'.format(dwarfList))
    print('Beds: {}'.format(bedList))
    print('EmptyBedSet: {}'.format(emptyBedSet))

    lastDwarf = dwarfList[-1]
    for bedIndex in range(len(bedList)):
        if bedList[bedIndex] == "Dwarf{}".format(lastDwarf):
            print("Dwarf{} is in Dwarf{}'s bed".format(lastDwarf, bedIndex+1))

DwarfSimulation(7)
