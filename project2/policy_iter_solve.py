from MaxLiklihoodMDP import MaxLiklihoodMDP
import numpy as np

def policy_iter_solve(pi, MDP, max_k):
    for k in range(1, max_k):
        U = policy_eval(MDP, pi)
        pip = []
        for s in pi:
            pip[s] = greedy(MDP, U, s)
        if pi == pi:
            break
        pi = pip

def policy_eval(MDP, pi):
    S, T, R, g = MDP.state_space, MDP.transition_funct, MDP.reward_funct, MDP.discount
    n = 100
    Rp = [0] * n
    Tp = np.empty(shape=(n, n))
    for s in Rp:
        Rp[s] = R[s, pi[s]]
    for s in S:
        for sp in S:
            Tp[s, sp] = T[s, pi[s], sp]
    return (np.identity(n) - g*np.transpose(Tp))*np.transpose(Rp)

def lookahead(MDP, U, s, a):
    S, T, R, g, V = MDP.state_space, MDP.transition_funct, MDP.reward_funct, MDP.discount, U
    ahead = [0] * len(S)
    for sp in S:
        ahead[sp-1] = T[s-1, a-1, sp-1]*V[sp-1]
    return R[s, a] + g * sum(ahead)

def greedy(MDP, U, s):
    A = MDP.action_space
    val = []
    for a in A:
        val[a-1] = lookahead(MDP, U, s, a)
    max = np.amax(val)
    max_action = np.where(max)
    return max, max_action
