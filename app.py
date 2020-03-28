from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, emit
from sys import stderr

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials. Please try again."

    return render_template('login.html', error=error)


## For PONG
@app.route('/pong')
def pong():
    return render_template('pong.html')


@socketio.on("move", namespace="/pong")
def move(displacement):
    global pos
    pos += displacement
    print(pos, file=stderr)
    emit('move', pos)

pos = 0
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)