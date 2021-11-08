import random
import time


def print_table(msg, table):
    print(msg)

    line = 0
    for item in table:
        print(item, end='')
        line += 1
        if line % 3 == 0:
            print()
        else:
            print('|', end='')
    print()


def make_a_move(player, position, table):
    if table[position] == 'x' or table[position] == '0':
        print("This position is unavailable\n")
        return False

    time.sleep(1)
    if player == 'computer':
        table[position] = '0'
        print_table("The computer played", table)
    else:
        table[position] = 'x'
        print_table("You played", table)

    return True


def chose_the_first(players):
    print("Chosing who will play first: ...")
    time.sleep(1)
    return random.choice(players)


def verify_table(table):
    # verificare linii orizontale
    if table[0] == table[1] == table[2] != ' ':
        return -1 if table[0] == '0' else 1
    if table[3] == table[4] == table[5] != ' ':
        return -1 if table[3] == '0' else 1
    if table[6] == table[7] == table[8] != ' ':
        return -1 if table[6] == '0' else 1

    # verificare linii verticale
    if table[0] == table[3] == table[6] != ' ':
        return -1 if table[0] == '0' else 1
    if table[1] == table[4] == table[7] != ' ':
        return -1 if table[1] == '0' else 1
    if table[2] == table[5] == table[8] != ' ':
        return -1 if table[2] == '0' else 1

    # verificare linii diagonale
    if table[0] == table[4] == table[8] != ' ':
        return -1 if table[0] == '0' else 1
    if table[2] == table[4] == table[6] != ' ':
        return -1 if table[2] == '0' else 1

    return 0


def human_move():
    user_choice = input("Сhose a position for your movement: ")
    while user_choice == '' or len(user_choice) > 1 or ord(user_choice) not in range(49, 58):
        user_choice = input("Please, chose a number from 1 to 9: ")
    return int(user_choice) - 1


def computer_move(table):
    if table[4] == ' ':
        return 4

    temp_list = list(filter(lambda x: table[x] == ' ', [0, 2, 6, 8]))

    if len(temp_list) == 0:
        temp_list = list(filter(lambda x: table[x] == ' ', [1, 3, 5, 7]))

    return temp_list[0]


def switch_player(player):
    if player == 'human':
        return 'computer'
    return 'human'


def check_table(table):
    for item in table:
        if item == ' ':
            return True

    return False


def main():
    table = [' ' for i in range(9)]
    print_table("The initial table is:", table)

    who_is_playing = chose_the_first(['computer', 'human'])
    # who_is_playing = players[1] //default
    print(f"The first player is: {who_is_playing}\n")

    if who_is_playing == 'computer':
        make_a_move('computer', 4, table)
        who_is_playing = 'human'

    while True:
        if not check_table(table):
            print("Game Over. No one won.")
            break

        if who_is_playing == 'human':
            move = human_move()
        else:
            move = computer_move(table)

        if not make_a_move(who_is_playing, move, table):
            continue

        who_is_playing = switch_player(who_is_playing)
        status = verify_table(table)

        if status == 1:
            print_table("\nCongratulations! You won!", table)
            break
        elif status == -1:
            print_table("\nGame Over! The computer won.", table)
            break


if __name__ == "__main__":
    main()
