from app import app, socketio

@socketio.on('connect')
def connect():
    session['sid'] = request.sid
