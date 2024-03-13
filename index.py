from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

from time import sleep
from threading import Thread, Event

mouse = Controller()

event = Event()
thread = Thread(target=(lambda x: x))
state = False

activateKey = Key.tab
escapeKey = Key.esc
changeRateKey = Key.up

class rate:
    long = 60
    short = 1
    fast = .5
    rapid = .1
    auto = .05

currentRate = rate.long

print("Gieven's Autoclicker\nTab: Start/Stop\nUp Arrow: Toggle Speed (60s or 1s cooldown, default 60s)\nEsc: End Program")
print("__________________________________________")

def main():
    global thread

    thread = getThread()
    thread.start()

    #waits for thread to end before terminating 
    thread.join

##========================================================================================
##OPTIONS
##========================================================================================
def changeRate():
    global currentRate
    global state

    currentRate = rate.long if currentRate == rate.short else rate.short

    print("Changed Click Rate: {}".format(currentRate))
    
    if state:
        restartThread()
##========================================================================================
##THREADING
##========================================================================================
def getThread():
    return Thread(target=task)

def startThread():
    global thread
    global event

    if thread.is_alive():
        endThread()

    main()

##Probably the weirdest way to do this but whatever
def restartThread():
    toggleState()
    toggleState()

def endThread():
    global thread
    global event

    event.set()

    while thread.is_alive():
        sleep(rate.fast)

def toggleState():
    global state

    state = not state
    print('Changed State: {}'.format("Running" if state == True else "Stopped"))

    if state:
        startThread()
    else:
        #state is false, terminate running thread
        endThread()

def task():
    global state
    global currentRate
    global event

    while state:
        mouse.click(Button.left, 1)
        for i in range(currentRate*2):
            sleep(.5)
            if event.is_set():
                state = False
                event.clear()
                break

##========================================================================================
##INPUT
##========================================================================================
def on_press(key):
    global activateKey
    global changeRateKey

    if key == activateKey:
        toggleState()
    if key == changeRateKey:
        changeRate()

def on_release(key):
    global escapeKey

    if key == escapeKey:
        endThread()
        print("Exiting Program")
        return False

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()