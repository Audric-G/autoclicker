
from modules.keyboard_Listener import KeyboardListener
from modules.process_Manger import Manager

from windows.keyboard_Window import KeyboardWindow
kbdWindow = KeyboardWindow()

def StartManager() -> Manager:
    Manager.register('KeyboardListener', KeyboardListener)
    
    manager:Manager = Manager()
    manager.start()

    input = manager.KeyboardListener()
    input.SubscribeTo('OnPress', kbdWindow.OnPress)
    input.SubscribeTo('OnRelease', kbdWindow.OnRelease)

    manager.AddProcess(input.StartKeyboardListener)
    manager.StartAll()

    return manager

def StartWindow():
    kbdWindow.mainloop()

def main():
    manager = StartManager()
    StartWindow()

    ##EOF Cleanup
    manager.KillAllProcess()
    manager.shutdown()

if __name__ == "__main__": 
    main()