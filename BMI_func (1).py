
def greater_than_one(heightft,heightin,weight):
    if heightft == "" or heightin =="":
        print ("Please enter your height.")
        exit()
    if weight == "":
        print ("Please enter your weight.")
        exit()
def decimal_calc(heightft,heightin,weight):
    heightft = float(heightft)
    heightin = float(heightin)
    weight = float(weight)
def make_sure_the_numbers_are_real(heightft,heightin,weight):
    if heightft <0 or heightin <0:
        print ("You cannot possibly have a negative height!")
        exit()
    if heightft < 3:
        print ("Standing " + str(heightft) + " feet tall you must be a child; this is an adult BMI calcuator!")
        exit()
    if heightft > 10:
        print ("Are you really " + str(heightft) + " feet tall ?!")
        exit()
    if heightin > 12:
        print ("Your height in inches shouldn't exceed 12!")
        exit()
    if weight < 0:
        print ("Your weight can only be negative in Theoretical Physics..., NOT in real life.")
        exit()
    if weight  < 30:
        print ("Weighing " + str(weight) + " lbs, you must be a child; this is an adult BMI calcuator!")
        exit()
    if weight > 1500:
        print ("Do you really weigh " + str(weight) + " pounds?!")
        exit()
def tell_them_their_BMI(thisBMI):
    if thisBMI < 18.5: 
        print ("Your BMI is ", thisBMI, " Underweight - eat a pizza!")
    elif  18.5 <= thisBMI <= 24.99:
        print ("Your BMI is ", thisBMI, " - Normal, keep it up!")
    elif  25 <= thisBMI <= 29.99:
        print ("Your BMI is ", thisBMI, " - Overweight, exercise more!")
    elif 30 <= thisBMI <=  39.99:
        print ("Your BMI is ", thisBMI, " - Obese, get off the couch!")
    elif thisBMI >=40:
        print ("Your BMI is ", thisBMI, " - Morbidly Obese - take action!")
    else:
        print("Please check your input values, BMI cannot be calculated.")


