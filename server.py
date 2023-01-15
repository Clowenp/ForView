from datetime import date
from datetime import datetime
from flask import Response
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json

from videos import readVideo
from questions import readQuestion, readSeenQuestions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/practice")
def practice():
    return render_template("practice.html")

@app.route("/progress")
def progress():
    return render_template("progress.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/practicePage")
def practicePage():
    info = readQuestion()
    question = [i for i in info.values()][0]
    return render_template("practicePage.html", question=question)

@app.route("/receive", methods=['post'])
def recieve():
    files = request.files
    file = files['file']
    filename = file.filename

    with open(filename, 'wb') as f:
        f.write(file.read())

    response = jsonify("File received and saved!")
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/update", methods=['post'])
def update():
    message = json.loads(request.data, strict=False)

    file = 'userHistory.json'
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


@app.route("/checkGrammar", methods = ['push'])
def checkGrammar():

    #ADD PYTHON CODE TO RUN

    response = jsonify("File received and saved!")
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":  
    app.run(debug=True)
