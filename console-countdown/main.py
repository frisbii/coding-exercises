'''Run ConsoleCountdown'''
import itertools
import random
import time

import requests
import tabulate as tab

from tabulate import tabulate

tab.PRESERVE_WHITESPACE = True
SCORE_RESPONSES = {2: 'Better luck next time...',
                   3: '... Only three?',
                   4: 'Good try!',
                   5: 'Nice job!',
                   6: 'Great word!',
                   7: 'Superb word!',
                   8: 'Amazing word!',
                   9: 'Maximum length, perfect word!'}

# Creates the list with only alphabetical words A-Z
# File containing all these words comes courtesy of dwyl on GitHub
# Code to parse the file written independently
ENGLISH_WORDS = requests.get(
    "https://github.com/dwyl/english-words/raw/master/words_alpha.txt")
ENGLISH_WORDS = set(ENGLISH_WORDS.text.split())

consonants = ['B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'F', 'F',
              'G', 'G', 'G', 'H', 'H', 'J', 'K', 'L', 'L', 'L', 'L', 'L',
              'M', 'M', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
              'P', 'P', 'P', 'P', 'Q',
              'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
              'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
              'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T',
              'V', 'W', 'X', 'Y', 'Z']
vowels = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
          'A', 'A',
          'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
          'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
          'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
          'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
          'U', 'U', 'U', 'U', 'U']
user_statistics = {'questions asked': 0,
                   'streak': 0,
                   'time taken': [],
                   'scores': [],
                   'max lengths': []}

def run_letters_game():
    '''
    Runs the game:
        Calls on get_letters to get the letters for the round
        Prompts for answer from user
        Calls on check_user_answer to see if the user's answer was valid
        Calls on find_solution to find answer
        Calls on display_statistics to show user stats
    '''
    game_letters = get_letters()

    # Prompts the user for an answer and gets the time they take to respond
    before = time.time()
    print('Timer starts now!')
    user_answer = input('Type your answer, then press enter\n - ')
    time_taken = round(time.time() - before, 1) # Use of mathematical concepts
    user_statistics['time taken'].append(time_taken)

    # Integrated algorithms within the parent algorithm
    check_user_answer(user_answer, game_letters)
    game_answer = find_solution(game_letters)

    print(f'\nYou took {user_statistics["time taken"][-1]} '
          f'seconds to buzz in.')
    print(f'{game_answer}, with {len(game_answer)} letters, '
          f'was a highest scoring answer for this selection.\n')

    user_statistics['questions asked'] += 1
    display_statistics()

def get_letters():
    '''
    Prompts the user for a vowel or consonant nine times, printing the current
    selection each time. Returns the resulting letters
    '''
    game_letters = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    clear_screen()
    print('\nCurrent Selection: \n' +
          tabulate([game_letters], tablefmt='pretty'))
    for i in range(9):
        while True:
            new_letter = input('\nVowel or Consonant? (Enter v or c)\n')
            if new_letter == 'v': # Use of logical concepts
                letter = random.choice(vowels)
                game_letters[i] = letter
                vowels.remove(letter)
            elif new_letter == 'c':
                letter = random.choice(consonants)
                game_letters[i] = letter
                consonants.remove(letter)
            else:
                print('Did not type "v" or "c"!')
                continue
            clear_screen()
            print('\nCurrent Selection: \n' +
                  tabulate([game_letters], tablefmt='pretty'))
            break
    if user_statistics['streak'] % 2 == 0: # Use of mathematical concepts
        print('\nGood luck!')
    else:
        print('\nYou got this!')
    return game_letters

def find_solution(game_letters):
    '''
    Starts with 9 letter length going down and checks permutations of passed
    letters to see whether they are in ENGLISH_WORDS, returns first match.
    '''
    for length in range(9, 1, -1):
        for combo in set(list(itertools.permutations(game_letters, length))):
            guess = ''.join(combo)
            if guess.lower() in ENGLISH_WORDS: # Use of logical concepts
                user_statistics['max lengths'].append(len(guess))
                return guess
    return 'No answer!'

def check_user_answer(user_answer, game_letters):
    '''
    Checks that each letter in the user's answer is in the selection. If they
    are, checks if the answer is an English word.
    '''
    letters_check = [letter.lower() for letter in game_letters]
    score = 0
    try:
        for letter in user_answer:
            letters_check.remove(letter)
        if user_answer in ENGLISH_WORDS: # Use of logical concepts
            user_statistics['streak'] += 1 # Use of mathematical concepts
            score = len(user_answer)
            print(f'Your word was {score} letters long. '
                  f'{SCORE_RESPONSES[score]}')
        else:
            print("Sorry, your word isn't in the dictionary!")
            user_statistics['streak'] = 0
    except ValueError:
        print('Your answer used letters not in the given list, '
              'or used invalid characters')
        user_statistics['streak'] = 0
    user_statistics['scores'].append(score)
    return score

def display_statistics():
    '''Tabulates current user statistics and prints the result.'''
    num_questions = user_statistics['questions asked']
    time_taken = round(sum(user_statistics['time taken'])/num_questions, 1)
    user_score = sum(user_statistics['scores'])
    max_score = sum(user_statistics['max lengths'])
    avg_user_score = round(user_score / num_questions, 1)
    avg_max_score = round(max_score / num_questions, 1)
    table = [['# Questions Asked', num_questions],
             ['Average Time Taken', f'{time_taken} seconds'],
             ['', ''],
             ['Average Score', avg_user_score],
             ['Max Possible Average', avg_max_score],
             ['Total Score', user_score],
             ['Max Possible Score', max_score]]
    print('Current Statistics:')
    print(tabulate(table, colalign=("right",)))

def clear_screen():
    '''Clears console by printing lots of newlines'''
    print(('\n')*50)

# Program execution starts here
print()
print(tabulate([['Console Countdown\nPython 3.8.2']], tablefmt="pretty"))
print('\nWelcome to ConsoleCountdown!\n'
      'In Countdown, you choose nine letters, randomly from either a vowel '
      'or consonant pool. Then, you have 30 seconds to come up with the '
      'longest word you can using those letters.\n')
input('Press enter to begin')
run_letters_game()

while True:
    response = input('\nPress enter to play again, '
                     'or type "exit" to stop the program\n - ')
    if response == 'exit':
        break
    run_letters_game()
