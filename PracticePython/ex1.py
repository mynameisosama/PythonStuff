import datetime

def calculated100YearsFrom(year, age):
    return year + (100-age)

name = raw_input("Enter Name: ")
age = int(raw_input("Enter Current Age: "))

out_msg = name + "!!\nIn " + str(calculated100YearsFrom(datetime.datetime.now().year, age)) + " years you will be 100 years old."
print out_msg
num = int(raw_input("Enter Repeat Count: "))
for i in range(num):
    print out_msg
    
