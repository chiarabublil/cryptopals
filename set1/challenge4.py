import challenge3

f=open("challenge4.txt", 'r')
hexs=f.readlines()

max=0
plaintext=""
for hex in hexs:
    s,p,k=challenge3.decodifica(hex)
    if(s>max): 
        max=s
        plaintext=p
print(plaintext)