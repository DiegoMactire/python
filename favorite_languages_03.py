favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'
    }
print("The following languages have been mentioned:")
for languages in set(favorite_languages.values()):
    print(languages.title())
