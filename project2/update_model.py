def update_model(model, s, a, r, sp):
    model.N[s, a, sp] += 1
    model.ρ[s, a] += r
    update_model(model.planner, model, s, a, r, sp)
    return model