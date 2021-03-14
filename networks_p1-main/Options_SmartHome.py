# Lights
class Lights:
    def __init__(self, dim, color):
        self.dim = dim
        self.color = color

    # getter
    def get_dim(self):
        #return print("Value is %" % (self.dim))
        return self.dim

    # setter
    def set_dim(self, d):
        self.dim = d

    def get_color(self):
        #return print("Value is %" % (self.color))
        return self.color
    # setter
    def set_color(self, c):
        self.color = c


# Alarm
class Alarm:
    def __init__(self, state):
        self._state = state

    # getter
    def get_state(self):
        return self._state

    # setter
    def set_state(self, s):
        self._state = s


# Locks (5)
class Locks:
    def __init__(self, lockNum, comb):
        self._lockNum = lockNum
        self._comb = comb

    # getter
    def get_lockNum(self):
        return self._lockNum

    # setter
    def set_lockNum(self, l):
        self._lockNum = l

    def get_comb(self):
        return self._comb

    # setter
    def set_comb(self, c):
        self._comb = c


# SecCam
class SecCam:
    def __init__(self, dim, color):
        self._dim = [20]
        self._color = ""

    # getter
    def get_dim(self):
        return self._dim

    # setter
    def set_dim(self, d):
        self._dim = d

    def get_color(self):
        return self._color

    # setter
    def set_color(self, c):
        self._color = c


# Blinds
class Blinds:
    def __init__(self, dim, color):
        self._dim = [20]
        self._color = ""

    # getter
    def get_dim(self):
        return self._dim

    # setter
    def set_dim(self, d):
        self._dim = d

    def get_color(self):
        return self._color

    # setter
    def set_color(self, c):
        self._color = c
