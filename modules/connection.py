class Connection:
    def __init__(self, conn):
        self.Fire = conn

    def Disconnect(self, list):
        if self.conn in list:
            del list[self.conn]
        del self