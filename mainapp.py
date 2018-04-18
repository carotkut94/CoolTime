from flask import Flask
from flask import request
import datetime
from flask import jsonify

app = Flask(__name__)


@app.route('/live')
def live():
    return 'Yes I am alive!'


@app.route('/cooltime')
def get():
    # get request parameter
    time = request.args.get('time')

    # temp date to store
    temp = datetime.datetime.fromtimestamp(int(time)).strftime('%d-%m-%Y %H:%M:%S')
    date = datetime.datetime.strptime(temp, '%d-%m-%Y %H:%M:%S')

    # return date time data as json payload
    return jsonify({"Date": date,
                    "YearDay": date.timetuple().tm_yday,
                    "WeekDay": date.timetuple().tm_wday,
                    "Hour": date.timetuple().tm_hour,
                    "Minute": date.timetuple().tm_min,
                    "Seconds": date.timetuple().tm_sec,
                    "Day": date.timetuple().tm_mday,
                    "Month": date.timetuple().tm_mon,
                    "Year": date.timetuple().tm_year
                    })


if __name__ == '__main__':
    app.run()
