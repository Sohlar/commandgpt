#   file mgmt
#
#Create new file
with open('new_file.txt', 'w') as file:
    file.write('Initial content')

#Read a file
with open('file.txt', 'r') as file:
    content = file.read()

#Write to a file
with open('file.txt', 'a') as file:
    file.write('New content')

#Delete a file
import os
os.remove('file.txt')

#Move/rename a file
import shutil
shutil.move('source.txt', 'destination.txt')

#System Monitoring
#
#Get CPU Usage
import psutil
cpu_usage = psutil.cpu_percent()
#Get memory Usage
import psutil
memory_usage = psutil.virtual_memory().percent
#Get disk usage
import psutil
disk_usage = psutil.disk_usage('/').percent
#List running processes
import psutil
processes = [process.as_dict(attrs=['pid', 'name']) for process in psutil.process_iter()]

#Resource Allocation
#
#Set process priority
import os
import psutil

pid = os.getpid()
process = psutil.Process(pid)
process.nice(psutil.HIGH_PRIORITY_CLASS)  # Set to desired priority class




