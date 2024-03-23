from pynput.keyboard import Key

class Options:
    clickRate:float
    state:bool
    profileKeyUp:list[Key]
    profileKeyDown:list[Key]
    #startRecord:list[Key]
    #endRecord:list[Key]
    exitKey:list[Key]

    def __new__(cls):
        if not hasattr(cls, 'isntance'):
            cls.instance = super(Options, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass

    def ToggleState(self):
        self.state = not self.state