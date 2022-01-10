import random
def quiz():
    from random import shuffle
    dictionary = {
        'Russia': 'Moscow',
        'Belarus': 'Minsk',
        'Ukraine': 'Kiev'}
    random = list(dictionary.keys())
    shuffle(random)
    score = 0

    for i in random:
        answer = input(f'Enter the capital of {i}: ')
        if answer == dictionary[i]:
            score += 100
            print(f'Correct answer, your score {score}')
        else:
            print(f'Wrong answer, your score {score}')
    print(f'Final score {score}')
quiz()
