import time
import random
import os
from tabulate import tabulate
from colorama import Fore, Back, Style, init
import questions
os.system('ls')
init(autoreset=True)


def runGame():
    '''Triggered at the start'''

    print(Back.WHITE + Fore.BLACK + Style.BRIGHT +
          'Welcome to ConsoleQuizbowl!\n' + Style.RESET_ALL + 
          'This program reads questions from the '
          'PACE 2019 National Scholastic Competition clue by clue.\n'
          'Earn points by answering these correctly: 15 points during power, '
          'denoted by (*), and 10 points after.')

    while True:
        try:
            amtQuestions = int(input(
                f'\n- How many questions would you like? (Max {len(questionBank)})\n- '))
        except ValueError:
            print('Not an integer!')
        else:
            if (0 < amtQuestions <= len(questionBank)) != True:
                if amtQuestions == 000000:
                    break  # Troubleshooting to stats
                print('Integer too big or negative!')
            else:
                break

    print("\nLet's get quizzing!")
    time.sleep(1)

    for n in range(amtQuestions):
        print(Back.WHITE + Fore.BLACK + f'\nQuestion {n + 1}')
        quiz()

    print("\nAnd that's the quiz!\n\n" +
          Back.WHITE + Fore.BLACK + 'Player Statistics')

    # Printing the stats
    core, subjects = finalStats()
    for char in core:
        print(char, end='')
        time.sleep(0.01)
    print(Style.BRIGHT + '\n\nSubject Scores')
    for char in subjects:
        print(char, end='')
        time.sleep(0.01)

    print('\n\nThanks for Playing!')


def quiz():
    '''Triggered in runGame() x amount of times.
    Initiates readQuestion(), computes stats'''

    print('')
    pos = random.randint(0, len(questionBank) - 1)
    question = questionBank[pos]
    del questionBank[pos]
    promptClues = question['prompt'].split('//')
    answer = [stringFix(x) for x in question['answer']]
    fullAnswer = question['full answer']
    subject = question['subject']

    clueNum, powerActive, correct = readQuestion(promptClues, answer)

    print('- The answer was',
          Back.CYAN + Style.BRIGHT + fullAnswer,
          f'(Subject: {subject.capitalize()})')

    # Computes player statistics after a question
    percentOfQuestion = percentOfHundred((clueNum + 1), len(promptClues))
    if correct:
        print(f'- You needed {clueNum + 1} clues to answer,',
              f'or {percentOfQuestion}% of the question')
        subjectStats[subject][0] += 1
        coreStats['correct'] += 1
        if powerActive:
            coreStats['points'] += 15
            coreStats['powers'] += 1
            print('- The answer was in power, for 15 points!')
        else:
            coreStats['points'] += 10
            print('- The answer was out of power, for 10 points.')

    coreStats['% to answer'].append(percentOfQuestion)
    coreStats['asked'] += 1
    subjectStats[subject][1] += 1

    input('\n- Press enter to continue')


def readQuestion(question, answer):
    '''Read questions clue by clue and returns player results.
    Triggered in quiz()'''

    for n, clue in enumerate(question):
        powerActive = True
        correct = False
        clueNum = n
        print(f'Clue {str(n + 1)}: ', end='', flush=True)

        cluesWords = clue.split()
        for word in cluesWords:
            if word != '(*)':
                print(word, '', end='', flush=True)
                time.sleep(0.1)
            else:
                print(Back.CYAN + word, '', end='', flush=True)
                powerActive = False
                time.sleep(0.01)
        print('\n')

        if clue != question[-1]:
            response = stringFix(
                input(
                    Fore.RED +
                    '- Type the answer, or press enter for the next clue \n- '))
            if response in answer:
                print('- Marvelous, that is correct!\n')
                correct = True
                break
            elif answer == '':
                print()
                time.sleep(0.1)
            else:
                print('- Wrong! Here is your next clue: \n')
                time.sleep(0.1)
        else:
            response = stringFix(
                input(
                    Fore.RED +
                    '- Type the answer, or press enter to reveal it \n- '))
            if response in answer:
                print('- Marvelous, that is correct!\n')
                correct = True
            elif answer == '':
                break
            else:
                print('- Wrong, and that is the end of the question!\n')
    return clueNum, powerActive, correct


def finalStats():
    '''Determines and tabulates final stats at the end of runGame()'''

    ##coreStats = {
    ##    'points': 165,
    ##    'correct': 14,
    ##    'asked': 21,
    ##    'powers': 5,
    ##    '% to answer': [79.65]}
    ##subjectStats = {
    ##    'literature': [0, 1], 
    ##    'history': [3, 5], 
    ##    'rmp': [2, 2], 
    ##    'science': [4, 6], 
    ##    'social science': [2, 2], 
    ##    'geography': [1, 2], 
    ##    'fine arts': [2, 3]}
    # Above are for troubleshooting

    points = coreStats['points']
    correct = coreStats['correct']
    asked = coreStats['asked']
    powers = coreStats['powers']
    avgToAnswer = round(sum(coreStats['% to answer']) /
                        len(coreStats['% to answer']), 2)
    pp20tuh = round(points * 20 / asked, 2)
    coreTable = tabulate([
        ['Total Points', points],
        ['Questions Correct', f'{correct} / {asked}',
         f'{percentOfHundred(correct, asked)}%'],
        ['Questions Answered in Power', f'{powers} / {asked}',
         f'{percentOfHundred(powers, asked)}%'],
        ['Avg % of Question Needed for Answer', f'{avgToAnswer}'],
        ['Points per 20 Tossups Heard', pp20tuh]
    ])

    subjectTable = [
        ['Literature'],
        ['History'],
        ['Religion/Myth/Philosophy'],
        ['Science'],
        ['Social Science'],
        ['Geography'],
        ['Fine Arts']
    ]
    i = 0
    for _, (val, tot) in subjectStats.items():
        rightOverAsked = f'{val} / {tot}'
        statPercent = f'{percentOfHundred(val, tot)}%'
        subjectTable[i].extend([rightOverAsked, statPercent])
        i += 1
    subjectTable = tabulate(subjectTable)

    return (coreTable, subjectTable)


def resetStats():
    '''Resets player statistics at the beginning of runGame()'''
    coreStats = {
        'points': 0,
        'correct': 0,
        'asked': 0,
        'powers': 0,
        '% to answer': [],
    }
    subjectStats = {
        # Subject scores: [0] is amt correct, [1] is amt asked
        'literature': [0, 0],
        'history': [0, 0],
        'rmp': [0, 0],
        'science': [0, 0],
        'social science': [0, 0],
        'geography': [0, 0],
        'fine arts': [0, 0],
    }
    return coreStats, subjectStats


def percentOfHundred(n, d):
    '''Determines % correct given amount correct and amount given'''
    num = n / d if d else 0
    return round(num * 100, 2)


def stringFix(string):
    '''Makes strings uniform to .lower() and spacers'''
    punct = r'''!()-[]{};:''\,<>./?@#$%^&*_~'''
    spacers = '''-_'''

    string = string.lower()
    stringFixed = ''
    for char in string:
        if char not in punct:
            stringFixed += char
        elif char in spacers:
            stringFixed += ' '

    return stringFixed

# Beginning of execution


print('''
    ConsoleQuizbowl
    Made in Python 3.8.1''')
extraGame = False

while True:
    if not extraGame:
        begin = input('\nPress enter to start\n')
        if begin == '':
            questionBank = questions.resetQuestions()
            coreStats, subjectStats = resetStats()
            extraGame = True
            runGame()
    else:
        begin = input("\nPress enter to play again, or type 'exit' to stop\n")
        if begin == '':
            questionBank = questions.resetQuestions()
            coreStats, subjectStats = resetStats()
            os.system('clear')
            runGame()
        elif begin == 'exit':
            break
