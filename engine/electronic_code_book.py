# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:12:32 2019

@author: hp
"""

from block_cipher_encryption import block_cipher_encrypt
from block_cipher_decryption import block_cipher_decrypt

def encrypt(message, expanded_key, number_of_rounds, iv = ''):
    encrypted_text = []
    for i in range(0, len(message), 16):
        encrypted_text += block_cipher_encrypt(message[i: i + 16], expanded_key, number_of_rounds)
    
    encrypted_text = [chr(i) for i in encrypted_text]
    return ''.join(encrypted_text)

def decrypt(encrypted_message, expanded_key, number_of_rounds, iv = ''):
    decrypted_text = []  
    for i in range(0, len(encrypted_message), 16):
        decrypted_text += block_cipher_decrypt(encrypted_message[i: i + 16], expanded_key, number_of_rounds)
     
    decrypted_text = [chr(i) for i in decrypted_text]
    return ''.join(decrypted_text)
