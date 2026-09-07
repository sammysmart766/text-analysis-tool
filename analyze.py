from random_username.generate import generate_username

def welcomeUser():
    print('\nWelcome to the text analysis tool. I will mine and analyze a bodY of text from the file you give me')

# Get username
def Getusername():
    # Get input from user into the terminal
    usernameFromInput = input('\nTo begin, please enter your username: ')
    
    if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
        print('your username must be at least five characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces and cannot start with a number')
        print('assigning username instead')
        usernameFromInput = generate_username(1)[0]
        
    return usernameFromInput

# Greet the user
def greetuser(name):
    print('Hello' + ' ' + name)
    
welcomeUser()
username = Getusername()
greetuser(username)
