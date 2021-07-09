unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print("Printing model: " + current_designs)
    completed_models.append(current_designs)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
