import update_model
import update_value_function
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
S = range(1,100)
A = [1, 2, 3, 4]
N = np.empty(shape=(100, 4, 100))
R = np.empty(shape=(100, 4))
V = []

# Fill up the transition and reward functions
for data_point in small_data:
    s = int(data_point[0])
    a = int(data_point[1])
    r = int(data_point[2])
    sp = int(data_point[3])
    # calculate
    N[s-1, a-1, sp-1] += 1
    R[s-1, a-1] += r

small_mdp = MaxLiklihoodMDP(S, A, N, R, 0.95, V, 0, 0)
formMDP(small_mdp)

# Policy Iteration to Find Optimal Policy
pi = np.full(shape=100, fill_value=1)

max_iter = 1000
pi = policy_iter_solve(pi, small_mdp, max_iter)