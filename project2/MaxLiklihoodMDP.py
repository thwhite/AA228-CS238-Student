class MaxLiklihoodMDP:

    def __init__(self, s, a, t, r, gamma, v, T, R):
        self.state_space = s
        self.action_space = a #this is an array of left, right, up, down, right?
        self.transition_count = t
        self.reward_sum = r
        self.discount = gamma # this is a value that we import
        self.value_funct = v
        self.transition_funct = T
        self.reward_funct = R

