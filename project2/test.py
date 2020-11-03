import update_model
import update_value_function
from formMDP import formMDP
from MaxLiklihoodMDP import MaxLiklihoodMDP
from policy_iter_solve import policy_iter_solve
import numpy as np
import csv

run_small = 0
run_medium = 1

######## CODE FOR SMALL PROBLEM #########

if run_small:

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

    max_iter = 10
    pi = policy_iter_solve(pi, small_mdp, max_iter)
    print("yay!")
    print("The final, optimal policy is: ", pi)
    with open("small_policy", "w") as f:
        f.write(str(pi))
        f.close()

######## CODE FOR MEDIUM PROBLEM #########

if run_medium:

    # Init Values from Data Structure
    with open('data/medium.csv') as csv_file:
        medium_reader = csv.reader(csv_file, delimiter=',')
        medium_data = list(small_reader)
        medium_data.pop(0)

    # Declare the data inputs
    S = range(0, 49999)
    A = [0, 1, 2, 3, 4, 5, 6]
    N = np.empty(shape=(50000, 7, 50000))
    R = np.empty(shape=(50000, 7))
    V = []

    # Fill up the transition and reward functions
    for data_point in medium_data:
        s = int(data_point[0]) - 1
        a = int(data_point[1]) - 1
        r = int(data_point[2])
        sp = int(data_point[3]) - 1
        # calculate
        N[s, a, sp] += 1
        R[s, a] += r

    medium_mdp = MaxLiklihoodMDP(S, A, N, R, 1, V, 0, 0)
    formMDP(small_mdp)

    # Policy Iteration to Find Optimal Policy
    pi = [0] * 50000

    max_iter = 10
    pi = policy_iter_solve(pi, medium_mdp, max_iter)
    print("yay!")
    print("Policy for Medium: ", pi)
    with open("medium_policy", "w") as f:
        f.write(str(pi))
        f.close()
