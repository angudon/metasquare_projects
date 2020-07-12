from flask import Flask, request, url_for

file_name = 'SalesJan2009.csv'
num_rows=0
for rows in open(file_name):
    num_rows+=1

@app.route('/')
def index():
    return '''
        <form method="POST" action="/successful" enctype="multipart/form-data">
            <h2>Upload your csv File</h2>
            <input type="file" name="csv_file">
            <input type="submit">
            </form>
    '''

