from flask import Flask,request, redirect, url_for

from pymongo import MongoClient
import json
import pandas as pd

app = Flask(__name__)
client = MongoClient('<mongodb-url>')
db = client['metasquare']
col = db['project2']

@app.route('/')
def index():
    return '''
        <form method="POST" enctype="multipart/form-data" action="/uploading">
            <h2>Upload only csv file</h2>
            <input type="file" name="document_file">
            <input type="submit" >
    '''
@app.route('/uploading',methods=['POST'])
def uploading():
    if 'document_file' in request.files:
        document_file = request.files['document_file']
        df = pd.read_csv(document_file)
        data = df.to_dict('records')
        count = len(data)
        col.insert_many(data, ordered = False)
        return 'Uploading completed.\nA total of '+str(count)+' records were inserted into MongoDB.'


#Compiling the program:
    #1)export FLASK_APP=project2.py
    #2)export FLASK_DEBUG=1
    #3)flask run
