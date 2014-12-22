import random
#This is a text-based RPG based on Lakeland Jr-Sr High Schoool.
#Note: I'm probably going to remove soe of the classes.
def lakelandRPG():
    classNum = 0
    characterClass = 'N/A'
    classes = ['Nerd', 'Geek', 'Artsy', 'Jock', 'Preppy', 'Dork']
    #Stat information
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
    
    # Nerd Stats
    # Total: 41
    Nerd_ATK = 3
    Nerd_DEF = 5
    Nerd_SPCL = 10
    Nerd_INTL = 11
    Nerd_CRT = 5
    Nerd_ATHR = 7
    
    # Geek Stats
    # Total: 40
    Geek_ATK = 3
    Geek_DEF = 4
    Geek_SPCL = 10
    Geek_INTL = 9
    Geek_CRT = 8
    Geek_ATHR = 6
    
    # Artsy Stats
    # Total: 42
    Artsy_ATK = 4
    Artsy_DEF = 4
    Artsy_SPCL = 10
    Artsy_INTL = 7
    Artsy_CRT = 11
    Artsy_ATHR = 6
    
    # Jock Stats
    # Total: 39
    Jock_ATK = 11
    Jock_DEF = 10
    Jock_SPCL = 4
    Jock_INTL = 3
    Jock_CRT = 2
    Jock_ATHR = 9
    
    # Preppy Stats
    # Total: 38
    Preppy_ATK = 7
    Preppy_DEF = 5
    Preppy_SPCL = 6
    Preppy_INTL = 6
    Preppy_CRT = 3
    Preppy_ATHR = 11
    
    # Dork Stats
    # Total: 34
    Dork_ATK = 6
    Dork_DEF = 10
    Dork_SPCL = 6
    Dork_INTL = 4
    Dork_CRT = 4
    Dork_ATHR = 4
    
    # Admin Stats
    # Total: 45
    # Admins are basically going to be bosses.
    # They are NOT going to be playable.
    Admin_ATK = 7
    Admin_DEF = 4
    Admin_SPCL = 12
    Admin_INTL = 6
    Admin_CRT = 3
    Admin_ATHR = 13
    
    gender = 'genderless'
    print "This is a text test game."
    player_name = raw_input("Name: ")
    print "Hello", player_name, "!"
    print "Your gender can be male, female, on anything that you want."
    print "Use a capital letter for the first letter of your gender."
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
    #Get the class of the player and do the proper
    #introduction for their class.
    if characterClass == 'Geek':
        GeekIntro()
    if characterClass == 'Nerd':
        NerdIntro()
    if characterClass == 'Artsy':
        ArtsyIntro()
    if characterClass == 'Jock':
        JockIntro()
    if characterClass == 'Preppy':
        PreppyIntro()
    if characterClass == 'Dork':
        DorkIntro()
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