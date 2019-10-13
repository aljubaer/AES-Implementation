# -*- coding: utf-8 -*-

# Used in Round() and serves as the final round during decryption
# SubRoundKey is simply an XOR of a 128-bit block with the 128-bit key.
# So basically does the same as AddRoundKey in the encryption
import utility as helper
from aes_helper import key_expansion
import aes_modes


def decrypt(encrypted_message, key, keylen = 16, save_file_name = 'aes_decrypt.txt', mode = 'ecb', initial_vector = ''):
    encrypted_message, key, num_of_rounds, iv = helper.initial_process(encrypted_message, key, keylen, initial_vector)
      
    expanded_key = key_expansion(key)    
    
    aes_mode = aes_modes.get_mode(mode)
    decrypted_text = aes_mode.decrypt(encrypted_message, expanded_key, num_of_rounds, iv)
    write = open(save_file_name, 'w+')
    write.write(decrypted_text)
    write.close()
    print('Result')
    return decrypted_text

if __name__ == '__main__':
    key = 'tahmid khan'
    file = open('aes.bin', 'rb')
    print(prepare_decryption(file.read().decode(), key))
