'''
Created on Feb 19, 2021

@author: nigel
'''

from message import Message
from shprotocol import SHProtocol
from shome import SHome
import time

class SHServer(object):
    '''
    classdocs
    '''


    def __init__(self, s: SHProtocol):
        '''
        Constructor
        '''
        self._shp = s
        self._login = False
        self._mLevel = 'main'
        self._home = SHome()
        self._home.mkDummy()
        self._debug = True
        
    def _debugPrint(self, m: str):
        if self._debug:
            print(m) 

    def _doLogin(self):
        count = 0
        try:
            while not self._login:
                print("Response")
                ms = Message()
                ms.setType('USER')
                ms.addParam('pnum','1')
                ms.addParam('1','user')
                ms.addLine('Enter your username:')
            
                self._shp.putMessage(ms)
            
                mr = self._shp.getMessage()
                user = mr.getParam('user')
                if not len(user) > 0:
                    ms.reset()
                    ms.setType('ERROR')
                    ms.addParam('pnum','1')
                    ms.addParam('1','error')
                    ms.addLine("Username can't be blank")
                    self._shp.putMessage(ms)
                    time.sleep(1)
                    continue
            

                #print("gahh")
                print("Response")
                ms.reset()
                ms.setType('PASS')
                ms.addParam('pnum','1')
                ms.addParam('1','pass')
                ms.addLine('Enter your password:')

                #print("before put")
                self._shp.putMessage(ms)
                #print("after put")
            
                mr = self._shp.getMessage()
                
                passw = mr.getParam('pass')

                if not len(passw) > 0:
                    ms.reset()
                    ms.setType('ERROR')
                    ms.addParam('pnum','1')
                    ms.addParam('1','error')
                    ms.addLine("Password can't be blank")
                    self._shp.putMessage(ms)
                    time.sleep(1)
                    continue
                
                self._home.addUser(user, passw)

                self._login = self._home.checkLogin(user, passw)
                count = count + 1
                if count > 2:
                    raise Exception('Too many login tries')
                self._mLevel = 'main'
                
        except Exception as e:
            print('doLogin:',e)
            self.shutdown()
        else:
            return
    
    def _doMainMenu(self):
        try:
            
            menu = ['1. List Devices', '2. Display States','3. Change States', '4. Logout']
            choices = {'1': 'list', '2': 'display', '3': 'change', '4': 'logout'}
            ms = Message()
            ms.setType('MENU')
            ms.addParam('pnum','1')
            ms.addParam('1','choice')
            ms.addLine("Enter choice number:")
            ms.addLines(menu)
            
            
            self._shp.putMessage(ms)
            mr = self._shp.getMessage()
            self._debugPrint(mr)
            choice = mr.getParam('choice')
            print(choice, self._mLevel)
            if choice in choices:
                self._mLevel = choices[choice]
            else:
                ms.reset()
                ms.setType('ERROR')
                ms.addParam('pnum','1')
                ms.addParam('1','error')
                ms.addLine("No/Bad choice number entered. Going to main menu")
                self._shp.putMessage(ms)
                self._mLevel = 'main'
            
        except Exception:
            self.shutdown()
        else:
            return
    
    def _doListDevices(self):
        print("list devices")
        try:
            print("here")
            menu = self._home.getDevices()
            #print("here")
            menu.append("Enter choice number:")
            menu.append('{:>3}. Return to Main'.format(99))
            choices = {'99': 'main'}
            ms = Message()
            ms.setType('MENU')
            ms.addParam('pnum','1')
            ms.addParam('1','choice')
            ms.addLines(menu)

            #print(ms)
            
            self._shp.putMessage(ms)
            mr = self._shp.getMessage()
            
            # always go back to main
            self._mLevel = 'main'
                
        except Exception:
            self.shutdown()
        else:
            return
    
    def _doDisplay(self):
        try:
            menu = self._home.getStatuses()
            
            menu.append("Enter choice number:")
            menu.append('{:>3}. Return to Main'.format(99))
            choices = {'99': 'main'}
            ms = Message()
            ms.setType('MENU')
            ms.addParam('pnum','1')
            ms.addParam('1','choice')
            ms.addLines(menu)
            
            self._shp.putMessage(ms)
            mr = self._shp.getMessage()
            
            # always go back to main
            self._mLevel = 'main'
                
        except Exception:
            self.shutdown()
        else:
            return
    
    def _doChange(self):
        try:
            menu = self._home.getStatuses()
            menu.append('{:>3}. Return to Main'.format(99))
            choices = self._home.getDeviceDict()
            #print(choices)
            ms = Message()
            ms.setType('MENU')
            ms.addParam('pnum','1')
            ms.addParam('1','choice')
            ms.addLine("Enter choice number:")
            ms.addLines(menu)
            
            self._shp.putMessage(ms)
            mr = self._shp.getMessage()
            choice = mr.getParam('choice')
            if choice in choices:
                if 'Light' in choices[choice]:
                    self._home.toggleLightState(choices[choice])
                    
                elif choices[choice] == 'House Alarm':
                    #print("here")
                    ms.reset()
                    ms.setType('PASS')
                    ms.addParam('pnum','1')
                    ms.addParam('1','pass')
                    ms.addLine("Enter Alarm 4-digit pin:")
                    self._shp.putMessage(ms)
                    mr = self._shp.getMessage()
                    passw = mr.getParam('pass')
                    #print(passw)
                    if passw == self._home.getAlarmPassword():
                        self._home.toggleAlarm(passw)
                    else:
                        ms.reset()
                        ms.setType('ERROR')
                        ms.addParam('pnum','1')
                        ms.addParam('1','error')
                        ms.addLine("Incorrect pin")
                        self._shp.putMessage(ms)
                        time.sleep(1)

                elif 'Lock' in choices[choice]:
                    ms.reset()
                    ms.setType('PASS')
                    ms.addParam('pnum','1')
                    ms.addParam('1','pass')
                    ms.addLine("Enter Lock 4-digit pin:")
                    self._shp.putMessage(ms)
                    mr = self._shp.getMessage()
                    passw = int(mr.getParam('pass'))
                    lock = choices[choice]
                    if passw in self._home.getLockPasswordList(lock):
                        self._home.toggleLock(lock, passw)
                    else:
                        ms.reset()
                        ms.setType('ERROR')
                        ms.addParam('pnum','1')
                        ms.addParam('1','error')
                        ms.addLine("Incorrect pin")
                        self._shp.putMessage(ms)
                        time.sleep(1)
                    
                self._mLevel = 'change'
            else:
                self._mLevel = 'main'
            
        except Exception:
            self.shutdown()
        else:
            return
    
    def shutdown(self):
        self._login = False
        self._shp.close()  
        return    
        
    def test(self):
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
        
    def run(self):
        try:
            # recv start
            mr = self._shp.getMessage()
            self._debugPrint(mr)
            
            # do login
            self._doLogin()
            self._debugPrint('logged in')
            
            # run the menus
            # a dict with the menu names and the corresponding methods
            menus = {'main': self._doMainMenu,
                     'list': self._doListDevices,
                     'display': self._doDisplay,
                     'change': self._doChange,
                     'logout': self.shutdown}

            while self._login:
                self._debugPrint('menu level='+self._mLevel)
                m = menus[self._mLevel]
                m()

        except Exception as e:
            print('run: shutdown')
            print(e)
            self.shutdown()
        else:
            return
        