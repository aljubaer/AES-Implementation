# -*- coding: utf-8 -*-

import utility as helper
from aes_helper import key_expansion
import aes_modes

def encrypt(message, key, keylen = 16, save_file_name = 'aes.bin', mode = 'ecb', initial_vector = ''):
    
    message, key, num_of_rounds, iv = helper.initial_process(message, key, keylen, initial_vector)
    expanded_key = key_expansion(key)
#    encrypted_text = electronic_code_book(message, expanded_key)
    aes_mode = aes_modes.get_mode(mode)
    encrypted_text = aes_mode.encrypt(message, expanded_key, num_of_rounds, iv)

    print(encrypted_text)
    print(len(encrypted_text))
    write = open(save_file_name, 'wb+')
    write.write(str.encode(encrypted_text))
    write.close()

if __name__ == '__main__':
    key = 'tahmid khan'
    message = 'Love is tough. If you love someone, she will take you for granted and ignore you a long time.'
    prepare_encryption(message, key, 16, 'aes.bin')