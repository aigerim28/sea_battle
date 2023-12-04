import random

#The list for all players, with their scores.
all_players = []

#The function for cleaning screen
def cls():
    print('\n' * 100)

#Key for sorting scores in list of all players
def custom_key(players_list):
    return players_list[1]


#This function creates a console which will be shown to user, with first row consisting of letters A-G and first column with numbers 1-7
def create_console():
    console = [[0 for _ in range(8)] for _ in range(8)]
    console[0] = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in range(1, 8):
        console[i][0] = i
    return console

#Function for creating 8 different maps where ships are located and it gives to user randomly one of them.
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

#hit_point function gets console, ships placement and x, y coordinates
#and checks whether the given point has a ship in there or not and gives True 
#or False. Furthermore,it checks did the user totally crushed one ship or just hit it, and 
#prints such message. 
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

#The function part where the game starts. It takes a name from user,
#gets coordinates until there is no ship on the map, counts hits and 
#appends name with number of hits to the all players' score list.
#After ending a game it asks user about their will to play again.
#So, if answer is yes, new game starts, if answer is no, it moves user
#back to Main menu.
def sea_battle():
    result = []
    name = input('Enter your name: ')
    print(f'Welcome to the game, {name}!')
    print('\nThe point will be displayed as: \n"-" - "miss", \n"x" - "hit"')
    print()

    y_domain = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    console = create_console()
    ships = place_ships()
    #Variable for counting hits 
    hits = 0
    #Variable for counting points for each hit ship.
    total_points = 0

    #Totally there are 11 places where ships are present.
    #So, we will continue the game until we crush all ships
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

        #If we get True value (so we hit or crush ship) and we 
        #add it to variable total_point
        if hit_point(console, ships, x, y) == True:
            total_points += 1
        hits += 1
    if total_points == 11:
        print('Congratulations! You have crushed all ships!')
        print('Quantity of hits you made:', hits)

        #Appending user's name and score to the list result firstly
        #and appending result list to list of all_players
        result.append(name)
        result.append(hits)
        all_players.append(result)

        #Asking user about their will to play again.
        will = int(input('\nWould you like to play one more time? (Enter 1/0)'))
        if will == 1:
            sea_battle()
        else:
            main_menu()


#The function for choosing actions: starting a game or seeing list of all players with their scores.
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
            #Sorting all_players list from highest to lowest and printing it.
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
        #If user enters invalid action that does not exist, program will tell it and ask to enter again.
        print('There is no such action. PLease, try again.')
        choose_action()
#Function for Main menu
def main_menu():
    print('You are in Main menu. ')
    print('\nActions: \n1 - Start a game \n2 - See the list of all players')
    print()
    choose_action()

main_menu()

