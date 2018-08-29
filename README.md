# USB-Utility
A user space application developed in python/C to deal with USB related issues on Ubuntu based distributions.

# Features
1. Fixing the issue of USB 3.0 not working (By adding the command/parameter 'iommu=soft' to the grub file located in '/etc/default/grub' and somehow disable the iommu in the bios (disabling iommu in bios may require the user manually doing it before executing/running the utility)
