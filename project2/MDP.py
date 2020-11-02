class MDP:

    def __init__(self, T, R, gamma):
        self.trans = T
        self.reward = R
        self.gamma = gamma