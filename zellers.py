def calculateDayofTheWeek(day, month, year, century):
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    W = (13*month - 1) / 5
    X = year/4
    Y = century/4
    Z = W+X+Y+day+year-(2*century)
    R = Z % 7

    print days[R]

def clean_data(data):
    day = (int(data[0])*10) + int(data[1])
    month = (int(data[3])*10) + int(data[4])
    century = (int(data[6])*10) + int(data[7])
    year = (int(data[8])*10) + int(data[9])

    if month < 3:
        month+=10
        if year == 0:
            year = 99
            century -=1
    else:
        month-=2

    calculateDayofTheWeek(day, month, year, century)
    
date = raw_input("Enter any date you like and I'll tell you the day of the week it is/was/will be (dd/mm/yyyy): ")
clean_data(date)
