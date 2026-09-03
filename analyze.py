def welcomeUser():
    print('\nWelcome to the text analysis tool. I will mine and analyze a bodY of text from the file you give me')

# Get username
def Getusername():
    # Get input from user into the terminal
    usernameFromInput = input('\nTo begin, please enter your username: ')
    return usernameFromInput

# Greet the user
def greetuser(name):
    print('Hello' + ' ' + name)
    
welcomeUser()
username = Getusername()
greetuser(username)
