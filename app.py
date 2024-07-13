import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from encryption_helper import encrypt_message, decrypt_message
from database_helper import save_message, get_last_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfc4768a1b3748c7a3bbfd1e2f91d6f9a8c72b7ed843d8a2'  # Use the generated key

socketio = SocketIO(app)

@app.route('/')
def index():
    last_message = get_last_message()
    if last_message:
        last_message = decrypt_message(last_message)
    return render_template('index.html', last_message=last_message)

@socketio.on('message')
def handle_message(msg):
    encrypted_msg = encrypt_message(msg)
    save_message(encrypted_msg)
    send(encrypted_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
