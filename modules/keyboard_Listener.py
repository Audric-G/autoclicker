from pynput.keyboard import Key, Listener
from modules.keystroke import Keystroke
from modules.event_Manager import EventManager

class KeyboardListener(EventManager):
    keysDown:dict = {}
    state:bool = False
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(KeyboardListener, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.RegisterEvent("OnPress")
        self.RegisterEvent("OnRelease")
        self.__ready__()
    
    def StartKeyboardListener(self):
        self.state=True

        with Listener(
            on_press=self.__OnPress__,
            on_release=self.__OnRelease__) as listener:
            self.listener=listener
            self.listener.join()

    def __OnPress__(self, key:Key) -> None:
        if self.keysDown.get(key) or not self.state: return

        self.keysDown[key] = Keystroke(key)
        self.FireEvent("OnPress", self.keysDown[key])

    def __OnRelease__(self, key:Key) -> None:
        # Return if key is not in keysDown, allowing keys in mid-press to finish when listener state is off but stopping any further listening.
        if not self.keysDown.get(key): return

        self.FireEvent("OnRelease", self.keysDown[key].EndStroke())
        self.keysDown.pop(key)

    def GetKeysDown(self) -> dict:
        return self.keysDown