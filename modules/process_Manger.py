from multiprocessing import Process
from multiprocessing.managers import BaseManager

class Manager(BaseManager):
    process:dict = dict()
    input:object

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Manager, cls).__new__(cls)
        return cls.instance

    @classmethod
    def SetInput(self, nput):
        self.input = nput

    @classmethod
    def AddProcess(self, target, *args):
        self.process[target] = Process(target=target, args=args)

    @classmethod
    def StartAll(self):
        for p in self.process.values():
            p.start()

    @classmethod
    def KillAllProcess(self):
        for p in self.process.values():
            p.terminate()

    @classmethod
    def JoinAllProcess(self):
        for p in self.process.values():
            p.join()

    @staticmethod
    def register(name, method):
        BaseManager.register(name, method)
