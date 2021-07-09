def build_person(first_name, last_name):
    """devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimmi', 'hendrix')
print(musician)
