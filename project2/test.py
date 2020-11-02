import epsilon_greedy
import update_model
import update_value_function
from MaxLiklihoodMDP import MaxLiklihoodMDP
import numpy as np
import csv


# INIT ALL OF THE VALUES FROM DATA STRUCTURE
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

small_model = MaxLiklihoodMDP(S, A, N, R, 0.95, V)

s = 1 # pick starting state

# for i in range(5):
#     update_model()