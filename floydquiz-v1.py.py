'''
This quiz is another small test project to further my skills.
It's a Pink Floyd themed quiz containing 10 questions.
It includes some easter eggs if the user name is one of the 5 Floyd members.
Each question has a personalized correct/wrong answer.
'''

import time

# this segment is assigning bot name and introducing the player

bot_name = 'FloydBot'

print(f'\n{bot_name}: Welcome to the ultimate Pink Floyd quiz!')
time.sleep(1)
print(f'{bot_name}: Test your knowledge, answer 10 questions, and find out if you\'re a true Pink Floyd fan!')
time.sleep(2)
print(f'\n{bot_name}: First off, what is your name?')

you = ('You: ')
name = input(you).strip().capitalize()

time.sleep(0.3)
print()

# this segment is a little easter egg if the user's name is the same as any of the band members

if name.lower() == 'roger':
    print(f'{bot_name}: Whoa... *The* Roger Waters? Nice.')
elif name.lower() == 'david':
    print(f'{bot_name}: Mr. David Gilmour in the house??')
elif name.lower() == 'nick':
    print(f'{bot_name}: Welcome back from Pompeii, Mr. Mason')
elif name.lower() == 'rick':
    print(f'{bot_name}: Rick Wright? Lowkey the best musician in the band..')
elif name.lower() == 'syd':
    print(f'{bot_name}: The madman himself *laughs in madcap*')
else:
    print(f'{bot_name}: It\'s nice to meet you {name}!')

time.sleep(1.5)
print(f'{bot_name}: {name}, are you ready to begin?')

# this while segment will get the user pumped and ready for the quiz
while True:
    ready = input(you).lower()
    
    if ready == 'yes':
        time.sleep(0.5)
        print(f'\n{bot_name}: Great! Let\'s begin!')
        time.sleep(1.5)
        break
    else:
        time.sleep(0.5)
        print(f'\n{bot_name}: Huh, guess you listen to  Taylor Swift then... I said ARE. YOU. READY?!')

# dictionary with all the questions and answers
questions_dict = {
    'q1': {
        'text': 'What year was the Dark Side of the Moon released?',
        'answer': ['1973', 'in 1973', 'in \'73', '\'73', '73'],
        'correct_reaction': 'Good job! If you got that wrong, I would have quit right there and then...',
        'wrong_reaction': 'Damn... Not off to a good start dude...'
        },
    'q2':{
        'text': 'What song features the lyrics "If you should go skating"',
        'answer': ['thin ice', 'the thin ice'],
        'correct_reaction': 'Good job! Let\'s keep going',
        'wrong_reaction': 'Go listen to The Wall again...'
         },
    'q3':{
        'text': 'Which Pink Floyd album starts and ends with a heartbeat?',
        'answer': ['dsotm', 'dsom', 'dark side', 'dark side of the moon', 'the dark side of the moon'],
        'correct_reaction': 'This one was a no-brainer, let\'s keep going!',
        'wrong_reaction': '*rolls eyes*'
          },
    'q4':{
        'text': 'What was the original name of the band before Pink Floyd?',
        'answer': ['tea set', 'the tea set'],
        'correct_reaction': 'Hell yeah! You really know your stuff!',
        'wrong_reaction': 'This one was a little tougher, I don\'t blame you.'
          },
    'q5':{
        'text': 'During the recording of The Wall, which member was nearly fired?',
        'answer': ['rick', 'rick wright', 'wright'],
        'correct_reaction': 'Thank God they kept our man Rick for the gem that is this album.',
        'wrong_reaction': 'Ugh, wrong...'
          },
    'q6':{
        'text': 'Which album features the song "If"?',
        'answer': ['ahm', 'atom heart mother'],
        'correct_reaction': 'Good job! You have good taste too.',
        'wrong_reaction': 'Casual...'
          },
    'q7':{
        'text': 'What instrument opens the album Wish You Were Here?',
        'answer': ['synth', 'strings', 'synth strings', 'synthesizer', 'keyboard', 'keyboards', 'moog'],
        'correct_reaction': 'Great job! You must be a musician.',
        'wrong_reaction': 'Bruh... Check this link for future reference - www.google.com/what-is-an-instrument'
          },
    'q8':{
        'text': 'What\'s the name of the guitar effect used by Gilmour to create the seagull-like sounds in Echoes?',
        'answer': ['wah', 'wah wah', 'wah pedal', 'reverse wah', 'reverse wah pedal'],
        'correct_reaction': 'Thank God the tech hooked up his wah pedal in reverse that one day',
        'wrong_reaction': 'Guess you missed Floyd live at Pompeii last month.'
          },
    'q9':{
        'text': 'What song features a hidden message when played backwards?',
        'answer': ['empty spaces'],
        'correct_reaction': 'Correct! We\'re almost there, keep going!',
        'wrong_reaction': 'Pathetic...'
          },
    'q10':{
        'text': 'On what tour did Roger Waters spit on a fan?',
        'answer': ['animals tour', 'animal instincts', '\'77', 'animals', 'montreal', 'in montreal', '1977'],
        'correct_reaction': 'Yes! Specifically on the Animals Tour at a Montreal show.',
        'wrong_reaction': 'I\'d say you were the fan he spat on, but you got it wrong.'
          },
}

score = 0

# the for loop for going through each question, it will refer to the dictionary for the question, answer and correct/incorrect response.

for question_num, question_info in questions_dict.items():
    print(f'\n{bot_name}: {question_info["text"]}')
    user_input = input(you).lower()
    time.sleep(1)
    if user_input in question_info['answer']:
        print(f'\n{bot_name}: {question_info["correct_reaction"]}')
        score += 1
    else:
        print(f'\n{bot_name}: {question_info["wrong_reaction"]}')
    time.sleep(1.5)

print(f'\n{bot_name}: Calculating your final score...')
time.sleep(1.5)
print('==========================================')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')

if score == 10:
    print(f'\n{bot_name}: {name}..., your final score is {score}/10! You absolutely crushed it! You should be proud of yourself.')
elif score >= 8:
    print(f'\n{bot_name}: Great job {name}, your final score is {score}/10! You\'re a true Pink Floyd fan!')
elif score >= 5:
    print(f'\n{bot_name}: Hmm {name}, your final score is {score}/10. Not a bad attempt! Better luck next time!')
elif score >= 1:
    print(f'\n{bot_name}: Sorry {name}, your final score is {score}/10. I expected better from you...')
else:
    print(f'\n{bot_name}: Dude... {name}, your final score is {score}/10... I think you better stick to listening to K-Pop.')

time.sleep(3)
print(f'\n{bot_name}: FloydBot signing off...')
time.sleep(1.5)
print(f'\n{bot_name}: Goodbye cruel world...')
time.sleep(2)
    
    
# this was the way I had it coded without the for loop, where I would have had to copy and paste this 10 times.
# i decided to use a for loop instead to improve my looping skills, and added all the question/answer info in the dictionary.
    
    # if user_input in questions_dict['q1']:
    #     print(f'{bot_name}: Good job! If you got that wrong, I would have quit right there and then...')
    #     score +=1
    #     break
    # else:
    #     print(f'{bot_name}: Damn... Not off to a good start dude...')
    #     break
