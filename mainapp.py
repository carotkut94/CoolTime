from flask import Flask
from flask import request
import datetime
import calendar
from flask import jsonify
import pafy

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
                    "WeekDayName": calendar.day_name[date.timetuple().tm_wday],
                    "Hour": date.timetuple().tm_hour,
                    "Minute": date.timetuple().tm_min,
                    "Seconds": date.timetuple().tm_sec,
                    "Day": date.timetuple().tm_mday,
                    "Month": date.timetuple().tm_mon,
                    "Year": date.timetuple().tm_year
                    })


@app.route('/youtube')
def getyoutube():
    urls = request.args.get('url')
    video = pafy.new(urls)

    streams = video.streams
    audioStream = video.audiostreams
    streams_info = []
    audio_info = []
    for s in streams:
        streams_info.append((s.resolution, s.extension, s.get_filesize(), s.url))

    for a in audioStream:
        audio_info.append((a.bitrate, a.extension, a.get_filesize()))

    videoInfo = {
        "title": video.title,
        "author": video.author,
        "url": "http://www.youtube.com/watch?v=" + video.videoid,
        "duration": video.duration,
        "thumbnail": video.thumb,
        "streams": streams_info,
        "audio":audio_info

    }
    return jsonify({"success": True, "video": videoInfo})


if __name__ == '__main__':
    app.run()
