# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:01:28 2019

@author: hp
"""

from block_cipher_encryption import block_cipher_encrypt
from utility import array_xor

def encrypt(message, expanded_key, number_of_rounds, iv):
    encrypted_text = []
    print('OFB Encrypt')
    for i in range(0, len(message), 16):
        initial = message[i : i + 16]
        block_encypted_text = block_cipher_encrypt(iv, expanded_key, number_of_rounds)           
        block_encypted_text = array_xor(block_encypted_text, initial)
        encrypted_text += block_encypted_text
        iv = block_encypted_text[0:16]

    encrypted_text = [chr(i) for i in encrypted_text]
    return ''.join(encrypted_text)


def decrypt(encrypted_message, expanded_key, number_of_rounds, iv):
    print('OFB Decrypt')
    decrypted_text = []
    for i in range(0, len(encrypted_message), 16):
        initial = encrypted_message[i : i + 16]
        block_decrypted_text = block_cipher_encrypt(iv, expanded_key, number_of_rounds)   
        block_decrypted_text = array_xor(block_decrypted_text, initial)       
        decrypted_text += block_decrypted_text
        iv = initial[0:16]

    decrypted_text = [chr(i) for i in decrypted_text]
    return ''.join(decrypted_text)