import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ENCRYPTED_FOLDER = os.path.join(UPLOAD_FOLDER, 'encrypted')
DECRYPTED_FOLDER = os.path.join(UPLOAD_FOLDER, 'decrypted')
KEYS_FOLDER = os.path.join(BASE_DIR, 'keys')

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

BG_COLOR = '#f0f0f0'
WINDOW_TITLE = 'SM4 Encryption Tool'
WINDOW_SIZE = '1000x600'

TEXT_COLOR = '#4d0000'
BUTTON_COLOR = '#ff6666'
ACCENT_COLOR = '#cc0000'
NAV_BG = '#ffebeb'
NAV_ACTIVE = '#ffcccc'

LISTBOX_WIDTH = 35
LISTBOX_HEIGHT = 15
BUTTON_WIDTH = 18
FONT_NAME = 'Microsoft YaHei'

SM4_KEY_SIZE = 16
MAX_FILE_SIZE = 1024 * 1024 * 100
LOG_LEVEL = 'INFO'
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')

def ensure_directories():
    directories = [
        UPLOAD_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER,
        KEYS_FOLDER, os.path.dirname(LOG_FILE)
    ]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
