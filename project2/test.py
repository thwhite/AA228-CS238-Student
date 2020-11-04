from formMDP import formMDP
from MaxLiklihoodMDP import MaxLiklihoodMDP
from policy_iter_solve import policy_iter_solve
import numpy as np
from read_data import read_data
from scipy import sparse
import time


# Init Values from Data Structure
medium_data = read_data('data/medium.csv')

# Declare the data inputs
S = range(0, 49999)
A = [0, 1, 2, 3, 4, 5, 6]
# N = np.empty(shape=(50000, 7, 50000), dtype=np.dtype('int8'))
R = np.empty(shape=(50000, 7), dtype=np.dtype('int8'))
N = dict()
V = []

# Fill up the transition and reward functions
for data_point in medium_data:
    s = int(data_point[0]) - 1
    a = int(data_point[1]) - 1
    r = int(data_point[2])
    sp = int(data_point[3]) - 1
    # calculate
    key = (s, a, sp)
    if key in N:
        N[key] += 1
    else:
        N[key] = 1
    R[s, a] += r

medium_mdp = MaxLiklihoodMDP(S, A, N, R, 1, V, 0, 0)
print("I got to forming the MDP")
formMDP(medium_mdp)

# Policy Iteration to Find Optimal Policy
pi = [0] * 50000
max_iter = 10
print("I'm about to try and solve!")
pi = policy_iter_solve(pi, medium_mdp, max_iter)
print("yay!")
print("Policy for Medium: ", pi)

# Save data
with open("medium_policy", "w") as f:
    f.write(str(pi))
    f.close()
