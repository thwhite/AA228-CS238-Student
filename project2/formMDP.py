import numpy as np

# The way this function is set up is very slow when using dicts, but luckily only needs to run once.

def formMDP(MDP):
    N, r, S, A = MDP.transition_count, MDP.reward_sum, MDP.state_space, MDP.action_space
    T, R = dict(), np.full_like(r, fill_value=0)
    for s in S:
        for a in A:
            keycheck = str(s) + str(a)
            sps = []
            n = 0
            for key in N:
                if keycheck in key:
                    n += 1
                    sps.append(key)
            for key in sps:
                if n == 0:
                    T[key] = 0
                    R[s, a] = 0
                else:
                    T[key] = N[key] / n
                    R[s, a] = r[s, a] / n
    MDP.transition_funct = T
    MDP.reward_funct = R
    print("I finished forming the MDP!")


