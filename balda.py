import random
def get_word():
    word_list = []
    with open('russian_nouns.txt', encoding='utf8') as file:
        for line in file:
            if len(line) > 8:

                word_list.append(line.strip())
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):  # основная функция игры
    word_x = [i for i in '_' * len(word)]  # список, содержащий символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв или слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print('\nЗагаданное слово:', *word_x,
          '\nВам нужно его отгадать, \nможете это делать отгадывая по одной букве или сразу написать слово.')
    print('\nНапишите букву или слово:')
    while 0 < tries:
        # print(word, guessed_words, guessed_letters)
        s = input().upper()
        if not s.isalpha():
            print('Вводить можно только буквы, попробуйте еще раз.')
            continue
        if s == word:
            print(f'Поздравляем, вы угадали слово {word.upper()}! Вы победили!')
            break
        if s in guessed_letters:
            print('Эта буква или слово были ранее, выберете другой вариант.')
            continue
        else:
            guessed_letters.append(s)
        for j in range(len(word)):
            if word[j] == s:
                word_x[j] = s
        print('Смотрим, что получилось:', ' '.join(word_x).upper())
        if word == ''.join(word_x):
            print(f'Поздравляем, вы угадали слово {word.upper()}! Вы победили!')
            break
        if s not in word:
            tries -= 1
            print(display_hangman(tries))
        if tries == 0:
            print('Увы, попыток больше не осталось.')
            print('Было загадано, слово: "', word.upper(), '"', sep='')
            print('Не расстраивайтесь попробуйте еще, Вам обязательно повезет! :)')
        else:
            print('Осталось попыток:', tries)

word = get_word()
play(word)