import os
from config.settings import UPLOAD_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER

def ensure_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(ENCRYPTED_FOLDER):
        os.makedirs(ENCRYPTED_FOLDER)
    if not os.path.exists(DECRYPTED_FOLDER):
        os.makedirs(DECRYPTED_FOLDER)
