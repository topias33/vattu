from random import shuffle
import string

game_questions = []
i = 0
answer = ''

def quiz_start(questions, amount = 1):
    questions = questions.split('\n')
    print('all:'+str(questions))
    questions = list(filter(None, questions))
    shuffle(questions)
    global game_questions, i
    try:
        amount = int(amount)
    except:
        amount = 1
    game_questions = questions[:amount]
    print('Questions: ' + str(game_questions))
    i = 0

def quiz_next():
    global game_questions, i, answer
    if i < len(game_questions):
        question, answer = game_questions[i].rsplit(' ? ',1)
        i += 1
        return question
    return ''

def quiz_check(guess):
    whitelist = string.ascii_letters + string.digits + ' '
    global answer
    answer = ''.join(char for char in answer if char in whitelist).lower()
    guess = ''.join(char for char in guess if char in whitelist).lower()
    print('Guess: '+guess+'\nAnswer: '+answer)
    return guess == answer
