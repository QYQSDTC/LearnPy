from sys import argv
script, user_name = argv
prompt = '>'
print(f"Hi {user_name}, I am the {script} script")
print("I'd like to ask you some questions")
print(f"Do you like me? {user_name}")
likes = input(prompt)
print(f"Where do you live? {user_name}")
lives = input(prompt)
print("What computer do you have?")
computer = input(prompt)
print(f'''
    Allright, so you said \"{likes}\" liking me. You live in {lives}. Not sure where that is. You have a {computer} computer. Nice.
    ''')
