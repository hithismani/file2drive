import csv
from os.path import exists

def saveToOptions(origin_folder, source_dir, output_dir, removedstdupli):
    if exists("options.csv"):
        fields=[origin_folder, source_dir,output_dir,removedstdupli]
        with open(r'options.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            csv_file.close()
            
    else:    
        with open('options.csv', mode='w+', newline='') as csv_file:
            fieldnames = ['short_name','source_dir', 'output_dir', 'remove_duplicates']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'short_name': origin_folder,'source_dir': source_dir, 'output_dir': output_dir, 'remove_duplicates': removedstdupli})
            csv_file.close()
    
    with open('options.csv') as f:
        data = list(csv.reader(f))
        new_data = [a for i, a in enumerate(data) if a not in data[:i]]
        with open('options.csv', 'w') as t:
            write = csv.writer(t)
            write.writerows(new_data)