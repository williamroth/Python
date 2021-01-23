# Shows the user a menu of options
print(30 * "-")
print("Main Menu")
print(30 * "-")
print("1. Backup")
print("2. User management")
print("3. Reboot the server")

# Gets the input from the User
choice = raw_input("Enter your choice [1-3]: ")

#Convert string choice to integer
choice = int(choice)

#Starts the correct menu action based on user choice
if choice == 1:
    print("Starting backup...")
elif choice == 2:
    print("Starting user management...")
elif choice == 3:
    print("Rebotting server...")
else:
    print("Invalid choice. Please select again...")
    
