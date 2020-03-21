answer1 = ''
answer2 = ''
answer3 = ''
answer4 = ''
list_of_questions = ["Do you have weak muscles? ","Do you feel tired all the time? ","Do you have a bad mood? ","Do you have an increase in infection or illness "]
answer1 = input(list_of_questions[0])
answer2 = input(list_of_questions[1])
answer3 = input(list_of_questions[2])
answer4 = input(list_of_questions[3])
dict_of_questions = {"Do you have weak muscles?":answer1, "Do you feel tired all the time?": answer2,"Do you have a bad mood?":answer3, "Do you have an increase in infection or illness":answer4}
print(dict_of_questions)