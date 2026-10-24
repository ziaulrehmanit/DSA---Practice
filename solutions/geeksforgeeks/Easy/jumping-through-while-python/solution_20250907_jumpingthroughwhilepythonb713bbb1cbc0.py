def printIncreasingPower(x):
    number = 1
    square = 1
    while(square<=x):
        square = number*number
        if square<=x:
            print (square, end = " ")
        number+=1
