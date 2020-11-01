import random

# i'm not exactly sure how to implement the lookahead yet. we'll work on it.

def epsilon_greedy(model, s, pi):
    A, e = model.a, pi.e
    if random.rand() < e:
        return random.choice(A)
    else:
        Q[s, a] = lookahead(model, s, model.a)
        return max(Q)

