from flask import Flask
from flask import session
from flask_session import Session
from flask_socketio import SocketIO, emit
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid4().hex
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
socketio = SocketIO(app)

from app import sockets
from app import views  	
