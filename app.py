import os,sys
import shutil
from flask import Flask,request,render_template
from utils.common import get_extension,create_directory
from utils.file_organizer import FileOrganizer

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])

def index():
    message=""
    if request.method=='POST':
        source_directory=request.form['source_directory']
        organize_files=FileOrganizer(source_directory)
        organize_files.organize_files()

    return render_template('index.html',message=message)


if __name__=='__main__':
    app.run(debug=True)

