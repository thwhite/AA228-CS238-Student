from formMDP import formMDP
from MaxLiklihoodMDP import MaxLiklihoodMDP
from policy_iter_solve import policy_iter_solve
import numpy as np
import csv


# Init Values from Data Structure
with open('data/small.csv') as csv_file:
    small_reader = csv.reader(csv_file, delimiter=',')
    small_data = list(small_reader)
    small_data.pop(0)


# Declare the data inputs
S = range(0, 99)
A = [0, 1, 2, 3]
N = np.empty(shape=(100, 4, 100))
R = np.empty(shape=(100, 4))
V = []

# Fill up the transition and reward functions
for data_point in small_data:
    s = int(data_point[0]) - 1
    a = int(data_point[1]) - 1
    r = int(data_point[2])
    sp = int(data_point[3]) - 1
    # calculate
    N[s, a, sp] += 1
    R[s, a] += r

small_mdp = MaxLiklihoodMDP(S, A, N, R, 0.95, V, 0, 0)
formMDP(small_mdp)

# Policy Iteration to Find Optimal Policy
pi = [0] * 100

max_iter = 100
pi = policy_iter_solve(pi, small_mdp, max_iter)
print("yay!")
print("The final, optimal policy is: ", pi)

# Upload to file

pi = [p + 1 for p in pi] # reformat for submission
with open("small_policy.txt", "w") as f:
    for p in pi:
        f.write(str(p) + "\n")
    f.close()