'''
Created on Feb 19, 2021

@author: nigel
'''

from message import Message
from shprotocol import SHProtocol

class SHClient(object):
    '''
    classdocs
    '''


    def __init__(self, s: SHProtocol):
        '''
        Constructor
        '''
        self._shp = s
        
    def run(self):
        ms = Message()
        ms.setType('START')
        
        self._shp.putMessage(ms)
        
        mr = self._shp.getMessage()
        print(mr.getBody())
        
        choice = input('-->')
        ms.reset()
        ms.setType('CHOICE')
        ms.addParam('user', choice)
         
        self._shp.putMessage(ms)
        
        mr = self._shp.getMessage()
        print(mr.getBody())
        
        choice = input('-->')
        ms.reset()
        ms.setType('CHOICE')
        ms.addParam('pass', choice)
         
        self._shp.putMessage(ms)
        
        self._shp.close()
        