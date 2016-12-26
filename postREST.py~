from flask import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./random1', 'w')
        f.write(request.data)
        f.close()
        return "Text message written!"

    else:
        return "415 Unsupported Media Type ;)"



if __name__ == '__main__':
    app.run()

#curl -H "Content-type: application/octet-stream" -X POST http://127.0.0.1:5000/messages --data  @/home/jishuraaj/Desktop/random.csv

