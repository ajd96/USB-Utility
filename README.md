# USB-Utility
A user space application developed in python/C to deal with USB related issues on Ubuntu based distributions.

# Features
1. Fixing the issue of USB 3.0 not working (By adding the command/parameter 'iommu=soft' to the grub file located in '/etc/default/grub' and somehow disable the iommu in the bios (disabling iommu in bios may require the user manually doing it before executing/running the utility program). Also once the utility has executed and added the string data on the end of the file in the grub section 'GRUB_CMDLINE_LINUX', the utility program will need to execute the command 'update-grub' to update the latest grub file configurations for the fix to take affect on system restart/booting into the ubuntu based distribution.

2. Consider creating a simple GUI option within python for the user to interact with the program. GUI may only be good if more than one utilty feature is added to the project/program. Probably best to create a command line application for the python script to execute and apply the fix on execution.



