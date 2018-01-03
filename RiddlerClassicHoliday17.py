import random

def leftRightCenterSim(playernum, moneynum):
    assert playernum > 0 and isinstance(playernum, int)
    assert moneynum  > 0 and isinstance(moneynum, int)

    print("Simulation w {0} players for ${1}".format(playernum, moneynum))

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

leftRightCenterSim(3,1)
