🚨 Script is still under develpoment. Expect this documentation to be completed soon.

# file2drive 
Inspired by the need to backup all installed fonts from my local drive into my OneDrive, I came up with file2drive. An experimental script that makes use of Shutil to enter a folder and push them into a backup folder seamlessly. 

*Tested On Windows 10 + Python 3.6* 

### Features
- Transfer files from virtually any directory to another one, with a single script. 
- Save your options into a file, to 'schedule' tasks in a single sprint.
- Remove extra files in your destination directory.

### Usage
1. git pull this repository 
2. cd file2drive 
3. run <code>python src/index.py -source <i>(Source Directory)</i> -destination <i>(Destination Directory)</i></code> 
4. your files would be transferred.

### Optional Parameters
1. -removeDestinationExtras <i>True (Defaults False)</i>
    
    This removes any file in the destination folder which IS NOT present in your source folder.
2. -saveOptions <i>True (Defaults False)</i>
    
    Saves options into an options.cvs file, for you to automate your tasks in the future.

### Experimental
1. -forceTransfer <i>True (Defaults False)</i>
    
    The only reason this is added in, is to bug test. I would not recommend you run the script on production folders with this option set to True.

### Importing Options
To import options you simply run <code>python src/import.py</code>. The script will look for options.csv in the root folder and perform every task you list within it. Options here are set using -saveOptions mentioned above. 

### Pending
- Directory Restructuring
- Completing Documentation
- Testing on MacOS and Linux

### Future Plans
- Supplementing CLI with a possible GUI. 
- Memory Optimization of the script.

I’m just trying to create daily utility tools using Python. If this made your life easier, you know what you can do. If you feel something could change or be better optimized, please critique and contribute to this project.