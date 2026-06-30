from flask import Blueprint, request, jsonify, render_template
import os
from datetime import datetime
from services.file_service import FileService
from config.settings import ENCRYPTED_FOLDER, KEYS_FOLDER, DECRYPTED_FOLDER

file_bp = Blueprint('file', __name__)
file_service = FileService()

@file_bp.route('/')
def index():
    return render_template('index.html')

@file_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected'})
    if file:
        success = file_service.save_uploaded_file(file)
        if success:
            return jsonify({'message': 'File uploaded successfully'})
        return jsonify({'message': 'Upload failed'}), 500

@file_bp.route('/files')
def list_files():
    files = file_service.list_encrypted_files()
    return jsonify({'files': files})

@file_bp.route('/decrypt', methods=['POST'])
def decrypt():
    if 'file' not in request.files or 'key' not in request.files:
        return jsonify({'message': 'Missing file or key'}), 400
    file = request.files['file']
    key_file = request.files['key']
    success = file_service.decrypt_file(file, key_file)
    if success:
        return jsonify({'message': 'Decryption successful'}), 200
    return jsonify({'message': 'Decryption failed'}), 500
