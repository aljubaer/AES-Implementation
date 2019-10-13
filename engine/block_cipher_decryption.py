# -*- coding: utf-8 -*-

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

    tmp[0] = mul14[state[0]] ^ mul11[state[1]] ^ mul13[state[2]] ^ mul9[state[3]]
    tmp[1] = mul9[state[0]] ^ mul14[state[1]] ^ mul11[state[2]] ^ mul13[state[3]]
    tmp[2] = mul13[state[0]] ^ mul9[state[1]] ^ mul14[state[2]] ^ mul11[state[3]]
    tmp[3] = mul11[state[0]] ^ mul13[state[1]] ^ mul9[state[2]] ^ mul14[state[3]]

    tmp[4] = mul14[state[4]] ^ mul11[state[5]] ^ mul13[state[6]] ^ mul9[state[7]]
    tmp[5] = mul9[state[4]] ^ mul14[state[5]] ^ mul11[state[6]] ^ mul13[state[7]]
    tmp[6] = mul13[state[4]] ^ mul9[state[5]] ^ mul14[state[6]] ^ mul11[state[7]]
    tmp[7] = mul11[state[4]] ^ mul13[state[5]] ^ mul9[state[6]] ^ mul14[state[7]]

    tmp[8] = mul14[state[8]] ^ mul11[state[9]] ^ mul13[state[10]] ^ mul9[state[11]]
    tmp[9] = mul9[state[8]] ^ mul14[state[9]] ^ mul11[state[10]] ^ mul13[state[11]]
    tmp[10] = mul13[state[8]] ^ mul9[state[9]] ^ mul14[state[10]] ^ mul11[state[11]]
    tmp[11] = mul11[state[8]] ^ mul13[state[9]] ^ mul9[state[10]] ^ mul14[state[11]]

    tmp[12] = mul14[state[12]] ^ mul11[state[13]] ^ mul13[state[14]] ^ mul9[state[15]]
    tmp[13] = mul9[state[12]] ^ mul14[state[13]] ^ mul11[state[14]] ^ mul13[state[15]]
    tmp[14] = mul13[state[12]] ^ mul9[state[13]] ^ mul14[state[14]] ^ mul11[state[15]]
    tmp[15] = mul11[state[12]] ^ mul13[state[13]] ^ mul9[state[14]] ^ mul14[state[15]]

    return tmp


# Shifts rows right (rather than left) for decryption
def shift_rows(state):
    tmp = [0 for x in range(16)]
    
#	Column 1 
    tmp[0] = state[0]
    tmp[1] = state[13]
    tmp[2] = state[10]
    tmp[3] = state[7]

#	Column 2 
    tmp[4] = state[4]
    tmp[5] = state[1]
    tmp[6] = state[14]
    tmp[7] = state[11]

#	Column 3
    tmp[8] = state[8]
    tmp[9] = state[5]
    tmp[10] = state[2]
    tmp[11] = state[15]

#	Column 4
    tmp[12] = state[12]
    tmp[13] = state[9]
    tmp[14] = state[6]
    tmp[15] = state[3]
    
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
def block_cipher_decrypt(encrypted_message, expanded_key, num_of_rounds):

    state = [encrypted_message[i] for i in range(16)] # Stores the first 16 bytes of encrypted message
    state = initial_round(state, expanded_key[10 * 16:])
    
    
    for i in reversed(range(num_of_rounds - 1)):
        state = round(state, expanded_key[(i + 1) * 16 : (i + 2) * 16])

    state = sub_round_key(state, expanded_key[0:16]) # Final round
    return state
