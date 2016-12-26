from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Snow'

if __name__ == '__main__':
    app.run()
