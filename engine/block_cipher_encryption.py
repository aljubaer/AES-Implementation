# -*- coding: utf-8 -*-
from aes_helper import *

def sub_bytes(state):
    state = [s_box[state[i]] for i in range(16)]
    return state

def shift_rows(state):
    tmp = [0 for i in range(16)] #create 16 size array
    
    tmp[0] = state[0]
    tmp[1] = state[5]
    tmp[2] = state[10]
    tmp[3] = state[15]
    
    tmp[4] = state[4]
    tmp[5] = state[9]
    tmp[6] = state[14]
    tmp[7] = state[3]
    
    tmp[8] = state[8]
    tmp[9] = state[13]
    tmp[10] = state[2]
    tmp[11] = state[7]
    
    tmp[12] = state[12]
    tmp[13] = state[1]
    tmp[14] = state[6]
    tmp[15] = state[11]
    
    state = tmp
    return state

def mix_columns(state):
    tmp = [0 for i in range(16)] #create 16 size array
    tmp[0] = mul2[state[0]] ^ mul3[state[1]] ^ state[2] ^ state[3]
    tmp[1] = state[0] ^ mul2[state[1]] ^ mul3[state[2]] ^ state[3]
    tmp[2] = state[0] ^ state[1] ^ mul2[state[2]] ^ mul3[state[3]]
    tmp[3] = mul3[state[0]] ^ state[1] ^ state[2] ^ mul2[state[3]]

    tmp[4] = mul2[state[4]] ^ mul3[state[5]] ^ state[6] ^ state[7]
    tmp[5] = state[4] ^ mul2[state[5]] ^ mul3[state[6]] ^ state[7]
    tmp[6] = state[4] ^ state[5] ^ mul2[state[6]] ^ mul3[state[7]]
    tmp[7] = mul3[state[4]] ^ state[5] ^ state[6] ^ mul2[state[7]]

    tmp[8] = mul2[state[8]] ^ mul3[state[9]] ^ state[10] ^ state[11]
    tmp[9] = state[8] ^ mul2[state[9]] ^ mul3[state[10]] ^ state[11]
    tmp[10] = state[8] ^ state[9] ^ mul2[state[10]] ^ mul3[state[11]]
    tmp[11] = mul3[state[8]] ^ state[9] ^ state[10] ^ mul2[state[11]]

    tmp[12] = mul2[state[12]] ^ mul3[state[13]] ^ state[14] ^ state[15]
    tmp[13] = state[12] ^ mul2[state[13]] ^ mul3[state[14]] ^ state[15]
    tmp[14] = state[12] ^ state[13] ^ mul2[state[14]] ^ mul3[state[15]]
    tmp[15] = mul3[state[12]] ^ state[13] ^ state[14] ^ mul2[state[15]]

    state = tmp
    return state

def add_round_key(state, round_key):
    state = [(state[i] ^ round_key[i]) for i in range(16)]
    return state

def round(state, key):
    state = sub_bytes(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, key)
    return state
    
def final_round(state, key):
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key)
    return state

def block_cipher_encrypt(message, expanded_key, num_of_rounds):
    
    state = [message[i] for i in range(16)]
    state = add_round_key(state, expanded_key)
    for i in range(num_of_rounds - 1):
        state = round(state, expanded_key[(i + 1) * 16: (i + 2) * 16])
        
    state = final_round(state, expanded_key[10 * 16: 11 * 16])
    return state
