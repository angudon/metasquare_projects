import os.path, time, csv
from zipfile import ZipFile

#Specifing zip file-name
zip_file_name = "samples.zip"
filename,file_extension = os.path.splitext(zip_file_name)

#Extracting the Zip File
with ZipFile(zip_file_name, 'r') as zip:
      
    print('Extracting all the files now...') 
    zip.extractall()
    print('Done!')

    #List all the files inside the directories
    files = os.listdir(filename)

    #creating a new csv file 
    with open('project1.csv',mode='w') as csv_file:
        fieldnames = ['Name','Full-Path','Last-Modified','Data-Created','File-Extension'] # Providing headers for the csv file
        writer = csv.DictWriter(csv_file,fieldnames)
        writer.writeheader()

        #Iterating all the files in the directory
        for i in files:
            file_name = os.path.basename(i)   #To get the name of the file

            full_path = os.path.abspath(file_name)  #To get the full path of the file

            dir_path = os.path.dirname(os.path.abspath(file_name))   # To get the directory path

            mod_time = os.path.getmtime(dir_path+"/"+filename+"/"+file_name)          #os.path.getmtime() gives the current modified time 
            mod_time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(mod_time))  #time.strftime() gives the time in the specified format
            
            create_time = os.path.getctime(dir_path+"/"+filename+"/"+file_name)       #os.path.getctime() gives the time when the file has been created
            create_time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(create_time))
            
            name,extension = os.path.splitext(file_name)                           #splitext() splits the word into 2 half
            if extension not in "  ": 
                no_gap_extension = extension                                       #get rid of spaces
            
            #appending all the data's into csv files
            writer.writerow({'Name':file_name, 'Full-Path':full_path, 'Last-Modified':mod_time1, 'Data-Created':create_time1, 'File-Extension':no_gap_extension}) 
        
        #closing the csv file
        csv_file.close()


