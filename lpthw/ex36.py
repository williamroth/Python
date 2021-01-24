# Choosing what the prompt will look like
prompt = ">> "

# Creating rooms that have a number of doors leading to other doors. Each room is a functions
def entrance_room():
    #This room will eventually have a sword and torch to pick up
    #This room will have doors to the east and west leading further into the cave
    # and one door to the south leading to the exit of the dungeon
    print "\n\n\n"
    print "Location: Entrance Room"
    #print "Directions: West and East and South"

    # Accept user commands and take an action
    print "\n\n\n"
    print "Options: Go West, Go East, Go South"
    hero_command = raw_input(prompt)
    if hero_command == "Go West":
        bear_room()

    elif hero_command == "Go East":
        skeleton_room()

    elif hero_command == "Go South":
        outside_dungeon()

    #elif all the other options

    else:
        print "NOT AN OPTION"

def outside_dungeon():
    #It would be awesome if you leave with enough gold you return a hero,
    #but if you leave the dungeon without enough gold you are a coward
    print "\n\n\n"
    print "Location: Outside Dungeon"
    #print "Directions: North"

    # Accept user commands and take an action
    print "\n\n\n"
    print "Options: Go North"
    hero_command = raw_input(prompt)
    if hero_command == "Go North":
        entrance_room()

    #elif all the other options

    else:
        print "NOT AN OPTION"

def bear_room():
    #If you come into this room without a torch it will eventually be too dark
    #doors to north to bbg or east to entrance
    #if you defeat bear you get gold, if not you die
    print "\n\n\n"
    print "Location: Bear Room"
    #print "Directions: North and East"

    # Accept user commands and take an action
    print "\n\n\n"
    print "Options: Go North, Go East"
    hero_command = raw_input(prompt)
    if hero_command == "Go North":
        bbg_room()

    elif hero_command == "Go East":
        entrance_room()

    #elif all the other options

    else:
        print "NOT AN OPTION"

def skeleton_room():
    #If you come into this room without a torch it will eventually be too dark
    print "\n\n\n"
    print "Location: Skeleton Room"
    #print "Directions: North and West"

    # Accept user commands and take an action
    print "\n\n\n"
    print "Options: Go North, Go West"
    hero_command = raw_input(prompt)
    if hero_command == "Go North":
        bbg_room()

    elif hero_command == "Go West":
        entrance_room()

    #elif all the other options

    else:
        print "NOT AN OPTION"

def bbg_room():
    #If you come into this room without a torch it will eventually be too dark
    print "\n\n\n"
    print "Location: BBG Room"
    #print "Directions: West and East"

    # Accept user commands and take an action
    print "\n\n\n"
    print "Options: Go North, Go West"
    hero_command = raw_input(prompt)
    if hero_command == "Go West":
        bear_room()

    elif hero_command == "Go East":
        skeleton_room()

    #elif all the other options

    else:
        print "NOT AN OPTION"

# Starting the game
print "\n\n\n"
print """
Title and Intro
    """
entrance_room()
