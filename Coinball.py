'''
Riddler Prompt for Oct 13, 2017

Coinball is a contest where two players take turns trying to call a fair coin
toss. The game lasts for 100 total tosses, 50 tosses for each player.
On each toss, the player calling it announces either "heads" or "tails" and
either "rush" or "pass."" If he says "rush,"" he gets one point if he calls the
toss correctly, and his opponent gets one point if the call is incorrect.

Saying "pass" means the toss is worth two points to the caller if he calls the
toss correctly and two points to his opponent if he does not. At the end, the
player with the most points wins. (The margin of victory is irrelevant;
in Coinball, league rankings are based only on wins, with a draw counting as
half a win.)

1) If you know your opponent always calls "rush" and you follow the optimal
   strategy given that knowledge, what are your chances of winning?

2) What if you know your opponent always calls "pass"?

3) If you and your opponent both play optimally, is it better to go first?
   Or to go second and therefore get the last call?

Extra credit:
   Put your Monte-Carlo simulations away and try to determine the win
   probabilities to 10 digits of precision.
'''
import random
'''
Note to begin with: I'm going to start with the naive Monte Carlo method, then
later attempt something more fancy once I've had the ability to play around
and think with this problem some more
'''

'''
Function to simulate one game of Coinball.
Input:
    numTosses        : int (number of total tosses in a game)
    playerStrategy   : list of (numTosses / 2) actions, either "pass" or "rush"
    opponentStrategy : str (same as above)
Output:
    playerWin        : float (1 if player won, 0.5 if tie, 0 if loss)
'''
def simulateGame(numTosses, playerStrategy , opponentStrategy="AP"):
    assert numTosses % 2 == 0 # otherwise the game isn't fair
    assert opponentStrategy in  ["AP", "AR", "RWB"]
    playerScore = 0
    oppScore    = 0
    for i  in range(numTosses / 2):
        # Player's Turn (currently invariant to cur_score -- TODO is to fix this)
        action = playerStrategy[i]
        assert action in ["pass", "rush"]
        playerChange, oppChange = takeTurn(action)
        playerScore += playerChange
        oppScore    += oppChange
        if opponentStrategy == "AP":
            oppChange, playerChange = takeTurn("pass")
            playerScore += playerChange
            oppScore    += oppChange
        if opponentStrategy == "AR":
            oppChange, playerChange = takeTurn("rush")
            playerScore += playerChange
            oppScore    += oppChange
        if opponentStrategy == "RWB":
            raise Exception("Unimplemented")

    # Returns whether the Player won, tied. or lost
    if playerScore > oppScore:
        return 1.
    elif playerScore == oppScore:
        return 0.5
    else:
        return 0


'''
Function which simulates a single flip in Coinball
Input:
    strat      : str (either "rush" or "pass" -- the player's choice)
    rushVal    : int (the absolute value of a "rush" toss)
    passVal    : int (the absolute value of a "pass" toss)
Output:
    tosserChange  : int (the change in the tosser's score)
    watcherChange : int (the change in the non-tosser's score)
'''

def takeTurn(strategy, rushVal=1, passVal=2):
    # Assume w.l.o.g. that the int '1' corresponds to the coin face called
    # and that '0' refers to the other face
    coinToss = random.randint(0,1)
    if strategy is "pass":
        return (passVal*coinToss, passVal*(1-coinToss))
    if strategy is "rush":
        return (rushVal*coinToss, rushVal*(1-coinToss))
