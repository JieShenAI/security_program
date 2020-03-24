def encrpt(s,k):
    # s = s.lower()
    result = []
    for item in s:
        if item >= 'a' and item <= 'z':
            result.append(chr((ord(item)+k-ord('a'))%26 + ord('a')))
        else:
            result.append(item)
    return ''.join(result)

if __name__ == '__main__':
    s = 'abc'
    res = encrpt(s,1)
    print(res)