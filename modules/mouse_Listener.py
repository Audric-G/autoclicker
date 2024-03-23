from pynput.mouse import Button, Controller

class MouseListener:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MouseListener, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass

    def StartMouseListener(self):
        pass
    
    