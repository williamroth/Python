from random import randint
from time import sleep
from sys import argv

script, hero_name = argv

cursor = "==|======> "
health = 40
bear_health = 10
skeleton_health = 10
bbeg_health = 22
inventory = ['POCKET LINT']
entrance_room_items = ['SWORD', 'NUNCHUCKS']
bbeg_items = ['TREASURE']

def bear_room(health, inventory, bear_health, skeleton_health, bbeg_health):
    while True:
        description = "The Bear Room has a BEAR you can FIGHT"
        directions = "North, East"
        print "\nDescription: %s\nDirections: %s" % (description, directions)
        print "Current Health: %s\nCurrent Inventory: %r" % (health, inventory)

        command = raw_input(cursor).upper()

        if command == "GO NORTH":
                bbeg_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GO EAST":
                entrance_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "FIGHT BEAR":

            while bear_health > 0:
                if "SWORD" in inventory or "NUNCHUCKS" in inventory:
                    attack = randint(2, 5)
                    print "\nAttacking bear for %d damage!" % attack
                    bear_health -= attack
                else:
                    attack = randint(1, 2)
                    print "\nAttacking bear with fists for %d damage!" % attack
                    bear_health -= attack

                bear_attack = randint(1, 8)
                print "\nBear attacks you for %d damage!" % bear_attack
                health -= bear_attack

                if health <= 0:
                    print "\nYou died."
                    quit()

                elif bear_health <= 0:
                    print "\nThe BEAR is dead."
                    print "Your health is %d" % health
                    break

                sleep(1)

            else:
                print "\nThe BEAR is already dead."

        else:
            print "\n%s?" % command

def bbeg_room(health, inventory, bear_health, skeleton_health, bbeg_health):
    while True:
        description = "The BBEG room has a BBEG you can FIGHT"
        directions = "East, West"
        print "\nDescription: %s\nDirections: %s" % (description, directions)
        print "Current Health: %s\nCurrent Inventory: %r" % (health, inventory)

        command = raw_input(cursor).upper()

        if command == "GO EAST":
                skeleton_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GO WEST":
                bear_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GET TREASURE":
            if bbeg_health <= 0 and bbeg_items:
                inventory.append('TREASURE')
                bbeg_items.remove('TREASURE')
                print "\nYou GET the TREASURE"

            elif bbeg_health <= 0 and not bbeg_items:
                print "\nYou already got the TREASURE"

            else:
                print "\nYou'll have to fight the BBEG for it."

        elif command == "FIGHT BBEG":

            while bbeg_health > 0:
                if "SWORD" in inventory or "NUNCHUCKS" in inventory:
                    attack = randint(2, 5)
                    print "\nAttacking BBEG for %d damage!" % attack
                    bbeg_health -= attack
                else:
                    attack = randint(1, 2)
                    print "\nAttacking BBEG with fists for %d damage!" % attack
                    bbeg_health -= attack

                bbeg_attack = randint(1, 4)
                print "\nBBEG attacks you for %d damage!" % bbeg_attack
                health -= bbeg_attack

                if health <= 0:
                    print "\nYou died."
                    quit()

                elif bbeg_health <= 0:
                    print "\nThe BBEG is dead."
                    print "Your health is %d" % health
                    print "The BBEG drops its TREASURE which you can GET"

                    break

                sleep(1)

            else:
                print "\nThe BBEG is already dead."

        else:
            print "\n%s?" % command

def skeleton_room(health, inventory, bear_health, skeleton_health, bbeg_health):
    while True:
        description = "The Skeleton Room has a SKELETON you can FIGHT"
        directions = "North, West"
        print "\nDescription: %s\nDirections: %s" % (description, directions)
        print "Current Health: %s\nCurrent Inventory: %r" % (health, inventory)

        command = raw_input(cursor).upper()

        if command == "GO NORTH":
                bbeg_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GO WEST":
                entrance_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "FIGHT SKELETON":

            while skeleton_health > 0:
                if "SWORD" in inventory or "NUNCHUCKS" in inventory:
                    attack = randint(2, 5)
                    print "\nAttacking skeleton for %d damage!" % attack
                    skeleton_health -= attack
                else:
                    attack = randint(1, 2)
                    print "\nAttacking skeleton with fists for %d damage!" % attack
                    skeleton_health -= attack

                skeleton_attack = randint(1, 4)
                print "\nSkeleton attacks you for %d damage!" % skeleton_attack
                health -= skeleton_attack

                if health <= 0:
                    print "\nYou died."
                    quit()

                elif skeleton_health <= 0:
                    print "\nThe SKELETON is dead."
                    print "Your health is %d" % health
                    break

                sleep(1)

            else:
                print "\nThe SKELETON is already dead."

        else:
            print "\n%s?" % command

def outside_room(health, inventory, bear_health, skeleton_health, bbeg_health):
    while True:
        if "TREASURE" not in inventory:
            description = "You're outside now. You haven't gotten the TREASURE yet. Get back in the dungeon!"
            directions = "North"
            print "\nDescription: %s\nDirections: %s" % (description, directions)
            print "Current Health: %s\nCurrent Inventory: %r" % (health, inventory)

            command = raw_input(cursor).upper()

            if command == "GO NORTH":
                    entrance_room(health, inventory, bear_health, skeleton_health, bbeg_health)

            else:
                print "\n%s?" % command
        else:
            print "\nCongratulations. You defeated the BBEG and got the TREASURE. you win!"
            quit()

def entrance_room(health, inventory, bear_health, skeleton_health, bbeg_health):
    while True:
        description = "The Entrance Room has a SWORD and NUNCHUCKS you can GET"
        directions = "West, East, South"
        print "\nDescription: %s\nDirections you can GO: %s" % (description, directions)
        print "Current Health: %s\nCurrent Inventory: %r" % (health, inventory)

        command = raw_input(cursor).upper()

        if command == "GET SWORD":
            if 'SWORD' in entrance_room_items:
                entrance_room_items.remove('SWORD')
                inventory.append('SWORD')
            else:
                print "\nThere is no SWORD to pick up."

        elif command == "GET NUNCHUCKS":
            if 'NUNCHUCKS' in entrance_room_items:
                entrance_room_items.remove('NUNCHUCKS')
                inventory.append('NUNCHUCKS')
            else:
                print "\nThere is no NUNCHUCKS to pick up."

        elif command == "GO WEST":
                bear_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GO EAST":
                skeleton_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        elif command == "GO SOUTH":
                outside_room(health, inventory, bear_health, skeleton_health, bbeg_health)

        else:
            print "\n%s?" % command


print "\n\n\nGreetings %s. Save your village by rescuing the TREASURE!" % hero_name
entrance_room(health, inventory, bear_health, skeleton_health, bbeg_health)
