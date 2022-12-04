a = 'a'
print(ord(a)+5)
print(chr(102))

password = 'StopWastingMoney'

def hash(password, key):
    secret = ''
    for i in range(0,len(password)):
        val = ord(password[i])+key
        secret = secret + chr(val)
    return secret

def decrypt(password, key):
    secret = ''
    for i in range(0, len(password)):
        val = ord(password[i]) - key
        secret = secret + chr(val)
    return secret

key = 5
encrypt = hash(password,key)
print("The Hashed Password : ",encrypt)
dec = decrypt(encrypt,key)
print("The Real Password : ",dec)
