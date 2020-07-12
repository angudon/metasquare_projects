#Modules and tools required:
    #1)pip3 install flask-pymongo
    #2)Install mongo tool for creating a local database . Refer to this link https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/ for installation.


#importing all the modules
from flask import Flask, request, url_for
from flask_pymongo import PyMongo

#creating a web server
app = Flask(__name__);

#intializing the mongo url
app.config['MONGO_URL'] = '<mongo_db_url>'
mongo = PyMongo(app)

#creating a homepage for uploading a csv file 
@app.route('/')
def index():
    return '''
        <form method="POST" action="/successful" enctype="multipart/form-data">
            <h2>Upload your csv File</h2>
            <input type="file" name="csv_file">
            <input type="submit">
            </form>
    '''

#Processing the uploaded csv file 
@app.route('/successful', methods=['POST'])
def create():
    if 'csv_file' in request.files:
        csv_file = request.files['csv_file']
        mongo.save_file(csv_file.filename, csv_file)
        mongo.db.users.insert({'username' : request.form.get('username'), 'csv_file_name' : csv_file.filename})
 #      num_rows = mongo.db.csv_file.find().count()
 #   return 'Uploading completed.\nA total of '+num_rows+' records were inserted into MongoDB.'
    return 'Uploading completed.' 


 #In terminal:
    #3)mongo <db-name>
    #4)show dbs 
    #5)use <db-name>
