def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing..... : {current_design}")
        completed_models.append(current_design)