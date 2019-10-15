# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:03:35 2019

@author: hp
"""

def adjust_size(key, length): #key is a string
    if len(key) < length:
        return key + ''.join([chr(0) for i in range(length - len(key))])
    return key[0:length]



def get_number_of_rounds(keylen):
    keylen_vs_rounds = {}
    keylen_vs_rounds[16] = 10
    keylen_vs_rounds[24] = 12
    keylen_vs_rounds[32] = 14
    return keylen_vs_rounds[keylen]

def convert_char_array_to_int_array(arr):
    return [ord(i) for i in arr]

def array_xor(arr1, arr2):
    return [arr1[i] ^ arr2[i] for i in range(len(min(arr1, arr2)))]

def initial_process(message, key, keylen, iv):
    while len(message) % 16 != 0:
        message += chr(0)
    key = adjust_size(key, keylen)
    key = convert_char_array_to_int_array(key)
    num_of_rounds = get_number_of_rounds(len(key))
    
    iv = adjust_size(iv, 16)
    iv = convert_char_array_to_int_array(iv)
    message = [ord(i) for i in message]
    return message, key, num_of_rounds, iv