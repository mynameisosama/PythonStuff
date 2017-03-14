class myTime(object):
    def __init__(self, **kwargs):
        self.hour = 0
        self.min = 0
        self.sec = 0
        return super().__init__(**kwargs)
    def setHours(self,hour):
        self.hour = hour
    def getHours(self):
        return self.hour
    def setMinutes(self,min):
        self.min = min
    def getMinutes(self):
        return self.min
    def setSeconds(self,sec):
        self.sec = sec
    def getSeconds(self):
        return self.sec
    def displayTime(self):
        print(str(self.hour) + ":" + str(self.min) + ":" + str(self.sec))