import numpy as np
import random

plainTextMessage = "WE ARE DISCOVERED. FLEE AT ONCE"
compositeKey = "1422555515"
polybius = np.array([['E', '2', 'R', 'F', 'Z', 'M'],
                     ['Y', 'H', '3', '0', 'B', '7'],
                     ['O', 'Q', 'A', 'N', 'U', 'K'],
                     ['P', 'X', 'J', '4', 'V', 'W'],
                     ['D', '1', '8', 'G', 'C', '6'],
                     ['9', 'I', 'S', '5', 'T', 'L']])


def getLocationInSquare(letter):
    location = np.where(polybius == letter)
    loc_string = str(location[0][0]) + str(location[1][0])
    loc_int = int(loc_string)
    return loc_int


def oneTimePad(cipher1, key):
    cipher_array = bytearray(cipher1, 'ascii')
    for i in range(len(cipher_array)):
        cipher_array[i] ^= int(key)
    return cipher_array.decode('ascii')


def getColumnarTranspositionKey(compositeKey):
    lst = []
    start = 0
    end = 2
    while end < len(compositeKey):
        lst.append(compositeKey[start:end])
        start += 2
        end += 2
    key = ""
    for pair in lst:
        key += polybius[int(pair[0])][int(pair[1])]
    return key


def getPolybiusStr(plainText):
    cleanedPlainText = ""
    for char in plainText:
        if (char.upper() not in (item for sublist in polybius for item in sublist)):
            continue
        cleanedPlainText = cleanedPlainText + char
    return cleanedPlainText


def encryptWithColumnarTransposition(plainText, key):
    innerCounter = 0
    outerLst = []

    cleanedPlainText = getPolybiusStr(plainText)

    padAmount = 0
    needsPadding = len(cleanedPlainText) % len(key)
    if (needsPadding != 0):
        padAmount = 5
    for i in range(0, padAmount):
        cleanedPlainText = cleanedPlainText + str(random.randrange(0, 10, 1))

    innerLst = []
    for char in cleanedPlainText:
        innerLst.append(char)
        innerCounter = innerCounter + 1
        if (innerCounter >= len(key)):
            outerLst.append(innerLst)
            innerLst = []
            innerCounter = 0

    sortedKey = "".join(sorted(key))
    sortedKeyPairs = []
    for i in range(0, len(sortedKey)):
        sortedKeyPairs.append((sortedKey[i], i, -1))

    newSortedKeyPairs = []

    for i in range(0, len(key)):
        for j in range(0, len(sortedKeyPairs)):
            if key[i] == sortedKeyPairs[j][0]:
                newSortedKeyPairs.append((sortedKeyPairs[j][0], sortedKeyPairs[j][1], i))
                sortedKeyPairs[j] = ("*", sortedKeyPairs[j][1], i)
                break

    sortedKeyPairs = newSortedKeyPairs
    cipherArray = []
    for i in range(0, len(key)):
        cipherArray.append([])

    for i in range(0, len(sortedKeyPairs)):
        text_str = ""
        newIndex = sortedKeyPairs[i][1]
        originalIndex = sortedKeyPairs[i][2]
        for j in range(0, len(outerLst)):
            text_str += outerLst[j][originalIndex]
        cipherArray[newIndex] = text_str
    return ''.join(cipherArray)


def createDecodeMatrix(cybertext, key):
    lenKey = len(key)
    lenTxt = len(cybertext)
    sortedKey = sorted(key)
    try:
        rowsn = int(lenTxt / lenKey)
    except Exception as e:
        print(e)
        return None
    matrix = []

    positionKey = {}
    tempKey = [char for char in key]

    for i in range(lenKey):
        for j in range(lenKey):
            if sortedKey[i] == tempKey[j]:
                tempKey[j] = None
                positionKey[i] = j
                break
    x = 0

    for i in range(rowsn):
        tempArray = []
        temp = x
        for j in range(lenKey):
            tempArray.append(cybertext[temp])
            temp += rowsn
        x += 1

        unsortTempArray = tempArray.copy()
        for j in range(lenKey):
            unsortTempArray[positionKey[j]] = tempArray[j]

        matrix.append(unsortTempArray)
    return matrix


def compressMatrix(matrix):
    string = ''
    for i in matrix:
        for j in i:
            string += j
    return string


print('Plaintext message: {}'.format(plainTextMessage))

key = getColumnarTranspositionKey(compositeKey)
first_encode = encryptWithColumnarTransposition(plainTextMessage, key)
print("First encoding: " + first_encode)

second_encode = oneTimePad(first_encode, compositeKey[-2:])
print("Second encoding: " + second_encode)

first_decoding = oneTimePad(second_encode, compositeKey[-2:])
print("First decoding {}".format(first_decoding))


""" Everything after this point is for the second decryption """
key = getColumnarTranspositionKey(compositeKey)
cybertext = first_encode

sortedKey = sorted(key)

matrix = createDecodeMatrix(cybertext, key)

decoded = compressMatrix(matrix)
print("Second and final Decoding: " + decoded)
