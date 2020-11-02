import numpy as np
from MDP import MDP

def formMDP(model):
    [N, r, S, A] = [model.transition_count, model.reward_sum, model.state_space, model.action_space]
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
    model.T = T
    model.R = R
