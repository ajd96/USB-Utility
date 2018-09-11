'''


@Author: Ashleigh Day
@Date: 11/09/18
@Github: https://github.com/Xynous/USB-Utility


@Purpose: The purpose of this python module/program is to provide the user the option backup their original/working version of the 'grub' file before performing any type of modifications to the file manually or
          automaitically using the other python modules provided in the project. The python module will essentially create a default backup directory called 'grub_backup' within the Linux filesystem 
          `/etc/default/grub_backup` and then allow the user to backup their `grub` file within a created 'sub' directory which gets created by user input, string concatenation and Linux system command
          execution, the 'sub' directory will be created under the 'grub_backup' directory which will keep all 'grub' file backups organized in one location. The python module/program also contains directory based
          checks to make sure the user cannot duplicate any 'grub' file backups using the same 'sub' directory name, aswell as preventing the root backup directory (grub_backup) from being duplicated. The module
          will copy the 'grub' file from the filesystem directory '/etc/default/grub' to the desired 'sub' directory automaitcally which is created earlier within the python module.


'''

import os	# Imports the 'os' library to support Linux based system execution.

makeInitialBackupDirectory = "sudo mkdir /etc/default/grub_backup"	# Stores the command to create the initial 'grub_backup' directroy within the Linux file system.
makeSubBackUpDirectory = "/etc/default/grub_backup"		# Stores the command to create the roots 'sub' backup directorys which is where the users 'grub' files will be stored/backed up.


initialDirectoryAlreadyExist = os.path.isdir("/etc/default/grub_backup")	# Gets the filesystems directory to see if it exists, if the directory exists return true otherwise return false.

if initialDirectoryAlreadyExist:	# Checks if the directory exists or not, returns the boolean value based on the conditions results.

	print("[NOTE] Backup root directory already exist") # Outputs 'Backup root directory already exist' when the directory 'grub_backup' is detected within /etc/default/grub_backup Linux filesystem.
else:
	
	os.system(makeInitialBackupDirectory)	# Execute system command to create the 'grub_backup' directory within '/etc/default' if the condition is false.


backupDirectoryName = raw_input("Enter the directory name you wish to save the 'grub' file too (NO SPACES) ") # Asks and stores users 'String' input for the sub directory name. Spaces are not supported.

createBackupDirectoryName = makeSubBackUpDirectory + "/" + backupDirectoryName # Concatenates the final string to produce the created backup directory in which the user is going to store their 'grub' file.

backupDirectoryAlreadyExist = os.path.isdir(createBackupDirectoryName)	# Checks to see if the users new input directory name exists within the 'grub_backup' directory for creation. Returns 'True' if it exists otherwise false.

if backupDirectoryAlreadyExist:		# Checks if the condition returns 'True' or 'False' depending if the directory already exists within the Linux filesystem and depending on the result, the if-else statement is executed.
	while True:
		backupDirectoryName = raw_input("[ERROR] Directory already exist, please enter a new directory name you wish to save the 'grub' file too (NO SPACES) ") # Asks and stores users 'String' input for the sub directory name. Spaces are not supported.

		createBackupDirectoryName = makeSubBackUpDirectory + "/" + backupDirectoryName # Concatenates the final string to produce the created backup directory in which the user is going to store their 'grub' file.

		backupDirectoryAlreadyExist = os.path.isdir(createBackupDirectoryName)		# Checks to see if the users new input directory name exists within the 'grub_backup' directory for creation. Returns 'True' if it exists otherwise false.

		if backupDirectoryAlreadyExist:		# Checks if the condition returns 'True' or 'False' depending if the directory already exists within the Linux filesystem and depending on the result, the if-else statement is executed.
			pass	# Allows the if statement to be used within the program logic without executing any command. (Related to solving the python indentation issue within the modules source code).
		else:
			print("[NOTE] Directory created")	# Outputs 'Directory created' in terminal if the 'sub' directory dosent already exist.
			break;	# Breaks out of the infinite loop once the directory name is unique (Returns false) and continues program execution.

else:
	print("[NOTE] Directory created")	# Outputs 'Directory created' in terminal if the 'sub' directory dosent already exist (Returned false) and continues program execution.


createBackupDirectoryNameExecution = "sudo mkdir " + makeSubBackUpDirectory + "/" + backupDirectoryName # Performs a string concatenation with multiple strings to create the Linux execution command for creating the 'sub' backup directory.

os.system(createBackupDirectoryNameExecution)	# Executes system command to create the users custom save directory for the 'grub' file.

pathToCustomDirectory = "/etc/default/grub_backup/" + backupDirectoryName # Concatenates the custom created 'grub' backup directory with the users created 'sub' directory located within the root directory. 

copyBackupGrubFile = "sudo cp /etc/default/grub " + pathToCustomDirectory	# Concatenates the 'cp' (Copy) command of the 'grub' file with the final backup directory the user has created for final system execution.

os.system(copyBackupGrubFile) # Performs a backup/copy of the 'grub' file to the custom created directory by the user by executing the final produced command.
