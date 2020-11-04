import numpy as np
import time

# The way this function is set up is very slow when using dicts, but luckily only needs to run once.

def formMDP(MDP):
    start_time = time.time()
    N, r, S, A = MDP.transition_count, MDP.reward_sum, MDP.state_space, MDP.action_space
    T, R = dict(), np.full_like(r, fill_value=0)
    for s in S:
        for a in A:
            sps = []
            n = 0
            for sp in S:
                if (s, a, sp) in N:
                    n += N[(s, a, sp)]
                    n += 1
                    sps.append((s, a, sp)) # save the relevant indicies so it's faster to go through them later.
            for key in sps:
                if n == 0:
                    T[key] = 0
                    R[s, a] = 0
                else:
                    T[key] = N[key] / n
                    R[s, a] = r[s, a] / n
        if s % 1000 == 0:
            print("Iterated over 1000 states.") # Used for debugging and timing.
    MDP.transition_funct = T
    MDP.reward_funct = R
    print("I finished forming the MDP!")
    elapsed_time = time.time() - start_time
    print("I ran in " + str(elapsed_time))


