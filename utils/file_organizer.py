import os,sys
import shutil
from utils.common import get_extension,create_directory

class FileOrganizer:
    def __init__(self,source_directory):
        self.source_directory=source_directory

    def organize_files(self):

        if not os.path.exists(self.source_directory):
            print("Source Directory not exist")
            return
        
        #Getting list of all files in the directory
        for file in os.listdir(self.source_directory):
            file_path=os.path.join(self.source_directory,file)

        #Checking if file path exists and getting the extension
            if os.path.exists(file_path):
                extension=get_extension(file)
                
                #Excluding 0th item of extension as it is a .(dot)
                if extension:
                    destination_directory=os.path.join(self.source_directory,extension[1:])   
                    create_directory(destination_directory)

                    try:
                        shutil.move(file_path,os.path.join(destination_directory,file))
                        print(f"Moved {file} to {destination_directory}")

                    except Exception as e:
                        print(f"error moving {file} to {destination_directory}: {e}")

                else:
                    print(f"Skipped '{file}' as it doesn't have an extension.")
            else:
                print(f"Skipped '{file}' as it is not a file.")  

        print("File organization completed.")                      
                                  
