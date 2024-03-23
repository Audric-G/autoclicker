from tkinter import *
from tkinter import ttk

class KeyboardWindow():
    keys:dict = dict()

    def __init__(self):

        self.root = Tk()
        self.root.attributes("-topmost", True)

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=50, pady=50, sticky=(N, S, E, W))
        
        self.styles = ttk.Style()
        self.styles.configure('TFrame', background='#030232')

        self.root['background']='#030232'

        keys=list("qwertyuiopasdfghjklzxcvbnm")
        self.keyLabels = dict()
        row = 0

        for key in keys:
            if key == 'a' or key == 'z': 
                row += 1
                indexKey = keys.index('a' if 'q' in keys else 'z')
                keys=keys[indexKey:keys.__len__()]

            self.keys[key] = ttk.Label(self.frame, text=key, background='#8f8dff')
            self.keys[key].grid(column=keys.index(key) + row, row=row, sticky=(N, S, E, W), padx=1, pady=1)
            self.keys[key].config(font=("Courier", 44))

        self.root.resizable(False, False)

    def mainloop(self):
        self.root.mainloop()

    @staticmethod
    def OnPress(keystroke):
        key = keystroke[0]

        # if KeyboardWindow.keys[key.name]:
        #     KeyboardWindow.keys[key.name].config(background='#030232')


    @staticmethod
    def OnRelease(keystroke):
        key = keystroke[0]

        # if KeyboardWindow.keys[key.name]:
        #     KeyboardWindow.keys[key.name].config(background='#8f8dff')

        print('"{}" Pressed for {} seconds'.format(key.name, key.timeElapsed))