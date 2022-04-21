
# Start with a basic flask app webpage.
from http.client import REQUEST_ENTITY_TOO_LARGE
from flask_socketio import SocketIO, emit
from flask import Flask, jsonify, redirect, render_template, request, url_for, copy_current_request_context, session
from random import random
from time import sleep
from threading import Thread, Event
import random
import string
from gameclass import *

games = {}

__author__ = 'Pixstatic'

app = Flask(__name__)

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()


        


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@app.route('/game/<string:code>')
def game(code):
    error = request.args.get('invalid')
    return render_template('connect.html',code=code, error=("Please provide a username" if error is not None else ''))

@app.route('/create')
def createGame():
    return redirect(url_for('game',code=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))))

@app.route('/play')
def playredir():
    return redirect(url_for('index'))

@app.route('/play/<string:code>')
def play(code):
    uemail = request.args.get('email')
    uname = request.args.get('user')

    if uname is None:
        return redirect(url_for('game',code=code)+'?invalid=True')

    session['username'] = uname
    session['email'] = uemail
    session['code'] = code

    return render_template('game.html',code=code)

@socketio.on('connect', namespace='/game')
def connect(auth):
    gc = session['code']
    if gc is not None:
        if gc in games.keys():
            games[gc].players.append(player(request.sid,session['username'],session['email']))
        else:
            games[gc] = gamestate(request.sid,session['username'],session['email'])
    emit('test',{'user':session["username"], 'email':session["email"], 'code': gc},room=request.sid)
    print(auth)

    

@socketio.on('disconnect', namespace='/game')
def disconnect():
    print('Client disconnected')

@socketio.on('guess', namespace='/game')
def message(msg):
    print(msg)


if __name__ == '__main__':
    app.secret_key = "vaD3pqokAMbqTvWOgGW7"
    socketio.run(app)