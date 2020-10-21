import random

# Lists:
option1 = ['paper', 'rock', 'scissors']
option = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air',
          'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors',
          'fire']

# ID and Rating:
name = str(input('Enter your name: '))
print(f'Hello, {name}')
# score_file = open('rating.txt', 'r') - deactivated
if name == "Tim":
    rating = 0
else:
    rating = 0
# score_file.close() - deactivated

# Iteration:
counter = 0
while True:
    user = input()
    if user == '!rating':
        print(f'Your rating: {rating}')
    elif user == '!exit':
        print('Bye!')
        break

    # Classic Game:
    elif user == '' or user.strip() in option1:
        pc = random.choice(option1)
        if counter == 0:
            print("Okay, let's start")
            user = input()
        counter += 1
        if user == pc:
            print(f'There is a draw {pc}')
            rating += 50
        elif (user == 'rock' and pc == 'scissors') or \
                (user == 'paper' and pc == 'rock') or \
                (user == 'scissors' and pc == 'paper'):
            print(f'Well done. Computer chose {pc} and failed')
            rating += 100
        else:
            print(f'Sorry, but computer chose {pc}')

    # Advanced Game:
    elif user in option or user.split(',') == option:
        pc = random.choice(option)
        if counter == 0:
            print("Okay, let's start")
            user = input()
        counter += 1
        if user == pc:
            print(f'There is a draw {pc}')
            rating += 50
        elif option.index(user) \
                == 0 and option.index(pc) <= 7 or option.index(user) \
                == 1 and 1 < option.index(pc) <= 8 or option.index(user) \
                == 2 and 2 < option.index(pc) <= 9 or option.index(user) \
                == 3 and 3 < option.index(pc) <= 10 or option.index(user) \
                == 4 and 4 < option.index(pc) <= 11 or option.index(user) \
                == 5 and 5 < option.index(pc) <= 12 or option.index(user) \
                == 6 and 6 < option.index(pc) <= 13 or option.index(user) \
                == 7 and 7 < option.index(pc) <= 14 or option.index(user) \
                == 8 and (8 < option.index(pc) <= 14 or option.index(
            pc) == 0) or option.index(user) \
                == 9 and (9 < option.index(pc) <= 14 or option.index(
            pc) <= 1) or option.index(user) \
                == 10 and (10 < option.index(pc) <= 14 or option.index(
            pc) <= 2) or option.index(user) \
                == 11 and (11 < option.index(pc) <= 14 or option.index(
            pc) <= 3) or option.index(user) \
                == 12 and (12 < option.index(pc) <= 14 or option.index(
            pc) <= 4) or option.index(user) \
                == 13 and (13 < option.index(pc) <= 14 or option.index(
            pc) <= 5) or option.index(user) \
                == 14 and (
                14 < option.index(pc) <= 14 or option.index(pc) <= 6):
            print(f'Sorry, but computer chose {pc}')
        else:
            print(f'Well done. Computer chose {pc} and failed')
            rating += 100
    else:
        print('Invalid input')
