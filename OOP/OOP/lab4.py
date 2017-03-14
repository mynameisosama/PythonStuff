import myTime
def getHour(t1, t2):
    return abs(t1.getHours()-t2.getHours())
currentTime = myTime.myTime()
flightTime = myTime.myTime()
currentTime.setHours(14)
flightTime.setHours(16)
print(getHour(currentTime, flightTime))