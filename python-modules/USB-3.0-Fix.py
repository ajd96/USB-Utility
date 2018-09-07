'''
@Author: Ashleigh Day
@Date: 07/09/18

@Purpose: The purpose of this python module/program is to fix a potential issue been found with USB-3.0 ports not working/detecting USB based devices 
          within Ubuntu/Debian based Linux distributions by writing specific string data to the 'grub' boot file. The specific data written to the 'grub'
          file will handle the 'iommu' to be controlled on the software side compared to being controlled on the hardware/bios side (Set by default).

'''

import os	# Imports the 'os' API for the purpose of system execution functionality

with open("/etc/default/grub") as f: # Reads the opened 'grub' file into the string variable and replaces the old string value with the new string value
	newText=f.read().replace('quiet splash', 'quiet splash iommu=soft')	


with open("/etc/default/grub", "w") as f:	# Writes the updated changes to the 'grub' file
	f.write(newText)

linux_update_grub_command = "sudo update-grub"	# String stores the 'update-grub' command

os.system(linux_update_grub_command)    # Executes system command, will execute the 'update-grub' command to update the latest changes to the 'grub' file

