def hex_to_int(hex):
    i=int(hex,16)
    return i

a=hex_to_int('1c0111001f010100061a024b53535009181c')
b=hex_to_int('686974207468652062756c6c277320657965')
print(hex(a^b)[2:])
