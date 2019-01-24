'''
@Author: Mr. Ashleigh Day (Software Engineer)
@Date: 07/09/18
@GitHub: https://github.com/Xynous/USB-Utility

@Purpose: The purpose of this python module/program is to fix a potential issue been found with USB ports not working/detecting USB based devices
          within Ubuntu/Debian based Linux distributions by writing specific string data to the 'grub' boot file. The specific data written to the 'grub'
          file will handle the 'iommu' to be controlled on the software side compared to being controlled on the hardware/bios firmware side which is set by default. Note that you will/may have to disable the 'iommu' within the bios first and then execute this python program (instructions can be found on the github page)
'''

import os	# Imports the 'os' library for the purpose of system execution functionality

def usb_Fix():

    linux_update_grub_command = "sudo update-grub"    # String stores the 'update-grub' command

    with open("/etc/default/grub") as f: # Reads the opened 'grub' file into the string variable and replaces the old string value with the new string value
	newText=f.read().replace('quiet splash', 'quiet splash iommu=soft')	

    with open("/etc/default/grub", "w") as f:	# Writes the updated changes to the 'grub' file
	f.write(newText)

    os.system(linux_update_grub_command)    # Executes system command, will execute the 'update-grub' command to update the latest changes to the 'grub' file

usb_Fix()   # Starting point of the program, calls usb_Fix function.

