'''
Created on Feb 17, 2021

@author: nigel
'''

from enum import Enum


class Message(object):
    '''
    classdocs
    '''
    # Constance
    MCMDS = Enum('MCMDS', {'START': 'START', 'USER': 'USER', 'PASS': 'PASS',
                           'MENU': 'MENU', 'CHOICE': 'CHOICE', 'ERROR': 'ERROR'})
    CRLF = '\r\n'
    SPACE = ' '
    PJOIN = '&'
    VJOIN = '{}={}'
    VJOIN1 = '='

    def __init__(self):
        '''
        Constructor
        '''
        self._type = Message.MCMDS.START
        self._params = {'lines': '0'}
        self._body = []
        self._bodyLines = 0

    def __str__(self) -> str:
        '''
        Stringify - marshal
        '''
        return self.marshal()

    def setType(self, mtype: str):
        self._type = Message.MCMDS[mtype]

    def getType(self) -> str:
        return self._type.value()

    def addParam(self, name: str, value: str):
        self._params[name] = value;

    def getParam(self, name: str) -> str:
        return self._params[name]

    def addLine(self, line: str):
        self._body.append(line)
        self._bodyLines += 1

    def addLines(self, lines: list):
        for line in lines:
            self.addLine(line)

    def getBody(self) -> str:
        return Message.CRLF.join(self._body)

    def marshal(self) -> str:
        self._params['lines'] = str(self._bodyLines)

        value = [self._type.value]
        pairs = [Message.VJOIN.format(k, v) for (k, v) in self._params.items()]
        params = Message.PJOIN.join(pairs)
        value.append(params)
        if len(self._body) > 0:
            value += self._body
        return Message.CRLF.join(value)

    def unmarshal(self, value: str):
        self._params.clear()
        self._body.clear()
        lines = value.split(Message.CRLF)
        self._type = Message.MCMDS[lines[0]]
        params = lines[1].split(Message.PJOIN)
        for p in params:
            k, v = p.split(Message.VJOIN1)
            self._params[k] = v
        self._body += lines[2:]
        self._bodyLines = int(self._params['lines'])


