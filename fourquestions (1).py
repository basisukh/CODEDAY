
def check_for_valid_answer(answer1,answer2,answer3,answer4):   
    if answer1 == "" or answer2 == "" or answer3 == "" or answer4 == "":
        print("Not valid response for one fo the questions try again. Restart the program and try again.")
        exit()
def yes_or_no_checker(answer1,answer2,answer3,answer4):
    if answer1 == "yes" or answer1 == "no":
        pass
    if answer2 == "yes" or answer2 == "no":
        pass
    if answer3 == "yes" or answer3 == "no":
        pass
    if answer4 == "yes" or answer4 == "no":
        pass
    else:
        print("Some of your answers are invalid, only enter yes or no. The program will now restart.")
def BMI_checker(answer1,answer2,answer3,answer4,BMI):
    if answer1 == "no" and answer2 == "no" and answer2 == "no" and answer3 == "no":
        asks = input("We don't think your suffering from anything. Would you still like us to calculate your BMI? ").lower()
        if asks == "yes":
            BMI()
        if asks == "no":
                exit()
    else:
        print("We have a hunch you could be suffering from something. We would like to calculate your BMI? ")
        BMI()

