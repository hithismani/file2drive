import os
import shutil
import argparse
import dirtransfer
import optionsfile

def transfer(args):

    dir_src = (args.source)  #Source Directory
    dir_dst = (args.dest)  #Destination Directory
    dir_duplicates = (args.removedstextra)
    to_force = args.force.lower()
    #Initialize Report Figures
    existing_file = 0
    new_files = 0
    unmatched = 0
    files_removed = []
    quick_ref = "Not Set"

    dirtransfer.sourceToDest(dir_src,dir_dst,existing_file,new_files,to_force)

    if args.removedstextra.lower()=="true":
        dirtransfer.destDupliDelete(dir_src,dir_dst,unmatched,to_force)
    
    if args.saveopts.lower() == "true":
        origin_folder = os.path.basename(os.path.normpath(dir_src))
        optionsfile.saveToOptions(origin_folder,dir_src, dir_dst,dir_duplicates)
        quick_ref = origin_folder

    #Copy Hygiene On Report      
    if files_removed == []:
        files_removed = "0"
    
    #Print Report
    print("Task complete.\n\nExisting Files = " + str(existing_file)+"\nNew Files =  " + str(new_files)+"\nUnmatched Files =  " + str(unmatched)+"\nFiles Removed =  " + str(files_removed)+"\nQuick Reference = "+ quick_ref) 


def main(args):
    parser=argparse.ArgumentParser(description="picToSquare")
    parser.add_argument("-source",help="Set Source Directory",dest="source",type=str,required=True)
    parser.add_argument("-destination",help="Set Destination Directory",dest="dest",type=str,required=True)
    parser.add_argument("-removeDestinationExtras",help="Remove Extra Files Not In Source Directory",dest="removedstextra",type=str,default="False",required=False)
    parser.add_argument("-saveOptions",help="Remove Extra Files Not In Source Directory",dest="saveopts",type=str,default="False",required=False)
    parser.add_argument("-forceSpeed",help="For Test Purposes Only. Not Recommended",dest="force",type=str,default="False",required=False)

    parser.set_defaults(func=transfer)
    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])