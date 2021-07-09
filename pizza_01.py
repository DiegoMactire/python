def make_pizza(*toppings):
    """Apresenta a
pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('green peppers', 'extra cheese', 'mushrooms')