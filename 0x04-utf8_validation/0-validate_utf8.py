#!/usr/bin/python3
'''Utf-8 charachter validation module
'''


def validUTF8(data):
    '''Return true if the data is valid utf8
    else false
    '''
    cnt = 0
    for num in data:
        if cnt == 0:
            if num & 128 == 0:
                cnt = 0
            elif num & 224 == 192:
                cnt = 1
            elif num & 240 == 224:
                cnt = 2
            elif num & 248 == 240:
                cnt = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
            cnt -= 1
    if cnt == 0:
        return True
    return False

