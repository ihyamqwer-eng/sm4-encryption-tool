import ctypes
import os

sm4_dll = ctypes.CDLL('./sm4.dll')

sm4_dll.sm4_decrypt_file.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_char_p, ctypes.c_char_p]
sm4_dll.sm4_decrypt_file.restype = ctypes.c_int
sm4_dll.sm4_encrypt_file.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_char_p, ctypes.c_char_p]
sm4_dll.sm4_encrypt_file.restype = ctypes.c_int

def encrypt_file(key, input_file, output_file):
    key_array = (ctypes.c_ubyte * 16)(*key)
    result = sm4_dll.sm4_encrypt_file(key_array, input_file.encode(), output_file.encode())
    return result == 0

def decrypt_file(key, input_file, output_file):
    key_array = (ctypes.c_ubyte * 16)(*key)
    result = sm4_dll.sm4_decrypt_file(key_array, input_file.encode(), output_file.encode())
    return result == 0
