# SM4 Encryption Tool
from flask import Flask
from flask_cors import CORS
import threading
from routes.file_routes import file_bp
from config.settings import ensure_directories
from ui.backend import backend_ui

app = Flask(__name__)
CORS(app)

ensure_directories()

app.register_blueprint(file_bp)

flask_thread = None

def run_flask():
    app.run(host='0.0.0.0', port=5000)

def start_flask():
    global flask_thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

if __name__ == '__main__':
    start_flask()
    backend_ui()
