from BMI_func import *
from fourquestions import *
from welcoming_statement import *
def BMI():
    heightft = int(input("Enter your height (feet): "))
    heightin = int(input("Enter your height (inches): "))
    weight = int(input("Enter your weight (pounds): "))
    height = 0
    greater_than_one(heightft,heightin,weight)
    decimal_calc(heightft,heightin,weight)
    make_sure_the_numbers_are_real(heightft,heightin,weight)
    height = heightft*12 + heightin     
    thisBMI =  round((weight /(height*height)) * 703.06957964,2)
    tell_them_their_BMI(thisBMI)
def questions():
    answer1 = ''
    answer2 = ''
    answer3 = ''
    answer4 = ''
    want = 0
    print("I am about to ask you a list of questions, only answer with yes or no")
    list_of_questions = ["Do you have weak muscles? ","Do you feel tired all the time? ","Do you have a bad mood? ","Do you have an increase in infection or illness "]
    answer1 = input(list_of_questions[0]).lower()
    answer2 = input(list_of_questions[1]).lower()
    answer3 = input(list_of_questions[2]).lower()
    answer4 = input(list_of_questions[3]).lower()
    check_for_valid_answer(answer1,answer2,answer3,answer4)
    yes_or_no_checker(answer1,answer2,answer3,answer4)      
    BMI_checker(answer1,answer2,answer3,answer4,BMI)
