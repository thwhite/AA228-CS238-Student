import numpy as np
import MDP

def formMDP(model):
    [N, r, S, A, Gamma] = [model.N, model.r, model.s, model.a, model.gamma]
    [T, R] = np.full_like(N), np.full_like(R)
    for s in S:
        for a in A:
            n = sum(N[s, a, :])
            if n == 0:
                T[s, a, :] = 0
                R[s, a] = 0.0
            else:
                T[s, a, :] = N[s, a, :] / n
                R[s, a] = r[s, a] / n
    return MDP(T, R, Gamma)