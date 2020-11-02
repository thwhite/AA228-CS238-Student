import numpy as np
from MDP import MDP

def formMDP(MDP):
    [N, r, S, A] = [MDP.transition_count, MDP.reward_sum, MDP.state_space, MDP.action_space]
    [T, R] = np.full_like(N, fill_value=0), np.full_like(r, fill_value=0)
    for s in S:
        for a in A:
            n = sum(N[s-1, a-1, :])
            if n == 0:
                T[s-1, a-1, :] = 0
                R[s-1, a-1] = 0
            else:
                T[s-1, a-1, :] = N[s-1, a-1, :] / n
                R[s-1, a-1] = r[s-1, a-1] / n
    MDP.transition_funct = T
    MDP.reward_funct = R
