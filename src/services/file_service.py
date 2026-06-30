import os
from datetime import datetime
from utils.sm4_utils import decrypt_file
from config.settings import ENCRYPTED_FOLDER, KEYS_FOLDER, DECRYPTED_FOLDER

class FileService:
    def save_uploaded_file(self, file):
        try:
            filename = os.path.join(ENCRYPTED_FOLDER, file.filename)
            file.save(filename)
            return True
        except Exception as e:
            print(f'Save failed: {str(e)}')
            return False

    def list_encrypted_files(self):
        try:
            return os.listdir(ENCRYPTED_FOLDER)
        except Exception as e:
            print(f'List files failed: {str(e)}')
            return []

    def decrypt_file(self, file, key_file):
        try:
            file_path = os.path.join(ENCRYPTED_FOLDER, file.filename)
            key_path = os.path.join(KEYS_FOLDER, key_file.filename)
            file.save(file_path)
            key_file.save(key_path)
            with open(key_path, 'rb') as f:
                key = f.read()
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            output_path = os.path.join(DECRYPTED_FOLDER, f'decrypted_{timestamp}_{file.filename}')
            return decrypt_file(key, file_path, output_path)
        except Exception as e:
            print(f'Decrypt failed: {str(e)}')
            return False
