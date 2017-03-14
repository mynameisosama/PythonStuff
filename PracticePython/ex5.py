import random
print [element for element in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if element in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
print [element for element in random.sample(range(50),15) if element in random.sample(range(75),25)]
