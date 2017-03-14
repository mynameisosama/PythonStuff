import datetime

name = raw_input("Enter Name: ")
age = int(raw_input("Enter Current Age: "))

out_msg = name + "!!\nIn the year " + str(datetime.datetime.now().year + (100-age)) + " you will be 100 years old.\n"
print out_msg[0:-1]
num = int(raw_input("Enter Repeat Count: "))
print num*out_msg
