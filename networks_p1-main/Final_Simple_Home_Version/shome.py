'''
Created on Feb 23, 2021

@author: nigel
'''
from enum import Enum
from pickle import TRUE
import random

class SHome(object):
    '''
    classdocs
    '''
    DSTATE = Enum('DSTATE', {'ON': 'ON', 'OFF': 'OFF' , 'DIM': 'DIM', 'BRIGHT': 'BRIGHT'})
    ALARMSTATE = Enum('ALARMSTATE', {'ARMED': 'ARMED', 'DISARMED': 'DISARMED'})
    LOCKSTATE = Enum('LOCKSTATE', {'OPEN': 'OPEN', 'LOCKED': 'LOCKED'})

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
        self._locks = dict()
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
        self.addLock("Lock 1", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 2", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 3", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 4", [random.randint(1000,9999) for i in range(5)])
        self._devices.append(self._locks)

    def getStatuses(self) -> list:
        ret = []
        i = 1
        for alarm in self._alarm:
            ret.append('{:>3}. {} is {}'.format(i,alarm,self._alarm[alarm].value))
            i += 1
        for light in self._lights:
            ret.append('{:>3}. {} is {}'.format(i,light,self._lights[light].value))
            i += 1
        for lock in self._locks:
            print(self._locks[lock][1])
            ret.append('{:>3}. {} is {}'.format(i,light,self._locks[lock][0].value))
            i += 1
        return ret

    def addLock(self, lockName: str, pin_list: list):
        self._locks[lockName] = [SHome.LOCKSTATE.LOCKED, pin_list]
        

    def getAlarmPassword(self):
        return self._alarmPassword

    def toggleAlarm(self, alarmPass: str):
        if alarmPass == self._alarmPassword:
            alarm = list(self._alarm.keys())[0]
            #print(self._alarm[alarm] == SHome.ALARMSTATE.DISARMED)
            if self._alarm[alarm] == SHome.ALARMSTATE.DISARMED:
                self._alarm[alarm] = SHome.ALARMSTATE.ARMED
                #print(self._alarm)
            else:
                self._alarm[alarm] = SHome.ALARMSTATE.DISARMED

    def getLockPasswordList(self, lockName: str):
        return self._locks[lockName][1]

    def toggleLock(self, lockName: str, lockPass: int):
        print("before if")
        if lockPass in self._locks[lockName][1]:
            print("before if")
            if self._locks[lockName][0] == SHome.LOCKSTATE.LOCKED:
                self._locks[lockName][0] = SHome.LOCKSTATE.OPEN
            else:
                self._locks[lockName][0] = SHome.LOCKSTATE.LOCKED

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
            if isinstance(dev, dict):
                for item in dev:
                    ret.append('{:>3}. {}'.format(i,item))
                    i += 1
            else:
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
        for lock in self._locks:
            ret[str(i)] = lock
            i += 1
        return ret
    