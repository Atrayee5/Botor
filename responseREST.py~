from flask import Response
from flask import Flask

app = Flask(__name__)



@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=5a7d6e97bdda42129c435d7c067c3f68'

    return resp

if __name__ == '__main__':
    app.run()
