'''
@Author: Ashleigh Day
@Date: 22/09/18
@Github: https://github.com/Xynous/USB-Utility


@Purpose: The purpose of this python program/module is to provide a 'grub' file restore feature which will allow the user to restore their orignal backed up
'grub' file on the linux filesystem by inserting or selecting the text. The feature however does rely on the user to have already created a 'grub' backup using
the 'grub-backup.py' python module/program, otherwise this features would be useless to the user. The current python module/program implementation contains a basic
CLI based interface which will display the 'sub' backup directorys which the user has created to provide convenience for the user to display the created 'grub' backups
without interacting with external windows. The python module/program also contains basic error checking with the 'grub_backup' directory and the 'sub' backup directorys
in terms of detecting the directorys already exist or detecting invalid input which will trigger the event handler to close the program.

'''

import os    # Imports the 'os' library to support Linux based system execution.

grubBackupDirectory = "/etc/default/grub_backup"    # Declared and initilized string to store the default 'grub_backup' directory.
defaultGrubFile = "/etc/default"    # String variable storing the default/working grub file within the Linux filesystem.
grubRestoreExecution = "sudo cp "   # String variable storing parts of the Linux copy 'cp' operation syntax for later usage within the python module/program.

directoryAlreadyExist = os.path.isdir("/etc/default/grub_backup")	# Gets the filesystems directory to see if it exists, if the directory exists return true otherwise return false.

if directoryAlreadyExist:    # Directory already exist, continue execution of the python program.
    pass    # Allows the if statement to be used within the program logic without executing any command. (Related to solving the python indentation issue within the modules source code).

else:   # Exit python program gracefully if directory does not exist. This assumes the user has not created any 'grub' file backups automatically using the 'grub-backup.py' module.
    print("[ERROR] No backup files/directory's exist 'grub_backup'")
    print("Closing Program!")
    exit()  # Exit method.

ReturnedDir = os.listdir(grubBackupDirectory)   # Method returns a list of directorys from the specified directory.

print("##################################### DIRECTORYS #####################################")     # CLI formatting.

counter = 0     # Counter value for each unique folder.

for directoryListing in ReturnedDir:
    print(counter, directoryListing + "        - Type: Directory" + "                  Path: /etc/default/grub_backup")     # CLI formatting + printing information in the terminal window.
    counter += 1    # Increment by 1 each time around the loop and label each folder with a unqiue value.


print("##################################### DIRECTORYS #####################################")     # CLI formatting.

grubRestoreInput = raw_input("Enter the desired directory name to restore the 'grub' file: ")   # Asks the user for the directory name input and stores the data as a string.

subDirectoryString_Concatenation = grubBackupDirectory + "/" + grubRestoreInput     # Concatenates the custom 'grub' backup directory with the users inputted directory name to select.

subDirectoryAlreadyExist = os.path.isdir(subDirectoryString_Concatenation)	# Gets the filesystems directory to see if it exists, if the directory exists return true otherwise return false.

if subDirectoryAlreadyExist:    # If the 'sub' directory already exist return 'True' and execute block.
    print("'grub' file restored successfully!")     # Print string to terminal.
else:   # Execute 'else' statement if the condition is 'False'.
    print("[ERROR] sub directory or 'grub' file does not exist")    # Print string to terminal.
    print("Closing Program!")   # Print string to terminal.
    exit() # Exit method which will close the program.


grubRestoreExecution_Concatenation = grubRestoreExecution + grubBackupDirectory + "/" + grubRestoreInput + "/" + "grub" + " " + defaultGrubFile     # Concatenates the final execution string to copy the selected 'grub' file to the 'default' directory (Current used version on Linux filesystems).

os.system(grubRestoreExecution_Concatenation)   # Executes the Linux system command to perform the copy 'cp' operation on the 'grub' backup file to the 'default' directory.
