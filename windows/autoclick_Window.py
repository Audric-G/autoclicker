#Imports tk, ttk and Window from window
from tkinter import *
from tkinter import ttk

class AutoClickWindow():
    state:bool = False

    def __init__(self):
        super(AutoClickWindow, self).__init__()

        root = Tk()
        self.mainframe = ttk.Frame(root, padding=("3 3 12 12"))
        mainframe = self.mainframe

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.clickRate_Entry = ttk.Entry(mainframe, width=10, textvariable=StringVar()).grid(column=3, row=1, sticky=(W, E))
        self.clickRate_Label = ttk.Label(mainframe, text="()s").grid(column=2, row=1, sticky=W)
        self.state_Label = ttk.Label(mainframe, text="OFF" if not self.state else "ON").grid(column=2, row=2, sticky=W)

        ttk.Label(mainframe, text="Click Rate:").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Current State:").grid(column=1, row=2, sticky=W)

        ttk.Label(mainframe, text="--Controls--------").grid(column=1, row=3)

        ttk.Label(mainframe, text="Activation Key:").grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, text="Toggle Profile Key:").grid(column=1, row=5, sticky=W)
        ttk.Label(mainframe, text="Close Program:").grid(column=1, row=6, sticky=W)

        root.attributes("-topmost", True)
    
    def TestConn(keystroke):
        print("[{}]: Pressed for {} seconds".format(keystroke.key, keystroke.timeElapsed))

    def StartMainLoop(self):
        self.root.mainloop()

