inventory = []
print "Your Inventory: %s" % inventory

items_list = ["nunchucks", "sword", "milkshake", "gold brick"]

while items_list:
    command = raw_input(">> ")
    if command in items_list:
        inventory.append(command)
        print "Your Inventory: %s" % inventory
        items_list.remove(command)
    else:
        print "%s?" % command
else:
    print "items list is empty"
