'''
Riddler Prompt for Oct 13, 2017

Coinball is a contest where two players take turns trying to call a fair coin
toss. The game lasts for 100 total tosses, 50 tosses for each player.
On each toss, the player calling it announces either “heads” or “tails” and
either “rush” or “pass.” If he says “rush,” he gets one point if he calls the
toss correctly, and his opponent gets one point if the call is incorrect.

Saying “pass” means the toss is worth two points to the caller if he calls the
toss correctly and two points to his opponent if he does not. At the end, the
player with the most points wins. (The margin of victory is irrelevant;
in Coinball, league rankings are based only on wins, with a draw counting as
half a win.)

1) If you know your opponent always calls “rush” and you follow the optimal
   strategy given that knowledge, what are your chances of winning?

2) What if you know your opponent always calls “pass”?

3) If you and your opponent both play optimally, is it better to go first?
   Or to go second and therefore get the last call?

Extra credit:
   Put your Monte-Carlo simulations away and try to determine the win
   probabilities to 10 digits of precision.
'''

'''
Note to begin with: I'm going to start with the naive Monte Carlo method, then
later attempt something more fancy once I've had the ability to play around
and think with this problem some more
'''
