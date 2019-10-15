# -*- coding: utf-8 -*-
from aes_encrypt import encrypt
from aes_decrypt import decrypt

aes_mode = 'cFB'
#aes mode can be cfb, cbc and ecb for now
iv = 'tahmid'

key = 'tahmid khan'
keylen = 32
#this can be 16, 24 or 32
message = 'Self respect is something that you should never lose'
encrypt(message, key, keylen, 'aes.bin', aes_mode, iv)

file = open('aes.bin', 'rb')
print(decrypt(file.read().decode(), key, keylen, 'aes_enrypt.bin', aes_mode, iv))

