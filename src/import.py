import os

if os.path.exists("options.csv"):
    with open(r'options.csv', 'r') as csv_file:
        lines = csv_file.readlines()[1:]
        csv_file.close()
        for line in lines:
            line = line.strip().split(',')
            if line != ['']:
                short_name= line[0]
                argument_one = line[1]
                argument_two = line[2]
                argument_three = line[3]
                print("Working With: "+short_name)
                os.system("python index.py -source "+argument_one+" -destination "+argument_two+" -removeDestinationDuplicates " + argument_three)
else:
    print("File Not Found")


