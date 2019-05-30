# USB-Utility

A user space application developed in python to deal with USB related issues on Ubuntu/Debian based distributions.

# Why create this project?

The reason why I created this project is to solve specific USB related issues across the Ubuntu/Debian Linux distributions easily for users from technical to none technical backgrounds in hope it becomes useful and solves USB related issues easily for everyone.

# Features

1. Fixing the issue of USB not working (By adding the command/parameter 'iommu=soft' to the grub file located in '/etc/default/grub' and somehow disable the iommu in the bios (disabling iommu in bios may require the user manually doing it before executing/running the utility program). Also once the utility has executed and added the string data on the end of the file in the grub section 'GRUB_CMDLINE_LINUX', the utility program will need to execute the command 'update-grub' to update the latest grub file configurations for the fix to take affect on system restart/booting into the ubuntu based distribution. (DONE)

2. 'grub' file backup will be added to allow the user to backup their orginal/working version of the grub file. This will provide confidence to the user before using/applying any changes to the Linux 'grub' boot configuration file using the project/program. (DONE)

3. 'grub' file restore will be added to allow the user to automatically restore the previous/selected 'grub' within the system. This feature relies on the fact that the user has produced a 'grub' backup file before hand and the 'grub file backup' feature is implemented within the project. (DONE)
   
4. 'grub' file deletion will be added to allow the user to delete the backup date of the 'grub' file's with the purpose of allowing the user to clear the system when required. (DONE)

# How to use

1. To fix USB related issues on Ubuntu/Debian based Linux distributions, simply download the python program 'USB-Fix.py' within the 'python-modules' folder, execute the python program on the system using the command 
'python2.7 USB-Fix.py' within the terminal window, restart your system and enter the bios menu to disable the 'iommu' feature within the bios settings, save the bios settings, restart the system and boot into your Linux distribution and test to see if the 'USB' ports work correctly as expected. Do note that when you boot into your system after the above changes and your mouse/keyboard is not working,this is due to disabling the 'iommu' within the bios and re-enabling this feature will fix this problem.

2. To use the 'grub' backup feature within the project, simply download the python program 'grub-backup.py' within the 'python-modules' folder, execute the python program on
   the system using the command 'python grub-backup.py', enter the directory/folder name you wish to store your 'grub' file in and then your done. Do note that when the 
   directory/folder name already exist, an error message will display asking you to enter another unique directory/folder name. Further information on how the python program/module
   works can be found within the "grub-backup.py' file.
   
3. To use the 'grub' file restore feature, simply download the python program 'grub-file-restore.py' within the 'python-modules' folder, execute the python program on
   the system using the command 'python grub-file-restore.py' and follow through the on screen instructions.

4. To use the 'grub' automatic deletion/cleaning feature, simply download the python program 'grub_backup_deletion.py'  within the 'python-modules' folder, then execute the python program on
   the systems terminal window using the command 'python grub_backup_deletion.py' and then follow the terminal window prompts by inputting 'yes' or 'no'. Note that the module has additional checks which may prevent the module to run, an example of this could be '[ERROR] No backup files/directory's exist 'grub_backup' which means the 'grub_backup' folder is missing from the Linux filesystem directory '/etc/default' and requires creation manually or using the 'grub-backup.py' module. Addtional information about the module can be found within the 'grub_backup_deletion.py' file which is located within the 'python-modules' folder.
   
# Notes

1. The additional features the project offers (Grub backup, grub file restore and grub deletion/cleaning is optional features to use as these tools were designed for beginners to use or provide ease of use to the user who decides to use the features.

2. Any software bugs / documentation errors, please create a pull request with the applied changes or contact me with the following methods within the "Contact Me" section.

# Python Version used for development/testing

Python Version: Python 2.7.15rc1 / Python 2.7 - Default python version which comes with 'Linux Mint 19 Tara' and Ubuntu 18.04.1 LTS

# Default Grub Location

Location/Path: /etc/default - Find the file named "grub"
   
# Backup Directory Location

Ubuntu/Debian based distribution: "/etc/default/grub_backup" - Default backup directory of the users 'grub' file's ('grub_backup' folder gets produced by the 'grub-backup.py' python                                  module/program)

# Disclaimer

This project has only being tested on my system and the solutions applied within this project solved my specific issues. Use at your own risk and always create BACKUPS before modifying any system related files in case system related issue occurs in which then you can recover easily without losing valuable data/information. This repository contains tools to backup your "grub" file so if you are unsure either use the tool to backup the file or backup manually, you can find the file in the "Default Grub Location" section.

# Contact Me

Join the discord server using the following web address: https://discord.gg/B8NmmuM

Email me at: day.ashleigh@gmail.com

# Author / Credits

Mr. Ashleigh Day - (Software Engineer).

