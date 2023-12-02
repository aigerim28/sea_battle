hits = 0
y_domain = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
console = [[0 for _ in range(8)] for _ in range(8)]
console[0] = y_domain
for i in range(1, 8):
    console[i][0] = i
ships = []

def place_ships():
    ships = [[0, 0, 0, 0, 1, 0, 0],
        [3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]]
    return ships

def check_point(ships, x, y):
    if ships[x - 1][y - 1] > 0:
        print('You have hit the ship!')
        ships[x - 1][y - 1] = 0
        console[x][y] = 'x'
    else:
        print('Oops! There was no ship...')
        ships[x - 1][y - 1] = 0
        console[x][y] = '-'
    
    

def sea_battle(ships):
    name = input('Enter your name: ')
    
    summa = 0
    summa = [[(summa + elem) for elem in row] for row in ships]
    
    while summa != 0:
        for row in console:
            print(' '.join([str(elem) for elem in row]))
        print('Enter place (for example: "A; 1") :')
        y_letter, x = input().split(';')
        
        y = y_domain.index(y_letter)
        x = int(x)
        
        if console[x][y] == '-' or console[x][y] == 'x':
            print('You have already hit this point, please, try to hit another place')
            y_letter, x = input().split(';')
            y = y_domain.index(y_letter)
            x = int(x)
        
        check_point(ships, x, y)
        hits += 1
    if summa == 0:
        print('Game is over.')
        print('Quantity of hits you made:', hits)
        will = int(input('\nWould you like to play one more time? (Enter 1/0)'))
        if will == 1:
            place_ships()
            sea_battle(ships)


#place_ships()
#sea_battle(ships)
y_letter = input()
y = y_domain.index(y_letter)
print(y)
