from flask import Flask,render_template
from flask_socketio import SocketIO,send

app=Flask(__name__)
app.config['SECRET']="scecret123"
socketio=SocketIO(app,cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print(message)
    if message!="user connected!":
        send(message,broadcast=True)
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app,host="localhost")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
