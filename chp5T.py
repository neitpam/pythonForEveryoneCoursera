smallest = None
largest = None

while True :
    try:
        num = input ("Enter a number: ")
        if num == "done":
                break
        if largest is None:
            largest = int(num)
        if int(num) > largest:
            largest = int(num)
        if smallest is None:
            smallest = int(num)
        if int(num) < smallest:
            smallest = int(num)

    except:
        print('Invalid input')

    #print (num)
    

print ('Maximum is', largest)
print ('Minimum is', smallest)
