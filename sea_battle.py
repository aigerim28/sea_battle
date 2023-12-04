import random

all_players = []

def cls():
    print('\n' * 100)

def custom_key(players_list):
    return players_list[1]

def main_menu():
    print('You are in Main menu. ')
    print('\nActions: \n1 - Start a game \n2 - See the list of all players')
    print()
    choose_action()

def choose_action():
    action = int(input('Choose action (1/2): '))
    if action == 1:
        cls()
        sea_battle()
    elif action == 2:
        if all_players:
            cls()
            print('List of players is empty. Become first!')
            print()
            menu = int(input('For going back to Main menu enter 1: '))
            if menu == 1:
                cls()
                main_menu()
        else:
            all_players.sort(key=custom_key, reverse=True)
            cls()
            print('List of all players:')
            for i in range(len(all_players)):
                print(f'{i + 1}. {all_players[i][0]} - {all_players[i][1]}')
            print()
            
            menu = int(input('For going back to Main menu enter 1: '))
            if menu == 1:
                cls()
                main_menu()
    else:
        print('There is no such action. PLease, try again.')
        choose_action()

def create_console():
    y_domain = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    console = [[0 for _ in range(8)] for _ in range(8)]
    console[0] = y_domain
    for i in range(1, 8):
        console[i][0] = i
    return console

def place_ships():
    list_ships = []
    ships1 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships1)
    ships2 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships2)
    ships3 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 2, 2],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3, 0, 0],
        [0, 0, 0, 0, 3, 0, 0],
        [0, 1, 0, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships3)
    ships4 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 0, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [3, 0, 0, 0, 2, 0, 0],
        [3, 0, 1, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships4)
    ships5 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 1, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 2, 2, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships5)
    ships6 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 2, 0, 1],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships6)
    ships7 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 0, 0, 2],
        [0, 0, 3, 0, 1, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships7)
    ships8 = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 1],
        [0, 0, 1, 0, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    list_ships.append(ships8)
    return random.choice(list_ships)

def hit_point(console, ships, x, y):
    if ships[x + 1][y - 1] == 1:
        print('You have crushed a ship!')
        ships[x - 1][y - 1] = 0
        console[x][y] = 'x'
        return True
    elif ships[x + 1][y - 1] == 2:
        ships[x + 1][y - 1] = 0
        console[x][y] = 'x'
        item = 2
        if item in ships[x + 1] or ships[x + 2][y - 1] == 2 or ships[x][y - 1] == 2:
            print('You have hit the ship!')
            return True
        else:
            print('You have crushed a ship!')
            return True
    elif ships[x + 1][y - 1] == 3:
        ships[x + 1][y - 1] = 0
        console[x][y] = 'x'
        item = 3
        if item in ships[x + 1] or ships[x + 2][y - 1] == 3 or ships[x + 3][y - 1] == 3 or ships[x][y - 1] == 3 or ships[x - 1][y - 1] == 3:
            print('You have hit the ship!')
            return True
        else:
            print('You have crushed a ship!')
            return True
    else:
        print('Oops! There was no ship...')
        ships[x + 1][y - 1] = 0
        console[x][y] = '-'
        return False


def sea_battle():
    result = []
    name = input('Enter your name: ')
    print(f'Welcome to the game, {name}!')
    print()

    y_domain = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    console = create_console()
    ships = place_ships()
    hits = 0
    total_points = 0
    
    while total_points < 11:
        for row in console:
            print(' '.join([str(elem) for elem in row]))
        print('\nEnter place (for example: "A;1") :')
        y_letter, x = input().split(';')
        
        y = y_domain.index(y_letter)
        x = int(x)
        
        if console[x][y] == '-' or console[x][y] == 'x':
            print()
            print('You have already hit this point, please, enter another place: ')
            y_letter, x = input().split(';')
            y = y_domain.index(y_letter)
            x = int(x)
        
        if hit_point(console, ships, x, y) == True:
            total_points += 1
        hits += 1
    if total_points == 11:
        print('Congratulations! You have crushed all ships!')
        print('Quantity of hits you made:', hits)

        result.append(name)
        result.append(hits)
        all_players.append(result)
        
        will = int(input('\nWould you like to play one more time? (Enter 1/0)'))
        if will == 1:
            sea_battle()
        else:
            main_menu()


main_menu()

