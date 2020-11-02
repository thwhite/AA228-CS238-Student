import numpy as np
from MDP import MDP

def formMDP(MDP):
    [N, r, S, A] = [MDP.transition_count, MDP.reward_sum, MDP.state_space, MDP.action_space]
    [T, R] = np.full_like(N, fill_value=0), np.full_like(r, fill_value=0)
    for s in S:
        for a in A:
            n = sum(N[s, a, :])
            if n == 0:
                T[s, a, :] = 0
                R[s, a] = 0
            else:
                T[s, a, :] = N[s, a, :] / n
                R[s, a] = r[s, a] / n
    MDP.transition_funct = T
    MDP.reward_funct = R
