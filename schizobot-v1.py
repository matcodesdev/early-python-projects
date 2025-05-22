'''
This script is my first chat bot test.
I will attempt to write it with only accessing my notes.
This chatbot can answer simple greetings and farewell,
perform mathematical calculations with the 4 basic operators,
tell a knock knock joke, and print a 'help' menu.
'''

import time

bot_name = 'SchizoBot'
print(f'\n{bot_name}: Hello, my name is {bot_name}! What is your name?')

name = input('You: ').strip()
you = 'You: '

time.sleep(0.5)
print(f'SchizoBot: Hello {name}, it\'s lovely to meet you!')
print()

chat_inputs = {
    'greetings': ['hi', 'hii', 'hiii', 'hiiii', 'hey', 'heyy', 'heyyy', 'hello', 'helloo', 'hellooo', 'oi', 'oii'],
    'farewells': ['bye', 'byee', 'goodbye', 'see u', 'see you', 'talk soon', 'cya', 'later'],
    'state question': ['how are you?', 'how you doing?', 'how\'s it going?', 'how do you feel?'],
    'state good': ['doing good', 'i\'m good', 'good', 'great', 'i\'m doing good'],
    'state bad': ['doing bad', 'i\'m not good', 'bad', 'meh', 'i\'m not doing good'],
    'actions questions': ['what\'s up?', 'what are you up to?', 'what\'s cooking?'],
    'joke': ['tell me a joke', 'joke', 'say something funny'],
    'who there': ['who\'s there?', 'who\'s there'],
    'wilma': ['wilma who?', 'wilma who'],
    'math': ['calculate', 'math', 'addition', 'subtraction', 'division', 'multiplication'],
    'math_types': ['addition', 'subtraction', 'division', 'multiplication'],
    'help':['help', 'commands', 'what can you do', 'what can you do?', 'list of commands', 'cmd']
    
}

while True:
    user_input = input(you).lower()
    time.sleep(0.5)

    # this section is to determine what category the user input is going to run.
    if user_input in chat_inputs['greetings']:
        print(f'\n{bot_name}: Hello {name}!')
    elif user_input in chat_inputs['farewells']:
        print(f'\n{bot_name}: Goodbye {name}!')
        break
    elif user_input in chat_inputs['state question']:
        print(f'\n{bot_name}: I\'m doing great {name}! How about yourself?')
        user_state = input(you).lower()
        if user_state in chat_inputs['state good']:
            print(f'\n{bot_name}: I\'m glad to hear that {name}!')
        elif user_state in chat_inputs['state bad']:
            print(f'\n{bot_name}: I\'m sorry to hear that {name}!')
    elif user_input in chat_inputs['help']: # bot tells user what it can do
        print(f'''\n{bot_name}: Here\'s what I can do;
              - Greet you, say hi!
              - Ask how you're feeling
              - Tell dirty jokes
              - Do math
              - Shut down if you say bye
              - And more soon...!''')
    
    elif user_input in chat_inputs['joke']:
        print(f'\n{bot_name}: Knock Knock!')

        # this while statement is to loop the answer of "Knock Knock" part of the joke
        while True:
            joke_input = input(you).lower()
            time.sleep(1.5)
            if joke_input in chat_inputs['who there']:
                print(f'\n{bot_name}: Wilma')
                break
            else:
                print(f'\n{bot_name}: Nu-uh! That\'s not how the joke goes, dummy!')
        
        # this while statement is to loop the "who's there" part of the joke
        while True:
            joke_input = input(you).lower()
            time.sleep(1.5)
            if joke_input in chat_inputs['wilma']:
                print(f'\n{bot_name}: Wilma balls fit in your mouth baby girl?')
                break
            else:
                print(f'\n{bot_name}: Stop trying to ruin my joke!')

    elif user_input in chat_inputs['math']:
        print(f'\n{bot_name}: Let\'s do some maths!')
        time.sleep(1)
        print(f'{bot_name}: Would you like to do an addition, subtraction, division or multiplication?')

        math_type = input(you)

        while math_type not in chat_inputs['math_types']:
            time.sleep(0.5)
            print(f'\n{bot_name}: I\'m sorry, I don\'t recognize that operation. Please try again.')
            math_type = input(you)
        
        time.sleep(0.5)
        print(f'\n{bot_name}: Please input the first number.')
        num1 = float(input(you))
        time.sleep(0.5)
        print(f'\n{bot_name}: Please input the second number.')
        num2 = float(input(you))

        # this segment will give you an answer based on the operator type, as well as data type (float or int)
        if math_type == 'addition':
            if (num1 + num2).is_integer():
                print(f'\n{bot_name}: The answer of {int(num1)} plus {int(num2)} is {int(num1 + num2)}.')
            else:
                print(f'\n{bot_name}: The answer of {num1} plus {num2} is {num1 + num2}.')
        if math_type == 'subtraction':
            if (num1 - num2).is_integer():
                print(f'\n{bot_name}: The answer of {int(num1)} minus {int(num2)} is {int(num1 - num2)}.')
            else:
                print(f'\n{bot_name}: The answer of {num1} minus {num2} is {num1 - num2}.')
        if math_type == 'division':
            if (num1 / num2).is_integer():
                print(f'\n{bot_name}: The answer of {int(num1)} divided by {int(num2)} is {int(num1 / num2)}.')
            else:
                print(f'\n{bot_name}: The answer of {num1} divided by {num2} is {num1 / num2}.')
        if math_type == 'multiplication':
            if (num1 * num2).is_integer():
                print(f'\n{bot_name}: The answer of {int(num1)} multiplied by {int(num2)} is {int(num1 * num2)}.')
            else:
                print(f'\n{bot_name}: The answer of {num1} multiplied by {num2} is {num1 * num2}.')

    else:
        print(f'\n{bot_name}: I\'m sorry {name}, I was not programmed to understand this input yet!')