
from enum import Enum
from pickle import TRUE
import random

class SHome(object):
    '''
    classdocs
    '''
    DSTATE = Enum('DSTATE', {'ON': 'ON', 'OFF': 'OFF'})
    ALARMSTATE = Enum('ALARMSTATE', {'ARMED': 'ARMED', 'DISARMED': 'DISARMED'})
    LOCKSTATE = Enum('LOCKSTATE', {'OPEN': 'OPEN', 'LOCKED': 'LOCKED'})
    DIMSTATE = Enum('DIMSTATE', {'DIMMED': 'DIMMED', 'BRIGHT': 'BRIGHT'})
    COLORSTATE = Enum('COLORSTATE', {'WHITE': 'WHITE', 'BLUE': 'BLUE', 'RED': 'RED', 'GREEN': 'GREEN'})

    CRLF = '\r\n'

    def __init__(self):
        '''
        Constructor
        '''
        self._username = 'admin'
        self._password = 'welcome'
        self._users = {self._username : self._password}
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
        
        self.addLock("Lock 1", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 2", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 3", [random.randint(1000,9999) for i in range(5)])
        self.addLock("Lock 4", [random.randint(1000,9999) for i in range(5)])
        self._devices.append(self._locks)


        self.addLight('LR Light 1')
        self.addLight('LR Light 2')
        self.addLight('LR Light 3')
        self.addLight('LR Light 4')
        self.addLight('LR Light 5')
        self.addRoom("Living Room", self._lights)
        self._lights = dict()

        self.addLight('K Light 1')
        self.addLight('K Light 2')
        self.addLight('K Light 3')
        self.addRoom("Kitchen", self._lights)
        self._lights = dict()


        self.addLight('MB Light 1')
        self.addLight('MB Light 2')
        self.addLight('MB Light 3')
        self.addRoom("Master Bedroom", self._lights)
        self._lights = dict()

        self.addLight('O Light 1')
        self.addLight('O Light 2')
        self.addRoom("Office", self._lights)
        self._lights = dict()

        self.addLight('GR Light 1')
        self.addLight('GR Light 2')
        self.addLight('GR Light 3')
        self.addRoom("Guest room", self._lights)
        self._lights = dict()
        

    def getStatuses(self) -> list:
        ret = []
        i = 1
        for alarm in self._alarm:
            ret.append('{:>3}. {} is {}'.format(i,alarm,self._alarm[alarm].value))
            i += 1
    
        #print(self._rooms)
        for room in self._rooms:
            ret.append('{}'.format(room))
            for light in self._rooms[room]:
                ret.append('   {:>3}. {} is {}, {}, and {}'.format(i,light,self._rooms[room][light][0].value
                        , self._rooms[room][light][1].value, self._rooms[room][light][2].value))
                i += 1
        
        for lock in self._locks:
            print(self._locks[lock][1])
            ret.append('{:>3}. {} is {}'.format(i,lock,self._locks[lock][0].value))
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
        if lockPass in self._locks[lockName][1]:
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
    
    def addRoom(self, roomName: str, lightDict: dict):
        self._devices.append(roomName)
        self._rooms[roomName] = lightDict

    def getDevices(self):
        #print("in home getDevices")
        ret = []
        i = 1
        rooms = list(self._rooms.keys())
        #print(rooms)
        #print(self._rooms)
        #print(self._devices)
        for dev in self._devices:
            #print(dev) 
            if isinstance(dev, dict):
                for item in dev:
                    ret.append('{:>3}. {}'.format(i,item))
                    i += 1
            elif dev in rooms:
                ret.append(dev)
                for light in self._rooms[dev]:
                    ret.append('{:>3}. {}'.format(i,light))
                    i +=1
            else:
                ret.append('{:>3}. {}'.format(i,dev))
                i += 1
        return ret

    def addLight(self, lname: str):
        #self._devices.append(lname)
        self._lights[lname] = [SHome.DSTATE.OFF, SHome.DIMSTATE.BRIGHT , SHome.COLORSTATE.WHITE]
    
    def setLightState(self, lname: str, state: str):
        if lname in self._lights:
            self._lights[lname] = SHome.DSTATE[state]
    
    def toggleLightState(self, lname: str):
        for room in self._rooms:
            if lname in self._rooms[room]:
                if self._rooms[room][lname][0] == SHome.DSTATE.OFF:
                    self._rooms[room][lname][0] = SHome.DSTATE.ON
                else:
                    self._rooms[room][lname][0] = SHome.DSTATE.OFF

    def toggleLightDimState(self, lname: str):
        for room in self._rooms:
            if lname in self._rooms[room]:
                if self._rooms[room][lname][1] == SHome.DIMSTATE.BRIGHT:
                    self._rooms[room][lname][1] = SHome.DIMSTATE.DIMMED
                else:
                    self._rooms[room][lname][1] = SHome.DIMSTATE.BRIGHT
    
    def toggleLightColor(self, lname: str, lcolor: str):
        print(lcolor)
        for room in self._rooms:
            if lname in self._rooms[room]:
                self._rooms[room][lname][2] = SHome.COLORSTATE[lcolor]

    def getLightOptions(self, lname: str) -> list:
        lightOptions = []
        i = 0
        rooms = list(self._rooms.keys())
        for room in rooms:
            if lname in  self._rooms[room]:
                lightOptions.append('{:>3}. {}'.format(1, self._rooms[room][lname][i].value))
                i+=1
                lightOptions.append('{:>3}. {}'.format(2, self._rooms[room][lname][i].value))
                i+=1
                lightOptions.append('{:>3}. {}'.format(3, self._rooms[room][lname][i].value))
                i+=1
                break
        return lightOptions

    def getLightOptionsDict(self, lname: str) -> dict:
        lightOptions = {}
        i = 1
        rooms = list(self._rooms.keys())
        for room in rooms:
            if lname in  self._rooms[room]:
                lightOptions[str(i)] = self._rooms[room][lname][0].value
                i+=1
                lightOptions[str(i)] = self._rooms[room][lname][1].value
                i+=1
                lightOptions[str(i)] = self._rooms[room][lname][2].value
                i+=1
                break
        return lightOptions

    def lightColorOptions(self) -> list:
        colorOptions = []
        i = 1
        
        colorOptions.append('{:>3}. {}'.format(i, SHome.COLORSTATE.WHITE.value))
        i+=1
        colorOptions.append('{:>3}. {}'.format(i, SHome.COLORSTATE.BLUE.value))
        i+=1
        colorOptions.append('{:>3}. {}'.format(i, SHome.COLORSTATE.RED.value))
        i+=1
        colorOptions.append('{:>3}. {}'.format(i, SHome.COLORSTATE.GREEN.value))

        return colorOptions

    def getLightColorOptionsDict(self) -> dict:
        colorOptions = {}
        i = 1
        colorOptions[str(i)] =  SHome.COLORSTATE.WHITE.value
        i+=1
        colorOptions[str(i)] =  SHome.COLORSTATE.BLUE.value
        i+=1
        colorOptions[str(i)] =  SHome.COLORSTATE.RED.value
        i+=1
        colorOptions[str(i)] =  SHome.COLORSTATE.GREEN.value
        return colorOptions

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
        y = 1
        for alarm in self._alarm:
            ret[str(i)] = alarm
            i += 1
        for light in self._lights:
            ret[str(i)] = light
            i += 1
        for room in self._rooms:
            ret['Room' + str(y)] = room 
            y += 1
            for light in self._rooms[room]:
                ret[str(i)] = light
                i += 1
        for lock in self._locks:
            ret[str(i)] = lock
            i += 1
        return ret
    