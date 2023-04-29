"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Marcel Halamka
email: maacek1@seznam.cz
discord: Kronos #8011
"""

print("Welcome to Tic Tac Toe")
print("""
Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
=============================================
Let's start the game
---------------------------------------------""")

def separator() -> None:
    """Vypíše jen oddělovač"""
    print("=============================================")

def board(new_list) -> None:
    """Tahle funkce mi vyprintuje hrací pole"""
    print(new_list[0] + " | " + new_list[1] + " | " + new_list[2])
    print(new_list[3] + " | " + new_list[4] + " | " + new_list[5])
    print(new_list[6] + " | " + new_list[7] + " | " + new_list[8])

def checking_input(symbol) -> int:
    """Funkce zkontroluje zda-li je vstup číslo a je
    v rozmezí 0 - 9.Nejlepší způsob je podle mne
    v cyklu while použít try-except abych zachytil 
    ValueError chybu"""
    lets = True
    while lets:
        try:
            number = int(input(f"Player {symbol} Please enter your move number(1-9):"))
            number = number - 1
            if number > -1 and number < 9:
                if new_list[number] == "-":
                    lets = False
                else:
                    print("Occupied, try again!")
            else:
                print("Wrong number(not 1-9)")
        except ValueError:
            print("It is not integer!!!")
    return number

def fill(symbol, number) -> None:
    """Zde vlastně projedeme list a nahradíme
    "-" za symbol od uživatele"""
    for x in range(len(new_list)):
        if number == x:
            new_list[number] = symbol

def check_result(symbol) -> None:
    """Zkontroluje, jestli jsme náhodou nevyhráli nebo
    nenastala remíza(vyplnili jsme všechny pole)
    a pokud nastane jedna z těchto dvou podmínek tak se
    program ukončí."""
    # Kontrola řad, sloupců a diagonál
    if (new_list[0] == symbol and new_list[1] == symbol and new_list[2] == symbol) or\
    (new_list[3] == symbol and new_list[4] == symbol and new_list[5] == symbol)or\
    (new_list[6] == symbol and new_list[7] == symbol and new_list[8] == symbol) or\
    (new_list[0] == symbol and new_list[3] == symbol and new_list[6] == symbol)or\
    (new_list[1] == symbol and new_list[4] == symbol and new_list[7] == symbol) or \
    (new_list[2] == symbol and new_list[5] == symbol and new_list[8] == symbol)or\
    (new_list[0] == symbol and new_list[4] == symbol and new_list[8] == symbol)or\
    (new_list[2] == symbol and new_list[4] == symbol and new_list[6] == symbol):
        separator()
        print(f"Congratulations, player {symbol} win!")
        separator()
        quit()
    # Kontrola zda-li nenastala remíza
    elif "-" not in new_list:
        separator()
        print("Tie!!")
        separator()
        quit()

def main()-> None:
    """Hlavní funkce kde se vše spouští a je zde hlavní cyklus.Zde jsem dal 
    proměnnou-new_list do globálního rámce, protože skoro všechny funkce s ní
    pracují, tak myslím, že sem patří:)"""

    global new_list
    new_list = 9 * ["-"]
    board(new_list)
    # Hlavní cyklus
    while True:
        separator()
        number = checking_input("O")
        separator()
        fill("O", number)
        board(new_list)
        check_result("O")
        separator()
        number = checking_input("X")
        separator()
        fill("X", number)
        board(new_list)
        check_result("X")
        
        
main()