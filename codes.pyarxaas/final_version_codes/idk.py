import csv
reader = csv.reader(open("/home/shreshtha/Documents/zip_hier.csv", "rU"), delimiter=',')
writer = csv.writer(open("output.txt", 'w'), delimiter=';')
abc=writer.writerows(reader) 
reader_obj = csv.reader(file_obj)
    hier=[]
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        hier=row
        """ cle """
        print(hier) 
    

     