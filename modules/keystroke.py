from pynput.keyboard import Key
from datetime import datetime

class Keystroke:
    """
    ### Keystroke:
        Keystroke is a class that keeps time data on each key press, which can be used by other classes
    ### Attributes:
        startTime:time
        timeElapsed:time
        state:bool
        key:Key
    ### Methods:
        EndStroke():
            Immediately called on KeyboardListener's OnRelease event and saves the end time
    """

    def __init__(self, key):
        #print('down')
        self.startTime:datetime = datetime.now()
        self.endTime:datetime
        self.state:bool = True
        self.name:str = str(key).strip('\'')
        self.timeElapsed:datetime

    def EndStroke(self):
        """Returns itself after endstroke is calculated"""
        if not self.state: return self
        #print('up')
        self.endTime = datetime.now()
        self.state = False
        self.timeElapsed = self.endTime - self.startTime
        return self