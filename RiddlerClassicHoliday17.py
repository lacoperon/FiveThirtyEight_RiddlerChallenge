import random

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

    numtrials = 1000
    playernum = 6
    moneynum  = 3

    print("Simulation w {0} players for ${1}".format(playernum, moneynum))
    results = lrcTrial(numtrials, playernum, moneynum )
    print("Average is {0}, StdDev is {1}".format(results[0], results[1]))
