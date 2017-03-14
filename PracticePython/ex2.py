num = int(raw_input('Enter a Number: '))
print ('Odd' if num%2 else 'Even') + ' Number'
print '\r' if num%4 else 'Multiple of 4'
num1 = int(raw_input('Enter 1st Number: '))
num2 = int(raw_input('Enter 2nd Number: '))
if num2 > num1:
    num1,num2 = num2,num1
print str(num1) + ' is not divisible by ' + str(num2) if num1%num2 else str(num1) + ' is divisible by ' + str(num2)
