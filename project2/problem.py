class MaxLiklihoodMDP:

    def __init__(self, s, a, t, r, gamma, v):
        self.state = s
        self.action_space = a
        self.transition_count = t
        self.reward_sum = r
        self.discount = gamma
        self.value_funct = v

