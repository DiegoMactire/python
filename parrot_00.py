prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programa. "
active = True
message = " "
while message != 'quit':
    active = False
else:
    print(message)
    message = input(prompt)
    if message != 'quit':
        print(message)
