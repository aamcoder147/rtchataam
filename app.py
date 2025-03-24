from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for testing

# Store connected users (optional)
users = {}

@app.route('/')
def home():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    send(message, broadcast=True)  # Broadcast to all clients

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')  # Use SocketIO's server
