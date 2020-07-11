import os, time
from zipfile import ZipFile
zip_file_name = "samples.zip"
filename,file_extension = os.path.splitext(zip_file_name)

with ZipFile(zip_file_name, 'r') as zip:
      
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!')
    files = os.listdir(filename)
    for i in files:
            file_name = os.path.basename(i)
            full_path = os.path.abspath(file_name)
            dir_path = os.path.dirname(os.path.abspath(file_name))
            mod_time = os.path.getctime(dir_path+"/"+filename+"/"+file_name)
            mod_time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(mod_time))
            create_time = os.path.getctime(dir_path+"/"+filename+"/"+file_name)
            create_time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(create_time))
            name,extension = os.path.splitext(file_name)
            print('Name':file_name, 'Full-Path':full_path, 'Last-Modified':mod_time1, 'Data-Created':create_time1, 'File-Extension':no_gap_extension)

