import random


def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|      |        ",
              "|      0        ",
              "|     /|\       ",
              "|     / \       ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print(f"Вы проиграли! Было загадано слово '{word}'")


with open('words.txt', encoding='utf-8') as f:
    lst = f.readlines()

for i in range(len(lst)):
    el = lst[i][:len(lst[i])-1]
    lst[i] = el

random_word = random.choice(lst)


hangman(random_word)
