smallestSoFar = None
print('Before',)
for value in [9, 41, 12, 3, 74, 15] :
    if smallestSoFar is None :
        smallestSoFar = value
    elif value < smallestSoFar :
        smallestSoFar = value
    print(smallestSoFar, value)

print('After' , smallestSoFar)
