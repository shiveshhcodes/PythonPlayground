import os
# Getting the name of the operating system
os_name = os.name
print('OS Name:', os_name)

# Getting detailed system information
system_info = os.uname() if hasattr(os, 'uname') else 'uname not available on this system'
print('System Info:', system_info)

