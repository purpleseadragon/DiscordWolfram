"""from roan under can use this license"""

import math
import numpy as np

# determining wing probability of player "A"
def prob(Ra, Rb):
    expected = 1/(1 + math.pow(10,(Rb - Ra)/400))
    return expected

# defining K-factor based on USCF staggered ratings (without #of games)
def K_coeff(rating):
    if rating < 2100:
        return 32
    elif 2100 <= rating and rating <= 2400:
        return 24
    else: # final conditional for highest ranked players
        return 16

def team_rating(team1, team2):
    avg_A=np.mean(team1)
    avg_B=np.mean(team2)
    return avg_A, avg_B

#updating ratings after match
def elo_updt(Ra_current, Rb_current, win_check):
    # caclulating win probability of each side
    probA = prob(Ra_current, Rb_current)
    probB = prob(Rb_current, Ra_current)

    # k-factor for each player/team
    ka_temp = K_coeff(Ra_current)
    kb_temp = K_coeff(Rb_current)

    # case for player/team "A" wins
    if (win_check==0):
        Ra_prime = ka_temp*(1 - probA)
        Rb_prime = kb_temp*(0 - probB)

    else:
        Ra_prime = ka_temp*(0 - probA)
        Rb_prime = kb_temp*(1 - probB)

    # sample output

    return round(Ra_prime,1), round(Rb_prime,1)
