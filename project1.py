from zipfile import ZipFile
zip_file_name = "samples.zip"
filename,file_extension = os.path.splitext(zip_file_name)

with ZipFile(zip_file_name, 'r') as zip:
      
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!')

