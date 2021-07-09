from random import choice, choices
import string
from keyword import kwlist
import re

def crUniqName(nameSequence):
    name = nameSequence[0] + choice(string.ascii_lowercase) + nameSequence[1] + choice(string.ascii_lowercase) + choice(string.ascii_lowercase)

    while name in kwlist:
        name = crUniqName(nameSequence)

    return name

def dcString(sequence):
    line = re.search(r'\^(.+?|.*)\^', sequence).group(1)
    return f'"{line}"'

def dcPunctuation(sequence):
    if sequence[1] == 'c':
        return ':'
    if sequence[1] == 'v':
        return ','

def dcMath(sequence):
    if sequence[-1].isupper():
        sequence = sequence[:-1]
    pythonCode = ''
    for character in sequence[1:]:
        if character == 'e':
            pythonCode += '='
        elif character == 'a':
            pythonCode += '+'
        elif character == 's':
            pythonCode += '-'
        elif character == 'm':
            pythonCode += '*'
        elif character == 'd':
            pythonCode += '/'
        elif character == 'w':
            pythonCode += '//'
        elif character == 'r':
            pythonCode += '%'
        elif character == 'o':
            pythonCode += '**'
        elif character == 'p':
            pythonCode += '('
        elif character == 'q':
            pythonCode += ')'
        else:
            pythonCode += character
    return pythonCode
    

def dcLogic(sequence):
    if sequence[1] == 'e':
        return '=='
    if sequence[1] == 'q':
        return '!='
    if sequence[1] == 'n':
        return 'not'
    if sequence[1] == 'a':
        return 'and'
    if sequence[1] == 'o':
        return 'or'

def dcList(sequence, vrNames):
    # print(f'sequence in decode lib is <{sequence}>')
    pythonCode = '['

    if len(sequence) > 2:

        sequence = sequence.replace(']', '')
        sequence = sequence.replace('[', '')

        splt = sequence.split(',')
        
        for item in splt:
            item = item.strip().replace(',', '')
            pythonCode += decode(item, vrNames)
    else:
        return '[]'
    pythonCode += ']'
    # print(f'returned python code is <{pythonCode}>')
    return pythonCode

def dcDict(sequence):
    pass

def dcTuple(sequence):
    pass

def dcKeyword(sequence):
    if sequence[1] == 'f':
        return 'for'
    if sequence[1] == 'i':
        return 'in'
    if sequence[1] == 's':
        return 'if'
    if sequence[1] == 'e':
        return 'else'
    if sequence[1] == 'l':
        return 'elif'
    if sequence[1] == 'd':
        return 'def'
    if sequence[1] == 'r':
        return 'return'

def dcBuiltinFunction(sequence):
    if sequence[1] == 'e':
        return 'enumerate'
    if sequence[1] == 'c':
        return 'copy.deepcopy'

def dcVarSeq(nameSequence, vrDct):
    
    if nameSequence not in vrDct.keys():
        variableName = crUniqName(nameSequence)
        vrDct[nameSequence] = variableName
    if nameSequence in vrDct.keys():
        variableName = vrDct[nameSequence]

    return variableName

def decode(sequence, vrNames):
    enumSequence = enumerate(sequence)
    pythonCode = ''

    for index, character in enumSequence:

        if character.islower():
            continue

        if character == 'V':
            pythonCode += dcVarSeq(sequence[index + 1:index + 3], vrNames)
        if character == 'N':
            pythonCode += '\n'
        if character == 'M':
            pythonCode += dcMath(re.search('([A-Z]{1}.+?)([A-Z]{1}|.*$)', sequence[index:]).group(0))
        if character == 'S':
            pythonCode += dcString(re.search(r'\^(.+?|.*)\^', sequence[index:]).group(0))

            #This shit below is needed to avoid every character in string line!
            nxt = next(enumSequence)
            while True:
                nxt = next(enumSequence)
                if nxt[1] == '^':
                    break

        if character == 'L':
            pythonCode += dcLogic(sequence[index:index + 2])
        if character == 'W':
            pythonCode += ' '
        if character == 'P':
            pythonCode += dcPunctuation(sequence[index:index + 2])
        if character == 'K':
            pythonCode += dcKeyword(sequence[index:index + 2])
        if character == '[':
            pythonCode += dcList(re.match(r'\[.+\]', sequence[index:]), vrNames)

    return pythonCode