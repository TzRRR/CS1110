"""
Tianze Ren, Feb 2021, the program demonstrates fortune telling ball
"""
from random import randrange
question = input('Please ask a question answered yes or no, enter done to quit: ')
question = question.lower()
while question != 'done':
    if len(question) > 0:
        if question[len(question) - 1] == '?':
            if question.startswith('can') or question.startswith('do')\
                    or question.startswith('can') or question.startswith('will')\
                    or question.startswith('is') or question.startswith('are')\
                    or question.startswith('shall'):
                response_number = randrange(6)
                if response_number == 0:
                    print('It is decidedly so.')
                elif response_number == 1:
                    print('Most definitely.')
                elif response_number == 2:
                    print('Signs point to yes.')
                elif response_number == 3:
                    print('Signs point to no.')
                elif response_number == 4:
                    print('Definitely no.')
                else:
                    print('Not now, not ever, never.')
            else:
                print('The signs are not clear, ask again later.')
        else:
            print('Magic ball has no comment.')
    else:
        print('Nothing in, nothing out.')
    question = input('Please ask a question answered yes or no, enter done to quit: ')
    question = question.lower()