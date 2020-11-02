import epsilon_greedy
import update_model
import update_value_function
from MaxLiklihoodMDP import MaxLiklihoodMDP
import numpy as np

# read data
S = list(range(1, 100)) # names of all of the states
a = [1, 2, 3, 4] # action space
t = r = np.empty(shape=(100, 4, 100))
r = np.empty(shape=(100, 4)) # empty array we fill with reward values later, dims of state, action
v = np.empty(shape=(100, 4)) # will deal with this later

small_model = MaxLiklihoodMDP(S, a, t, r, 0.95, v)
print(small_model.state)

# question. are these things initialized all at once or added later?


# for i in range(5):
#     update_model()