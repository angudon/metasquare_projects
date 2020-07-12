from flask import Flask, request, url_for
from flask_pymongo import PyMongo

file_name = 'SalesJan2009.csv'
num_rows=0
for rows in open(file_name):
    num_rows+=1

app = Flask(__name__);
app.config['MONGO_URL'] = '<mongo_db_url>'
mongo = PyMongo(app)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/successful" enctype="multipart/form-data">
            <h2>Upload your csv File</h2>
            <input type="file" name="csv_file">
            <input type="submit">
            </form>
    '''

@app.route('/successful', methods=['POST'])
def create():
    if 'csv_file' in request.files:
        csv_file = request.files['csv_file']
        mongo.save_file(csv_file.filename, csv_file)
        mongo.db.users.insert({'username' : request.form.get('username'), 'csv_file_name' : csv_file.filename})

    return 'Uploading completed.\nA total of '+num_rows+' records were inserted into MongoDB.'
    

