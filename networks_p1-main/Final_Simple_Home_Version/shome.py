'''
Created on Feb 23, 2021

@author: nigel
'''
from enum import Enum
from pickle import TRUE

class SHome(object):
    '''
    classdocs
    '''
    DSTATE = Enum('DSTATE', {'ON': 'ON', 'OFF': 'OFF' , 'DIM': 'DIM', 'BRIGHT': 'BRIGHT'})
    ALARMSTATE = Enum('ALARMSTATE', {'ARMED': 'ARMED', 'DISARMED': 'DISARMED'})

    CRLF = '\r\n'

    def __init__(self):
        '''
        Constructor
        '''
        self._username = 'admin'
        self._password = 'welcome'
        self._users = dict()
        self._lights = dict()
        self._devices = list()
        self._rooms = dict()
        self._alarm = {'House Alarm': SHome.ALARMSTATE.DISARMED}
        self._alarmPassword = '1234'
        self._devices.append('House Alarm')

        
    def __str__(self) -> str:
        return (SHome.CRLF.join(self.getDevices()))
    
    def mkDummy(self):
        self.addLight('Light 1')
        self.addLight('Light 2')
        self.addLight('Light 3')
        self.addLight('Light 4')
        self.addLight('Light 5')

    def getStatuses(self) -> list:
        ret = []
        i = 1
        for alarm in self._alarm:
            ret.append('{:>3}. {} is {}'.format(i,alarm,self._alarm[alarm].value))
            i += 1
        for light in self._lights:
            ret.append('{:>3}. {} is {}'.format(i,light,self._lights[light].value))
            i += 1
        return ret

    def armAlarm(self, alarmPass: str):
        if alarmPass == self._alarmPassword:
            self._alarm['House Alarm'] = 'ARMED'
    
    def disarmAlarm(self, alarmPass: str):
        if alarmPass == self._alarmPassword:
            self._alarm['House Alarm'] = 'DISARMED'

    def getAlarmPassword(self):
        return self._alarmPassword

    def toggleAlarm(self, alarmPass: str):
        if alarmPass == self._alarmPassword:
            alarm = list(self._alarm.keys())[0]
            print(self._alarm[alarm] == SHome.ALARMSTATE.DISARMED)
            if self._alarm[alarm] == SHome.ALARMSTATE.DISARMED:
                self._alarm[alarm] = SHome.ALARMSTATE.ARMED
                #print(self._alarm)
            else:
                self._alarm[alarm] = SHome.ALARMSTATE.DISARMED

    def addUser(self, u: str, p: str):
        self._users[u] = p

    def checkLogin(self, u: str, p: str) -> bool:
        ret = False
        if u not in self._users:
            return False
        if p == self._users[u]:
            ret = True
        return ret
    
    def getDevices(self):
        #print("in home getDevices")
        ret = []
        i = 1
        for dev in self._devices:
            ret.append('{:>3}. {}'.format(i,dev))
            i += 1
        return ret

    def addLight(self, lname: str):
        self._devices.append(lname)
        self._lights[lname] = SHome.DSTATE.OFF
    
    def setLightState(self, lname: str, state: str):
        if lname in self._lights:
            self._lights[lname] = SHome.DSTATE[state]
    
    def toggleLightState(self, lname: str):
        if lname in self._lights:
            if self._lights[lname] == SHome.DSTATE.OFF:
                self._lights[lname] = SHome.DSTATE.ON
            else:
                self._lights[lname] = SHome.DSTATE.OFF
    
    def getLights(self) -> list:
        ret = []
        i = 1
        for light in self._lights:
            ret.append('{:>3}. {} is {}'.format(i,light,self._lights[light].value))
            i += 1
        return ret
    
    def getDeviceDict(self) -> dict:
        ret = {}
        i = 1
        for alarm in self._alarm:
            ret[str(i)] = alarm
            i += 1
        for light in self._lights:
            ret[str(i)] = light
            i += 1
        return ret
    