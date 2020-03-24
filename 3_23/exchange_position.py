import  math,pyperclip
def main():
    # myMessage = 'Common sense is not so common.'
    # myKey = 8
    # ciphertext = encryptMessage(myKey,myMessage)
    # print(ciphertext + '|')
    # pyperclip.copy(ciphertext)
    #Cenoonommstmme oo snnio. s s c
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8
    plaintext = decryptMessage(myKey,myMessage)
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def encryptMessage(key,Message):
    ciphertext = ['']*key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(Message):
            #这个是 ciphertext[column] 列表添加单个元素
            ciphertext[column] += Message[currentIndex]
            currentIndex += key
    #加密的结尾空格，一个也不打印
    #最后的len() 等于 len(message)
    return ''.join(ciphertext)

def decryptMessage(key,message):
    #???
    numOfColumns = int(math.ceil(len(message) / float(key)))
    #What is ceil?
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = ['']*numOfColumns
    #row 行，column 列
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        #if 的解释
        '''
        明文：             
        1234567
        密文：
        1 4 7
        2 5 *
        3 6 *
        14725*36*
        解密成明文：
        [123] [456] [7**]
        把密文分成
        '''
        if (column == numOfColumns) or (column == numOfColumns - 1 and 
            row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
            print('row: ',row)

    return ''.join(plaintext)

if __name__ == '__main__':
    main()
