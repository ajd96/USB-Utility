'''
@Author: Ashleigh Day - (Software Engineer)
@Date: 14/09/18
@GitHub: https://github.com/Xynous/USB-Utility

@Purpose: The purpose of this python module/program is to provide the user the option to delete all the created 'grub' backup files/directorys within the Linux filesystem directory 'etc/default/grub_backup' which could be used to clean any left over files which are no longer required. The module/program implementation provides a simple command line interface (CLI) which the user can interact with by using keyboard input aswell as providing additional safeguarding features to prevent the user from deleting important backup data by mistake. Also the source code implementation provides additional features such as converting the input string data to lowercase and removing whitespace (Spaces) within string input data which reduces any module/program errors overall during usage by the user.
'''
import os   # Imports the 'os' library to support Linux based system execution.

def tidy_and_exit():    # Method closes the program gracefully.
    exit()

grubBackupDirectory = "/etc/default/grub_backup"    # Declared and initilized string to store the default 'grub_backup' directory.

# Put check here to see if 'grub_backup' directory exist. If it does exist, continue execution of the program, else cancel program execution and close the python program (Exit process) as there is nothing to delete in terms of 'grub_backup' directorys.
directoryAlreadyExist = os.path.isdir("/etc/default/grub_backup")	# Gets the filesystems directory to see if it exists, if the directory exists return true otherwise return false.

if directoryAlreadyExist:    # Directory already exist, continue execution of the python program.
    pass    # Allows the if statement to be used within the program logic without executing any command.

else:   # Exit python program gracefully if directory does not exist. This assumes the user has not created any 'grub' file backups automatically using the 'grub-backup.py' module.
    print("[ERROR] No backup files/directory's exist 'grub_backup'")
    print("Closing Program!")
    tidy_and_exit()  # Exit method.

ReturnedDir = os.listdir(grubBackupDirectory)   # Method returns a list of directorys from the specified directory.

print("##################################### DIRECTORYS #####################################")     # CLI formatting

counter = 0     # Counter value for each unique folder.

for directoryListing in ReturnedDir:
    print(counter, directoryListing + "        - Type: Directory" + "                  Path: /etc/default/grub_backup")     # CLI formatting + printing information in the terminal.
    counter += 1    # Increment by 1 each time around the loop and label each folder with a unqiue value.


print("##################################### DIRECTORYS #####################################")     # CLI formatting

userInput = raw_input("\nAre you sure you want to delete all the 'grub_backup' directories and data?, type yes or no: ")  # Request user input from the user.

lowercaseOne = userInput.lower()    # Convers the user string/character to lowercase (Easier to process programmicaly for a functional python program)

removeallSpaces_lowercaseOne = lowercaseOne.replace(" ", "")    # Removes all the whitespaces / spaces within the input strings.

# If input is no, call tidy_and_exit method to close the program gracefully, otherwise continue with program execution.
if not removeallSpaces_lowercaseOne.isalpha():    # Checks if the user input has only alphabetical based input (String or characters only). If its not alphabetical based input, execute the condition.
    print("Program is closing")     # Print string on screen telling the user the program is gracefully closing. This is a saftey feature to prevent user losing their 'grub_backup' data on the Linux filesystem.
    tidy_and_exit()  # Exit/close the python program when condition is met.
else:
    if removeallSpaces_lowercaseOne == "yes":
        pass    # Allows the if statement to be used within the program logic without executing any command.
    else:
        print("Program is closing")     # Print string on screen telling the user the program is gracefully closing. This is a saftey feature to prevent user losing their 'grub_backup' data on the Linux filesystem.
        tidy_and_exit()   # Exit/close the python program when condition is met.

finalUserInputWarning = raw_input("Once data and directorys are deleted they cant be recovered, are you sure you want to delete?. Type yes or no: ")  # Request user input from the user.

# Convers the user string/character to lowercase (Easier to process programmicaly for a functional python program)
lowercaseTwo = finalUserInputWarning.lower()

# Removes all the whitespaces / spaces within the input strings.
removeallSpaces_lowercaseTwo = lowercaseTwo.replace(" ", "")

if not removeallSpaces_lowercaseTwo.isalpha():    # Checks if the user input has only alphabetical based input (String or characters only). If its not alphabetical based input, execute the condition.
    print("Program is closing")     # Print string on screen telling the user the program is gracefully closing. This is a saftey feature to prevent user losing their 'grub_backup' data on the Linux filesystem.
    tidy_and_exit()  # Exit/close the python program when condition is met.

else:
    if removeallSpaces_lowercaseTwo == "yes":     # If both user input is equals to 'yes', execute the condition.
        for deleteData in os.listdir(grubBackupDirectory):                                  # List each directory within 'etc/default/grub_backup' and execute the commands within the loop.
            finalDeleteCommand = "sudo rm -r " + grubBackupDirectory + "/" + deleteData     # Concatenate the Linux delete command along with the directory location.
            os.system(finalDeleteCommand)   # Execute the Linux delete command.
    else:       # Execute 'else' statement if condition is false.
        print("Program is closing")     # Print string on screen telling the user the program is gracefully closing. This is a saftey feature to prevent user losing their 'grub_backup' data on the Linux filesystem.
        tidy_and_exit()   # Exit/close the python program when condition is met.


# Ask the user for the input of yes or no to also delete the 'grub_backup' directory.
deleteRootFolderInput = raw_input("Would you like to also delete the created 'grub_backup' root directory?, type yes or no: ")  # Request user input from the user.

lowercaseThree = deleteRootFolderInput.lower()  # Convers the user string/character to lowercase (Easier to process programmicaly for a functional python program)

removeallSpaces = lowercaseThree.replace(" ", "")   # Removes all the whitespaces / spaces within the input strings

if not removeallSpaces.isalpha():    # Checks if the user input has only alphabetical based input (String or characters only). If its not alphabetical based input, execute the condition.
    print("Program is closing")     # Print string on screen telling the user the program is gracefully closing. This is a saftey feature to prevent user losing their 'grub_backup' data on the Linux filesystem.
    tidy_and_exit()  # Exit/close the python program when condition is met.

else:   # Execute 'else' statment if the condition is false.
    if removeallSpaces == "yes":    # if variable is equal to 'yes' then execute the if block.
        os.system("sudo rm -r /etc/default/grub_backup")    # Deletes the 'grub_backup' file.

    else:   # Execute if the previous condition is false.
        print("Program is closing") # Print output to terminal
        tidy_and_exit()  # Exits the program gracefully.
