def encrypt(message,key):
    c = ''
    hang = len(message) / key
    if hang - int(hang) > 0:
        hang = int(hang) + 1
    hang = int(hang)
    for i in range(key):
        for j in range(hang):
            #check index out of range
            if (i + j*key) >= len(message):
                c += ' ' 
            else:
                c += message[i + j*key]
    print(c)
    return c

def decrypt(c,key):
    m = ''
    hang = len(c) / key
    if hang - int(hang) > 0:
        hang = int(hang) + 1
    hang = int(hang)
    for i in range(hang):
        for j in range(key):
            m += c[j*hang + i]
    print(m)
    return m



if __name__ == '__main__':
    message = 'Common sense is not so common.'
    key = 8
    c = encrypt(message,key)
    decrypt(c,key)