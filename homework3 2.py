#!/usr/bin python
def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        keta = 0.1
        index += 1
        while index < len(line) and line[index].isdigit():
            number += keta* int(line[index])
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMINUS(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type':'MULTIPLY'}
    return token, index + 1

def readDivision(line, index):
    token = {'type':'DIVISION'}
    return token, index + 1



def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            token, index = readNumber(line, index)
        elif line[index] == '+':
            token, index = readPlus(line, index)
        elif line[index] == '-':
            token, index = readMINUS(line, index)
        elif line[index] == '*':
            token, index = readMultiply(line, index)
        elif line[index] == '/':
            token, index = readDivision(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def evaluate(tokens):
    index = 0
    answer = tokens[index]['number']
    index += 1
    while index < len(tokens):
        #print 1
        while tokens[index]['type'] == 'NUMBER'or tokens[index - 1]['type'] == 'DIVISION':
            if tokens[index - 1]['type'] == 'DIVISION':
                answer *= tokens[index]['number']
            elif tokens[index - 1]['type'] == 'DIVISION':
                answer /= tokens[index]['number']
            elif:
                 print 'Invalid syntax'
           index += 1
        return answer
            
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    print tokens
    answer = evaluate(tokens)
    print "answer = %d" % answer
