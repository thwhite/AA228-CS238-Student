def update(model, s, a, r, sp):
    model.N[s, a, sp] += 1
    model.ρ[s, a] += r
    update(model.planner, model, s, a, r, sp)
    return model