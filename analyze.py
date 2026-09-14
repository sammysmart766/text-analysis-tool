from random_username.generate import generate_username

def welcomeUser():
    print('\nWelcome to the text analysis tool. I will mine and analyze a bodY of text from the file you give me')

# Get username
def Getusername():
    
    maxAttempts = 3
    Attempts = 0
    
    # Get input from user into the terminal
    while Attempts < maxAttempts:  
        inputPrompt = ''
        if Attempts == 0:
           inputPrompt = '\nTo begin, please enter your username: '
        else:
            inputPrompt = '\nPlease try again: '
            
        usernameFromInput = input(inputPrompt)
    
        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print('\nyour username must be at least five characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces and cannot start with a number')
            Attempts += 1      
        else:
            return usernameFromInput

        
    print('\nExhausted all ' + str(maxAttempts) + ' attempts. ' + 'Assigning username instead')
    return generate_username(1)[0]
        
    

# Greet the user
def greetuser(name):
    print('Hello' + ' ' + name)
    
welcomeUser()
username = Getusername()
greetuser(username)
