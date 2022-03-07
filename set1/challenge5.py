def getBytes(str):
    bs=[]
    for b in bytes(str, 'UTF-8'):
        bs.append(b)
    return bs

plaintext=getBytes("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
key=getBytes("ICE")

c=""
for i in range(len(plaintext)):
    result=hex(plaintext[i]^key[i%3])[2:]
    if len(result)==1: result='0'+result
    c+=result

print(c)