import string
message = 'DO YOU LOVE ME?'
LETTERS = string.ascii_uppercase

for key  in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            #为什么是减
            num -= key
            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
    # else:
    translated += symbol
    print('Key #%s: %s' %(key,translated))    
