
run = True

while run == True:
    Choose = input("Please choose if you want to findout Distance or Time Or Speed: ")

    if Choose == "Distance":
        T = int(input("Enter a number for Time: "))
        S = int(input("Enter a number for Speed: "))
        sum1 = T * S
        print(sum1)
        run = False

    elif Choose == "Time":
        D = int(input("Enter a number for Distance: "))
        S = int(input("Enter a number for Speed: "))
        sum2 = D / S
        print(sum2)
        run = False
    elif Choose == "Speed":
        D = int(input("Enter a number for Distance: "))
        T = int(input("Enter a number for Time: "))
        sum3 = D / T
        print(sum3)
        run = False

    else:
        print("Please ask a valid option")