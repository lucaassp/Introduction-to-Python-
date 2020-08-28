from random import choice
from os import system
import platform

file = open('/home/lucas/Área de Trabalho/Curso de Python/Introdução a Programação/Projetos/game_force/words.txt', 'r')
file = file.readlines()

def generate_random_word():
    words = choice(file)
    return words[:-1]

def menu():
    print('-' * 10)
    print('F-O-R-C-A')
    print('-' * 10)

def clear():
    if platform.system != 'Windows':
        system('clear')
    else:
        system('cls')

def main():
    menu()
    playing = True
    incorrectLetters = ''
    correctLetters = ''
    word = generate_random_word()
    incompleteWord = ['_'] * len(word)

    while playing:
        print('\n', ' '.join(incompleteWord), '\n')
        letter = input('\033[1;32m\nDigite uma letra: ')
        if len(letter) != 1:
            clear()
            print('\033[1;31m\n*Digite apenas uma letra!*')
        elif letter in incorrectLetters or letter in correctLetters:
            clear()
            print('\033[1;31m\n*Esta letra já foi digitada!*\n')
        elif letter not in word:
            clear()
            incorrectLetters += letter
            print(f'\nLetras erradas: {incorrectLetters.upper()}\n')
            if len(incorrectLetters) == 6:
                print('\033[1;31m\n\n*Limite de tentativas acabada!*\n')
                print(f'A palavra correta é: {word.upper()}')
                playing = False
                option = input('\033[1;32m\nVocê quer retornar ao jogo? [S/n:] ')
                if option.lower() == 's':
                    clear()
                    menu()
                    playing = True
                    incorrectLetters = ''
                    correctLetters = ''
                    word = generate_random_word()
                    incompleteWord = ['_'] * len(word)

        else:
            for i in range(len(word)):
                if letter == word[i]:
                    incompleteWord[i] = letter
            correctLetters += letter
            if ' '.join(incompleteWord) == ' '.join(word):
                print('\033[1;36m=' * 40)
                print(f'\033[1;34m***PARABÉNS VOCÊ GANHOU***\nA paravra correta é: {word.upper()}')
                print('\033[1;36m=' * 40)
                playing = False
                option = input('\033[1;32m\nVocê quer retornar ao jogo? [S/n:] ')
                if option.lower() == 's':
                    clear()
                    menu()
                    playing = True
                    incorrectLetters = ''
                    correctLetters = ''
                    word = generate_random_word()
                    incompleteWord = ['_'] * len(word)

main()