def get_formatted_name(first_name, middle_name, last_name,):
    """devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'paiva', 'souza')
print(musician)