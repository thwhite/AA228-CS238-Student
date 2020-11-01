def formMDP(model):
    [N, R, S, A, Gamma] = [model.N, model.r, model.s, model.a, model.gamma]
    [T, R] = similar(N), similar(R)
    for s in S:
        for a in A:
            n = sum(N[s, a, :])
            if n == 0:
                T[s, a, :] = 0
                R[s, a] = 0.0
            else:
                T[s, a, :] = N[s, a, :] / n
                R[s, a] = ρ[s, a] / n
    return MDP(T, R, Gamma)