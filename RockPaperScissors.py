import random

print(' 1:Rock \n 2:Paper\n 3:Scissors \n 4:Exit' )

while True:
    x = input(str("Enter your choice: "))
    list = ['Rock', 'Paper', 'Scissors']
    choice = random.choice(list)

    print('You picked: ' + x)
    print('Player 2 picked: ' + choice)

    if x == '1' and choice == 'Rock':
        print('Draw')
    elif x == '1' and choice == 'Paper':
        print('You lose')
    elif x == '1' and choice == 'Scissors':
        print('You win')

    elif x == '2' and choice == 'Rock':
        print('You win')
    elif x == '2' and choice == 'Paper':
        print('Draw')
    elif x == '2' and choice == 'Scissors':
        print('You lose')

    elif x == '3' and choice == 'Rock':
        print('You lose')
    elif x == '3' and choice == 'Paper':
        print('You win')
    elif x == '3' and choice == 'Scissors':
        print('Draw')
    elif x == '4':
        break
    else:
        print('Invalid option')



