import urllib2

from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send, emit
from urllib import unquote
import imagerectest
import base64

import textscrape

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
globday = 3
globtime = 16

@app.route('/')
def cam():
    return render_template("liveweb1.html")

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg)

@socketio.on('result')
def handleResult(result):
    socketio.emit('result', result)

@socketio.on('failure')
def handleFailure(failure):
    socketio.emit('failure', failure.text)

@socketio.on('time')
def handleTime(time):
    #global globtime    # Needed to modify global copy of globvar
    #globtime = time
    print time
    socketio.emit('time', time)

@socketio.on('day')
def handleDay(day):
    #global globday    # Needed to modify global copy of globvar
    #globday = day
    print day
    socketio.emit('time', day)

@socketio.on('frame')
def user_video(frame):
    feed = frame  # or, more concisely using with statement
    if feed.startswith('data:'):
        params, data = feed.split(',', 1)
        params = params[5:] or 'text/plain;charset=US-ASCII'
        params = params.split(';')
        if not '=' in params[0] and '/' in params[0]:
            mimetype = params.pop(0)
        else:
            mimetype = 'text/plain'
        if 'base64' in params:
            # handle base64 parameters first
            data = data.decode('base64')
        for param in params:
            if param.startswith('charset='):
                # handle characterset parameter
                data = unquote(data).decode(param.split('=', 1)[-1])
	fh = open("imageToSave.png", "wb")
	fh.write(data)
	fh.close()
	result = imagerectest.get_string("imageToSave.png")
    if result:
        try:
            page = urllib2.urlopen(result)
            # if (page.getcode == 200):
            scraped = textscrape.scrape_text(result, globday, globtime)
            print scraped
            socketio.emit('result', scraped)
        except urllib2.HTTPError as e:
            error_message = e.read()
            print error_message
            socketio.emit('failure', error_message)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, host='0.0.0.0', port=8080)