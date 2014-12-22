import random
def lakelandRPG():
    classNum = 0
    characterClass = 'N/A'
    classes = ['Nerd', 'Geek', 'Artsy', 'Jock', 'Preppy', 'Dork']
    '''
     STATS INFO
    ------------
    ATK = attack
    DEF = defense
    SPCL = special
    INTL = intelligence
    CRT = creativity
    ATHR = authority
    '''
    
    # Nerd Stats 41
    Nerd_ATK = 3
    Nerd_DEF = 5
    Nerd_SPCL = 10
    Nerd_INTL = 11
    Nerd_CRT = 5
    Nerd_ATHR = 7
    
    # Geek Stats 40
    Geek_ATK = 3
    Geek_DEF = 4
    Geek_SPCL = 10
    Geek_INTL = 9
    Geek_CRT = 8
    Geek_ATHR = 6
    
    # Artsy Stats 42
    Artsy_ATK = 4
    Artsy_DEF = 4
    Artsy_SPCL = 10
    Artsy_INTL = 7
    Artsy_CRT = 11
    Artsy_ATHR = 6
    
    # Jock Stats 39
    Jock_ATK = 11
    Jock_DEF = 10
    Jock_SPCL = 4
    Jock_INTL = 3
    Jock_CRT = 2
    Jock_ATHR = 9
    
    # Preppy Stats 38
    Preppy_ATK = 7
    Preppy_DEF = 5
    Preppy_SPCL = 6
    Preppy_INTL = 6
    Preppy_CRT = 3
    Preppy_ATHR = 11
    
    # Dork Stats 34
    Dork_ATK = 6
    Dork_DEF = 10
    Dork_SPCL = 6
    Dork_INTL = 4
    Dork_CRT = 4
    Dork_ATHR = 4
    
    gender = 'genderless'
    print "This is a text test game."
    player_name = raw_input("Name: ")
    print "Hello", player_name, "!"
    print "Your gender can be male, female, on anything that you want."
    gender = raw_input("Gender: ")
    #Lowecase letters. Just. No...
    if gender == 'male':
        gender = 'Male'
    if gender == 'female':
        gender = 'Female'
    print "Choose a class."
    # Print the list of classes.
    for classNum in range(0, 6):
        print classes[classNum]
        classNum += 1
    characterClass = raw_input("Class: ")
    # Basic error handling
    while characterClass not in classes:
        print "Invalid class. Please type with a capital letter."
        characterClass = raw_input("Class: ")
    print "You are a", characterClass
    if characterClass == 'Geek':
        GeekIntro()
    if characterClass == 'Nerd':
        NerdIntro()
    if characterClass == 'Artsy':
        ArtsyIntro()
def GeekIntro():
    print '[Geek intro goes here]'
def NerdIntro():
    print '[Nerd intro goes here]'
def ArtsyIntro():
    print '[Artsy intro goes here]'
def JockIntro():
    print '[Jock intro goes here]'
def PreppyIntro():
    print '[Preppy intro goes here]'
def DorkIntro():
    print '[Dork intro goes here]'