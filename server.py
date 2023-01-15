from datetime import date
from datetime import datetime
from flask import Response
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("videoList.html")


@app.route("/receive", methods=['post'])
def recieve():
    files = request.files
    file = files['file']
    filename = file.filename

    with open("static/videos/"+filename, 'wb') as f:
        f.write(file.read())

    response = jsonify("File received and saved!")
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/update", methods=['post'])
def update():
    message = json.loads(request.data, strict=False)

    file = 'static/videos/userHistory.json'
    listObj = []

    with open(file) as fp:
        listObj = json.load(fp)

    listObj.append({
        "FILENAME": message['FILENAME'],
        "ID": str(message['ID']),
        "SCORE": str(message['SCORE'])
    })

    with open(file, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))

    with open("static/userData.json") as fp:
        listObj = json.load(fp)

    current = listObj['TOTAL']
    listObj.update({"TOTAL": str(int(current)+1)})

    with open("static/userData.json", 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))


    response = jsonify("File received and saved!")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getUserData", methods=['put'])
def getUserData():
    print("HI")
    return jsonify("File received and saved!")



if __name__ == "__main__":  
    app.run(debug=True)
