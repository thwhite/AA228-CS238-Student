from MaxLiklihoodMDP import MaxLiklihoodMDP
import numpy as np


def policy_iter_solve(pi, MDP, max_k):
    for k in range(1, max_k):
        U = policy_eval(MDP, pi)
        pip = np.empty(shape=len(pi))
        for s in pi:
            print(greedy(MDP, U, s)[1])
            pip[s] = greedy(MDP, U, s)[1]
        if np.array_equal(pi, pip):
            break
        print(pip)
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
    ahead = [0] * len(S)
    for sp in S:
        # print(T[s, a, sp])
        # print(V[sp])
        ahead += T[s, a, sp]*V[sp]
    return R[s, a] + g * sum(ahead)


def greedy(MDP, U, s):
    A = MDP.action_space
    val = []
    for a in A:
        val.append(lookahead(MDP, U, s, a))
    max = np.amax(val)
    max_action = np.where(max)[0][0]
    return max, max_action
