import numpy as np


def policy_iter_solve(pi, MDP, max_k):
    S = MDP.state_space
    for k in range(1, max_k):
        U = policy_eval(MDP, pi)
        pip = [0] * len(pi)
        for s in S:
            pip[s] = greedy(MDP, U, s)
        if pi == pip:
            break
        pi = pip
    return pi


def policy_eval(MDP, pi):
    S, T, R, g = MDP.state_space, MDP.transition_funct, MDP.reward_funct, MDP.discount
    n = len(S)
    Rp = np.empty(shape=n)
    Tp = np.empty(shape=(n, n))
    for s in S:
        Rp[s] = R[s, pi[s]]
    for s in S:
        for sp in S:
            Tp[s, sp] = T[s, pi[s], sp]
    return np.dot(np.linalg.inv(np.identity(n) - g*Tp), Rp)


def lookahead(MDP, U, s, a):
    S, T, R, g, V = MDP.state_space, MDP.transition_funct, MDP.reward_funct, MDP.discount, U
    ahead = 0
    for sp in S:
        ahead += T[s, a, sp]*V[sp]
    return R[s, a] + g * ahead


def greedy(MDP, U, s):
    A = MDP.action_space
    val = []
    for a in A:
        val.append(lookahead(MDP, U, s, a))
    return val.index(max(val)) #if a tie happens, this still only returns one value

