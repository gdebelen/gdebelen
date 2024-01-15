import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    The function "check_winnings" calculates the total winnings and identifies the winning lines in a
    slot machine game based on the symbols in each column.
    
    :param columns: A list of lists representing the symbols in each column of a slot machine. Each
    inner list represents a column, and each element in the inner list represents a symbol in that
    column
    :param lines: The number of lines in the slot machine game
    :param bet: The bet parameter represents the amount of money that the player has bet on the game
    :param values: The `values` parameter is a dictionary that maps each symbol to its corresponding
    value. For example, if the symbols are represented by letters and their values are represented by
    numbers, the `values` dictionary could look like this:
    :return: two values: the total winnings and a list of the winning lines.
    """
    winnings = 0
    winning_lines = []
    # The line `for line in range(lines):` is used to iterate over the range of numbers from 0 to
    # `lines-1`. It is used to represent each line in the slot machine game. The variable `line` takes
    # on the values from 0 to `lines-1` in each iteration of the loop.
    for line in range(lines):
        symbol = columns[0][line]
        # The line `for column in columns:` is used to iterate over each column in the `columns` list.
        # It is part of the `check_winnings` function and is used to compare the symbols in each
        # column for a specific line in the slot machine game.
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    The function `get_slot_machine_spin` generates a random spin result for a slot machine with the
    specified number of rows, columns, and symbols.
    
    :param rows: The number of rows in the slot machine
    :param cols: The number of columns in the slot machine
    :param symbols: The `symbols` parameter is a dictionary where the keys are the symbols and the
    values are the number of times each symbol should appear on the slot machine
    :return: a list of columns, where each column is a list of symbols randomly selected from the given
    symbols.
    """
    # The line `all_symbols = []` initializes an empty list called `all_symbols`. This list will be
    # used to store all the symbols that can appear on the slot machine.
    all_symbols = []
    # The line `for symbol, symbol_count in symbols.items():` is used to iterate over the items in the
    # `symbols` dictionary. In each iteration, the variable `symbol` takes on the key of the current
    # item, and the variable `symbol_count` takes on the value of the current item. This allows the
    # code to access both the symbol and its corresponding count in the dictionary.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    # The line `for _ in range(cols):` is used to iterate over the range of numbers from 0 to
    # `cols-1`. It is used to represent each column in the slot machine game. The variable `_` is used
    # as a placeholder for the loop variable, indicating that the loop variable is not being used in
    # the loop body. This is commonly done when the loop variable is not needed and only the iteration
    # count is important.
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # The line `for _ in range(rows):` is used to iterate over the range of numbers from 0 to
        # `rows-1`. It is used to represent each row in the slot machine game. The variable `_` is
        # used as a placeholder for the loop variable, indicating that the loop variable is not being
        # used in the loop body. This is commonly done when the loop variable is not needed and only
        # the iteration count is important.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    The function `print_slot_machine` prints a slot machine with the given columns.
    
    :param columns: The "columns" parameter is a list of lists. Each inner list represents a column in
    the slot machine. The elements in each inner list represent the symbols in that column
    """
    # The line `for row in range(len(columns[0])):` is iterating over the range of indices of the
    # elements in the first column of the `columns` list. It is used to iterate over each row of the
    # slot machine and print the symbols in each column for that row.
    for row in range(len(columns[0])):
        # The line `for i, column in enumerate(columns):` is used to iterate over the `columns` list
        # and access each column along with its index.
        # The line `for i, column in enumerate(columns):` is used to iterate over the `columns` list
        # and access each column along with its index. The `enumerate()` function is used to return
        # both the index and the value of each element in the `columns` list. In each iteration of the
        # loop, the variable `i` represents the index of the current column, and the variable `column`
        # represents the value of the current column. This allows the code to print the symbols in
        # each column for a specific row in the slot machine game.
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                 print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    """
    The function `deposit()` prompts the user to enter an amount to deposit, validates the input, and
    returns the amount as an integer.
    :return: the amount that the user wants to deposit.
    """
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    """
    The function `get_number_of_lines` prompts the user to enter the number of lines they want to bet
    on, validates the input, and returns the number of lines.
    :return: the number of lines that the user has entered.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines. (1-{MAX_LINES}) lines")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    """
    The function `get_bet()` prompts the user to enter a bet amount and validates that it is a number
    within a specified range.
    :return: the amount that the user wants to bet on each line.
    """
    while True:
        amount = input("What would you like to bet on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    """
    The function `spin` takes a balance as input and allows the user to place a bet on a slot machine
    spin, checking if the bet is valid and calculating the winnings.
    
    :param balance: The balance parameter represents the current balance of the player's account. It is
    the amount of money they have available to place bets
    :return: the difference between the total winnings and the total bet.
    """
    lines = get_number_of_lines() 
    # The `while True:` statement creates an infinite loop. It means that the code inside the loop
    # will continue to execute indefinitely until a break statement is encountered or an exception is
    # raised. In this specific code, the `while True:` loop is used to repeatedly prompt the user to
    # play the slot machine game until they choose to quit by entering "q".
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is £{balance}.")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to £{total_bet}.") 

    # The line `slots = get_slot_machine_spin(ROWS, COLS, symbol_count)` is calling the
    # `get_slot_machine_spin` function with the arguments `ROWS`, `COLS`, and `symbol_count`.
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  
    print_slot_machine(slots)
    # The `print_slot_machine(slots)` function is used to print the symbols in each column of the slot
    # machine. It takes a list of columns as input, where each column is a list of symbols. It
    # iterates over each row of the slot machine and prints the symbols in each column for that row.
    # The symbols are separated by a "|" character.
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # The line `winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)` is calling
    # the `check_winnings` function with the arguments `slots`, `lines`, `bet`, and `symbol_value`.
    print(f"You won £{winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

    
def main():
    """
    The main function is the entry point of the program.
    """
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with £{balance}.")

    

main()