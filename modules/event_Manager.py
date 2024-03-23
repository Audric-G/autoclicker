from modules.connection import Connection

class EventManager:
    """
    ### Variables:
    #### event:dict
            Stores events and connections in a dictionary
    ### Methods:
    #### SubscribeTo(event:str, conn:function)
            Subscribe a function to a registered event

    #### RegisterEvent(event:str)
            Registers a new event in the Event Manager

    #### FireEvent(event:str, *args)
            Fires all connections tied to the event given, if any
    """
    event:dict = {
        'OnReady': [],
    }
    ready:bool = False
    
    @classmethod
    def SubscribeTo(self, event:str, conn) -> Connection:
        """Subscribes to an existing event in EventManager, prints err if no event found and returns new Connection object"""
        print('New {} Subscription'.format(event))
        if not event in self.event:
            print("No type found to subscribe to")
        
        newConnection = Connection(conn)

        self.event[event].append(newConnection)
        return newConnection
    
    def __ready__(self):
        self.ready = True
        self.FireEvent('OnReady', self)
    
    @classmethod
    def RegisterEvent(self, event:str):
        """Register an Event to the Instance of Event Manager"""
        print('Added "{}"'.format(event))
        self.event[event] = []

    @classmethod
    def FireEvent(self, event:str, *args):
        """Fire all connections tied to event"""
        for conn in self.event[event]:
            conn.Fire(args)

    @classmethod
    def GetEvents(self):
        return self.event