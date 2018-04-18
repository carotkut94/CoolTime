from flask import Flask
from flask import request
import datetime
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cooltime')
def get():
    time = request.args.get('time')
    return jsonify({"Date": datetime.datetime.fromtimestamp(int(time)).strftime('%d-%m-%Y %H:%M:%S')})


if __name__ == '__main__':
    app.run()
