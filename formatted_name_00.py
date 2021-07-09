def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'souza')
print(musician)
musician = get_formatted_name('john', 'paiva', 'souza')
print(musician)
