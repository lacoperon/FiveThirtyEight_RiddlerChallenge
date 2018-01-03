import random

'''
This function simulates one run of FiveThirtyEight's Riddler Prompt of the
Holiday Season 2017. The prompt is as follows:

Consider a game of chance called Left, Right, Center.
Everyone sits in a circle and begins with some $1 bills.

Taking turns, each person rolls three dice.
For each die, if you roll a 1 or 2 you give a dollar to the person on your left,
if you roll a 3 or 4 you give a dollar to the person on your right,
and if you roll a 5 or 6 you put a dollar in the middle.

The moment only a single person has any money left,
the game ends and that person gets all the money in the center.

Input:
    playernum : int (the number of players in the game),
    moneynum  : int (the number of dollars each player starts with)

Output:
    num_iter : int (the number of rounds the game goes
                    on for)                                 __
                                                           _|_|_
                                                            (••)
                                                           (    )
                                                          (      )
'''

def leftRightCenterSim(playernum, moneynum):
    assert playernum > 0 and isinstance(playernum, int)
    assert moneynum  > 0 and isinstance(moneynum, int)

    moneyarray = [moneynum] * playernum
    num_iter = 1
    while sum(moneyarray) != 0:
        print(moneyarray)
        for i in range(len(moneyarray)):
            if moneyarray[i] != 0:
                outcome = random.sample(["left","right","center"], k=1)[0]
                if outcome == "left":
                    moneyarray[(i - 1) % playernum] += 1
                    moneyarray[i] -= 1
                elif outcome == "right":
                    moneyarray[(i + 1) % playernum] += 1
                    moneyarray[i] -= 1
                elif outcome == "center":
                    moneyarray[i] -= 1
        num_iter += 1

    print(moneyarray)
    print(num_iter)

    return num_iter

'''
The lrcTrial function repeats trials of this game multiple times.
Input:
    numtrials : int (the number of games we want the simulation to play),
    playernum : int (the number of players in the game),
    moneynum  : int (the number of dollars each player starts with)
Output:
    expected_num_iter : float (the expected # of rounds in the game),
    stddev            : float (the standard deviation of # rounds in game)
'''
def lrcTrial(numtrials, playernum, moneynum):

    cum_squared_num_iter = 0
    cum_num_iter = 0
    for i in range(numtrials):
        curr_result = leftRightCenterSim(playernum, moneynum)
        cum_num_iter += curr_result
        cum_squared_num_iter += curr_result ** 2.

    expected_num_iter = float(cum_num_iter) / numtrials
    expected_squared_num_iter = float(cum_squared_num_iter) / numtrials

    stddev = (expected_squared_num_iter - (expected_num_iter ** 2.)) ** (1/2.)

    return [expected_num_iter, stddev]


if __name__ == "__main__":

    numtrials = 10000
    playernum = 6
    moneynum  = 3

    print("Simulation w {0} players for ${1}".format(playernum, moneynum))
    results = lrcTrial(numtrials, playernum, moneynum )
    print("Average is {0}, StdDev is {1}".format(results[0], results[1]))
