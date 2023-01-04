import random

#random module has functionality which allows the quiz to generate questions in a random order
#list nested with tuples which store questions and answers for the quiz
questions_answers = [
    ('What is the square root of 9? ', '3'),
    ('How many states are there in USA? ', '50'),
    ('What is the value of 5 squared? ', '25'),
    ('How many days are there in a leap year? ', '366'),
    ('What is 100 + 100 in binary arithmetic? ', '1000'),
    ('How many days does February have in a non leap year? ', '28'),
    ('How many seconds are there in 1 hour? ', '3600'),
    ('How many continents are there? ', '7'),
    ('What is the value of 25 squared? ', '625'),
    ('How many hours are there in 3 days? ', '72'),
]

def greet_user(name):
    '''Displays a simple greeting message for players'''
    print(f'Welcome to this console based quiz {name.title()}!')

def no_of_questions():
    '''Determines how long the quiz will be based on the player's
    choices, up to a maximum of 10 questions'''
    print('The default number of questions for this quiz is 10,'
    '\nhowever you can choose how many questions you want to answer, up to a maximum of 10.')
    #gives the player a choice of taking the default quiz with 10 questions or a custom quiz with
    #the number of questions they want to answer
    number_of_questions = 0
    while True:
        player_choice = input('\nWould you like to play the default quiz'
        ' or a custom quiz? (d for default/c for custom): ')
        if player_choice.lower() == 'd':
            print('\nYou have chosen the default quiz.\nLets begin!')
            number_of_questions = 10
            break
        elif player_choice.lower() == 'c':
            print('\nYou have chosen the custom quiz. You can now choose how many questions you want to answer.'
            '\nPlease note that your response must be greater than 0, and less than or equal to 10')
            number_of_questions = input('\nPlease enter the number of questions you want to answer: ')
            if number_of_questions.isdigit():
                number_of_questions = int(number_of_questions)
            else:
                print('Invalid input, for custom quizzes, please type a number between 0 and 10')
                continue
            if number_of_questions <= 0 or number_of_questions > 10:
                print('Invalid input, for customs quizzes, please type a number between 0 and 10')
                continue
            print(f'\nOkay, your quiz will have {number_of_questions} questions.\nLets begin!')
            break
        else:
            print("Invalid input, please input d for the default quiz, or c for a custom quiz")
            continue
    
    return number_of_questions

def get_question_check_answer():
    '''Retrieves random question from quiz dictionary and displays it to the user
    then prompts for user input. Adjust the score accordingly depending on the user's
    responses'''

    #Declare an empty list variable where the questions that are correctly answered will be stored
    #Incorrectly answered questions will be stored in a separate list, and the correct answers to 
    #the incorrectly answered questions in a separate list
    correct_review = []
    wrong_questions = []
    right_answer = []
    incorrect_review = {}

    #pick questions from the quiz in a random order
    random.shuffle(questions_answers)
    score = 0

    for question in questions_answers[0:quiz_length]:
        user_answer = input(question[0])
        if user_answer == question[1]:
            print('Correct!')
            score += 1
            correct_review.append(question[0])
        else:
            wrong_questions.append(question[0])
            right_answer.append(question[1])
            print('Incorrect')
    
    print("\nYou've reached the end of the quiz!")
    scores_list.append(score)

    #incorrectly answered questions are stored in a dictionary as keys, with the correct answer as a value
    for incorrect_question in range(len(wrong_questions)):
        incorrect_review[wrong_questions[incorrect_question]] = right_answer[incorrect_question]
    
    #at the end of the quiz the user is shown the questions they got correct and the questions they
    #got wrong with the correct answer
    correct = '\n'.join(correct_review)
    incorrect = '\n'.join(f'{q}: The correct answer is {a}' for q, a in incorrect_review.items())
    print(f'\nHere are the questions the questions you got correct\n{correct}')
    print(f'\nHere are the questions you got wrong with the correct answers provided\n{incorrect}')

    return score

def user_name_and_score():
    '''Stores different players names and their scores for the quiz
    in a dictionary. Then displays player scores in descending order, along
    with the average score.'''
    player_scores = {}
    for individual_player in range(len(player_list)):
        player_scores[player_list[individual_player]] = scores_list[individual_player]
    
    sorted_player_scores = sorted(player_scores.items(), key=lambda x:x[1], reverse=True)
    print(f'\nCongratulations to the highest scorer {(sorted_player_scores[0][0]).title()}, with a score of {sorted_player_scores[0][1]}')
    print('\nHere are the player scores in descending order.')
    for player_score in sorted_player_scores:
        print((player_score[0]).title(), player_score[1])
    
    total_score = sum(scores_list)
    total_players = len(player_list)
    average_score = total_score/total_players
    print(f'The average score is {average_score}')

def player_summary():
    '''Displays the final score and percentage score for each individual
    player that plays the quiz.'''
    final_score = get_question_check_answer()
    percentage_score = (final_score/quiz_length) * 100
    print(f'\nYou scored {final_score} out of {quiz_length}')
    print(f'Your percentage score is {round((percentage_score))}%')

#Each player that plays will have their name and score added to the appropriate list
player_list = []
scores_list = []

while True:
    user_name = input('Please enter your name: ')
    #error handling if the user inputs a blank name
    if user_name == '':
        print('Your name cannot be blank, please try again')
        continue

    player_list.append(user_name)
    greet_user(user_name)
    #giving the user an option to not play the quiz and breaking the loop if the answer is no
    playing = input('\nWould you like to play?(y for yes/ n for no): ')
    if playing.lower() == 'n':
        print('Okay, see you next time!')
        break
    
    #error handling for invalid inputs when the user is asked if they want to play the quiz or not
    elif playing.lower() != 'n' and playing.lower() != 'y':
        print('Invalid input, please try again by putting y for yes and n for no')
        continue
    
    #if user decides to play, they're then given the option of how many questions they want to answer,
    #then the quiz runs, keeping a running score
    else:
        quiz_length = no_of_questions()
        player_summary()
        #this function is called because it calls the get_question_check_answer function() within its definition
        #hence the quiz will run by calling the player_summary() function
    
    #giving the option for more users to play and repeating the programme if the answer is yes
    #if the answer is no then display the relevant scores, and the other players' scores
    continue_playing = input('\nWould another player like to play? (y for yes/n for no): ').lower()
    if continue_playing == 'n':
        print('Thanks for playing!')
        user_name_and_score()
        break
    
    elif continue_playing != 'n' and continue_playing != 'y':
        print('Invalid input. Next time please input y if another player is playing or n to quit the quiz')
        print('Thanks for playing!')
        user_name_and_score()
        break

    else:
        continue


#for code in lines 94 - 95 guidance was obtained from
#https://bobbyhadz.com/blog/python-print-each-key-value-pair-of-dictionary-on-new-line#:~:text=join()%20%23-,To%20print%20each%20key%2Dvalue%20pair%20of%20a%20dictionary%20on,string%20of%20key%2Dvalue%20pairs.

#for the code in line 109 guidance was obtained from 
# https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.

#for code in lines 89 - 90 and 106 - 107 guidance was obtained from
#https://datagy.io/python-dictionary-add-items/