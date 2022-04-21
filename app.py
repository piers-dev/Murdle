
# Start with a basic flask app webpage.
from http.client import REQUEST_ENTITY_TOO_LARGE
from flask_socketio import SocketIO, emit, join_room
from flask import Flask, jsonify, redirect, render_template, request, url_for, copy_current_request_context, session
from random import random
from time import sleep
from threading import Thread, Event
import random
import string
from gameclass import *
import uuid

games = {}

__author__ = 'Pixstatic'

app = Flask(__name__)

@app.before_request
def register_session():
    if 'id' in session.keys():
        return
    id = uuid.uuid4().hex
    session['id'] = id
        


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
def connection(msg={}):
    gc = session['code']
    if gc is not None:
        if gc in games.keys():
            if not session['id'] in games[gc].players.keys():
                games[gc].addPlayer(request.sid,session['username'],session['email'],session['id'])
        else:
            games[gc] = gamestate()
            games[gc].addPlayer(request.sid,session['username'],session['email'],session['id'])
    print(games[gc].getPlayers())
    join_room(session['code'])
    emit('updatestate',{'state':games[gc].getPlayers()},room=session['code'])

    

@socketio.on('disconnect', namespace='/game')
def disconnection():
    for player in games[session['code']].players:
        if player['sid'] == request.sid:
            del(player)
    print('Client disconnected')
    emit('updatestate',{'state':games[session['code']].getPlayers()},room=session['code'])

@socketio.on('guess', namespace='/game')
def message(msg):
    print(msg)


if __name__ == '__main__':
    app.secret_key = "vaD3pqokAMbqTvWOgGW7"
    socketio.run(app,host="0.0.0.0",port=8000)

