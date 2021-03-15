'''
Created on Feb 19, 2021

@author: nigel
'''

from message import Message
from shprotocol import SHProtocol

class SHServer(object):
    '''
    classdocs
    '''


    def __init__(self, s: SHProtocol):
        '''
        Constructor
        '''
        self._shp = s
        
    def run(self):
        mr = self._shp.getMessage()
        print(mr)
        
        ms = Message()
        ms.setType('USER')
        ms.addParam('user', 'none')
        ms.addLine('Enter your username:')
        
        self._shp.putMessage(ms)
        
        mr = self._shp.getMessage()
        print(mr)
        
        ms.reset()
        ms.setType('PASS')
        ms.addParam('pass', 'none')
        ms.addLine('Enter your password:')
        
        self._shp.putMessage(ms)
        
        mr = self._shp.getMessage()
        print(mr)

        self._shp.close()
        