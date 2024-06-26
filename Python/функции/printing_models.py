def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Мы распечатали следующий дизайн: {current_design}!")
        completed_models.append(current_design)

    print(completed_models)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


unprinted_designes = ['телефон', 'чехол', 'флешка']
completed_models = []
print_models(unprinted_designes[:], completed_models)
show_completed_models(completed_models)
print(completed_models)
print(unprinted_designes)