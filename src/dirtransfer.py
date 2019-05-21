import os
import shutil
from tqdm import tqdm
import time   


#Read Directory & Transfer Source File To Destination
def sourceToDest(dir_src, dir_dst,existing_file, new_files,to_force):

    for filename in tqdm(os.listdir(dir_src)):
        if os.path.exists(dir_dst + filename):
            existing_file = existing_file + 1 # File Already exists. Oops!
            tqdm.write("Transfer skipped For: " + filename)
            if to_force == "false":
                time.sleep(0.25)
        else:    
            shutil.copy( dir_src + filename, dir_dst, follow_symlinks=False) #Copy The New File!
            new_files = new_files + 1
            tqdm.write("Transferring: " + filename)
            if to_force == "false":
                time.sleep(0.25)

#Read Destination Directory & Delete Removed Files
def destDupliDelete(dir_src, dir_dst,unmatched,to_force):    
    for filename in tqdm(os.listdir(dir_dst)):
        if not os.path.exists(dir_src + filename):
            unmatched = unmatched + 1
            files_removed = files_removed.append(filename)
            os.remove(dir_dst + filename) #Remove Removed File From Backup Folder
            tqdm.write("Deleting: " + filename)
            if to_force == "false":
                time.sleep(0.25)
