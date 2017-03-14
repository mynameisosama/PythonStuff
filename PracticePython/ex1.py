import datetime

def calculated100YearsFrom(year, age):
    return int(year) + (100-int(age))

name = raw_input("Enter Name: ")
age = raw_input("Enter Current Age: ")

print name + "!!"
print "In " + str(calculated100YearsFrom(datetime.datetime.now().year, age)) + " years you will be 100 years old."

    
