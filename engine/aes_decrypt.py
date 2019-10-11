# -*- coding: utf-8 -*-

from textwrap import wrap

# Used in Round() and serves as the final round during decryption
# SubRoundKey is simply an XOR of a 128-bit block with the 128-bit key.
# So basically does the same as AddRoundKey in the encryption
from aes_helper import * 

def sub_round_key(state, round_key):
    state = [state[i] ^ round_key[i] for i in range(16)]
    return state

# InverseMixColumns uses mul9, mul11, mul13, mul14 look-up tables
# Unmixes the columns by reversing the effect of MixColumns in encryption

def inverse_mix_columns(state):
    tmp = [0 for x in range(16)]

    tmp[0] = mul14[state[0]] ^ mul11[state[1]] ^ mul13[state[2]] ^ mul9[state[3]];
    tmp[1] = mul9[state[0]] ^ mul14[state[1]] ^ mul11[state[2]] ^ mul13[state[3]];
    tmp[2] = mul13[state[0]] ^ mul9[state[1]] ^ mul14[state[2]] ^ mul11[state[3]];
    tmp[3] = mul11[state[0]] ^ mul13[state[1]] ^ mul9[state[2]] ^ mul14[state[3]];

    tmp[4] = mul14[state[4]] ^ mul11[state[5]] ^ mul13[state[6]] ^ mul9[state[7]];
    tmp[5] = mul9[state[4]] ^ mul14[state[5]] ^ mul11[state[6]] ^ mul13[state[7]];
    tmp[6] = mul13[state[4]] ^ mul9[state[5]] ^ mul14[state[6]] ^ mul11[state[7]];
    tmp[7] = mul11[state[4]] ^ mul13[state[5]] ^ mul9[state[6]] ^ mul14[state[7]];

    tmp[8] = mul14[state[8]] ^ mul11[state[9]] ^ mul13[state[10]] ^ mul9[state[11]];
    tmp[9] = mul9[state[8]] ^ mul14[state[9]] ^ mul11[state[10]] ^ mul13[state[11]];
    tmp[10] = mul13[state[8]] ^ mul9[state[9]] ^ mul14[state[10]] ^ mul11[state[11]];
    tmp[11] = mul11[state[8]] ^ mul13[state[9]] ^ mul9[state[10]] ^ mul14[state[11]];

    tmp[12] = mul14[state[12]] ^ mul11[state[13]] ^ mul13[state[14]] ^ mul9[state[15]];
    tmp[13] = mul9[state[12]] ^ mul14[state[13]] ^ mul11[state[14]] ^ mul13[state[15]];
    tmp[14] = mul13[state[12]] ^ mul9[state[13]] ^ mul14[state[14]] ^ mul11[state[15]];
    tmp[15] = mul11[state[12]] ^ mul13[state[13]] ^ mul9[state[14]] ^ mul14[state[15]];

    return tmp;


# Shifts rows right (rather than left) for decryption
def shift_rows(state):
    tmp = [0 for x in range(16)]
    
#	Column 1 
    tmp[0] = state[0];
    tmp[1] = state[13];
    tmp[2] = state[10];
    tmp[3] = state[7];

#	Column 2 
    tmp[4] = state[4];
    tmp[5] = state[1];
    tmp[6] = state[14];
    tmp[7] = state[11];

#	Column 3
    tmp[8] = state[8];
    tmp[9] = state[5];
    tmp[10] = state[2];
    tmp[11] = state[15];

#	Column 4
    tmp[12] = state[12];
    tmp[13] = state[9];
    tmp[14] = state[6];
    tmp[15] = state[3];
    
    return tmp

# Perform substitution to each of the 16 bytes
# Uses inverse S-box as lookup table

def sub_bytes(state):
    state = [inv_s_box[state[i]] for i in range(16)] # Perform substitution to each of the 16 bytes
    return state

#    Each round operates on 128 bits at a time
#    The number of rounds is defined in AESDecrypt()
#    Not surprisingly, the steps are the encryption steps but reversed

def round(state, key):
    state = sub_round_key(state, key)
    state = inverse_mix_columns(state)
    state = shift_rows(state)
    state = sub_bytes(state)
    return state

# Same as Round() but no InverseMixColumns
def initial_round(state, key):
    state = sub_round_key(state, key)
    state = shift_rows(state)
    state = sub_bytes(state)
    return state

# The AES decryption function
# Organizes all the decryption steps into one function
num_of_rounds = 9
def aes_decrypt(encrypted_message, expanded_key):

    state = [int(encrypted_message[i], 16) for i in range(16)] # Stores the first 16 bytes of encrypted message
    state = initial_round(state, expanded_key[10 * 16:]);
    
    
    for i in reversed(range(num_of_rounds)):
        state = round(state, expanded_key[(i + 1) * 16 : (i + 2) * 16])

    state = sub_round_key(state, expanded_key[0:16]); # Final round
    state = [chr(st) for st in state]
    return ''.join(state)

def prepare_decrypt(encrypted_message, key):
    
    key = [int(c, 16) for c in key.split()] 
    if len(key) == 16:
        num_of_rounds = 9
    elif len(key) == 24:
        num_of_rounds = 11
    elif len(key) == 32:
        num_of_rounds = 13 
        
    decrypted_text = ''
    expanded_key = key_expansion(key)    
    encrypted_message = encrypted_message.split()
    
    for i in range(0, len(encrypted_message), 16):
        decrypted_text += aes_decrypt(encrypted_message[i: i + 16], expanded_key)
     
    return decrypted_text;

if __name__ == '__main__':
    key = '01 04 02 03 01 03 04 0A 09 0B 07 0F 0F 06 03 02 01 01 02 02 02 01 01 01'
    file = open('aes.txt', 'r');
    print(prepare_decrypt(file.read(), key))
