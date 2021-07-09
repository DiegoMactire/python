def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)