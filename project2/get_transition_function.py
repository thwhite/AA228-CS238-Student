
def get_transition_function(MDP, s, a, sp):
    n_sp = 0
    n_tot = 0
    for data_point in MDP.state_data:
        if int(data_point[0]) == s:
            if int(data_point[1]) == a:
                if int(data_point[3]) == sp:
                    n_sp += 1
                n_tot += 1
    return n_sp/n_tot