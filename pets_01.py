def describe_pet(animal_type, pet_name):
    """exibe informações sobre o animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='cat', pet_name='amoroso')
describe_pet(animal_type='cat', pet_name='oscar')