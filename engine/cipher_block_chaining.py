# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:01:11 2019

@author: hp
"""

from block_cipher_encryption import block_cipher_encrypt
from block_cipher_decryption import block_cipher_decrypt
from utility import array_xor

def encrypt(message, expanded_key, number_of_rounds, iv):
    print('CBC Encrypt')
    encrypted_text = []
    for i in range(0, len(message), 16):
        initial = message[i : i + 16]
        initial = array_xor(iv, initial)
        block_encypted_text = block_cipher_encrypt(initial, expanded_key, number_of_rounds)           
        encrypted_text += block_encypted_text
        iv = block_encypted_text[0:16]

    encrypted_text = [chr(i) for i in encrypted_text]
    return ''.join(encrypted_text)

def decrypt(encrypted_message, expanded_key, number_of_rounds, iv):
    decrypted_text = []
    print('CBC Decrypt')
    for i in range(0, len(encrypted_message), 16):
        initial = encrypted_message[i : i + 16]
        block_decrypted_text = block_cipher_decrypt(initial, expanded_key, number_of_rounds)   
        block_decrypted_text = array_xor(iv, block_decrypted_text)        
        decrypted_text += block_decrypted_text
        iv = initial

    decrypted_text = [chr(i) for i in decrypted_text]
    return ''.join(decrypted_text)
