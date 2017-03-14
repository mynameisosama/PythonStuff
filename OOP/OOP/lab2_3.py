def addMultiplesOfFive(array):
    return sum([element for element in array if element%5==0])
print(addMultiplesOfFive([1, 4, 10, 12, 15, 20, 22]))