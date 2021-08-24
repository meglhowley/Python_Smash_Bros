import random
import json
from smash import Character
from smash import Battle

characters = []

p1_score = 0
cpu_score = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)


def game():
    print(random.choice(characters))
    print(r"""/

      ______. __    __  .______    _______ .______
    /       ||  |  |  | |   _  \  |   ____||   _  \
   |   (----`|  |  |  | |  |_)  | |  |__   |  |_)  |
    \   \    |  |  |  | |   ___/  |   __|  |      /
.----)   |   |  `--'  | |  |      |  |____ |  |\  \----.
|_______/     \______/  | _|      |_______|| _| `._____|


____/\\\\\\\\\\\____/\\\\____________/\\\\_____/\\\\\\\\\________/\\\\\\\\\\\____/\\\________/\\\_
 ___/\\\/////////\\\_\/\\\\\\________/\\\\\\___/\\\\\\\\\\\\\____/\\\/////////\\\_\/\\\_______\/\\\_
  __\//\\\______\///__\/\\\//\\\____/\\\//\\\__/\\\/////////\\\__\//\\\______\///__\/\\\_______\/\\\_
   ___\////\\\_________\/\\\\///\\\/\\\/_\/\\\_\/\\\_______\/\\\___\////\\\_________\/\\\\\\\\\\\\\\\_
    ______\////\\\______\/\\\__\///\\\/___\/\\\_\/\\\\\\\\\\\\\\\______\////\\\______\/\\\/////////\\\_
     _________\////\\\___\/\\\____\///_____\/\\\_\/\\\/////////\\\_________\////\\\___\/\\\_______\/\\\_
      __/\\\______\//\\\__\/\\\_____________\/\\\_\/\\\_______\/\\\__/\\\______\//\\\__\/\\\_______\/\\\_
       _\///\\\\\\\\\\\/___\/\\\_____________\/\\\_\/\\\_______\/\\\_\///\\\\\\\\\\\/___\/\\\_______\/\\\_
        ___\///////////_____\///______________\///__\///________\///____\///////////_____\///________\///__
                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⣾⢟⢁⡄⠀⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢟⣿⣿⣾⠟⠁⠀⣠⣾⠀⠀⠀⢠⣿⠄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⠀⠀⣼⣧⠀⢺⣿⣿⡃⠀⣴⣿⡟⠁⣼⠅⣠⣿⡗⡠⠀⠀⠀⠀      .______   .______        ______        _______.
            ⠀⠀⠀⠀⢰⣧⣠⣾⣿⣿⣆⣼⣿⣿⣡⢀⣿⣿⣿⣾⣿⣾⣿⣷⠟⠁⠀⠀⠀⠀      |   _  \  |   _  \      /  __  \      /       |
            ⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⡿⠟⢛⠁⠀⠀⠀⠀⠀⠀      |  |_)  | |  |_)  |    |  |  |  |    |   (----`
            ⠀⠀⣀⣠⣾⣿⣿⣿⡏⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣋⣀⣤⣏⠀⠀⠀⠀⠀⠀⠀      |   _  <  |      /     |  |  |  |     \   \
            ⠀⣤⣿⣿⠋⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀      |  |_)  | |  |\  \----.|  `--'  | .----)   |    __
            ⠀⢿⣿⠃⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢻⣿⡟⠀⠀⠀⠀⣠⠆⠀⠀⠀⠀⠀      |______/  | _| `._____| \______/  |_______/    (__)
            ⢀⣼⡏⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡉⢀⣀⣤⣾⠇⠀⠀⠀⠀⣀⠄
            ⢻⣿⣧⣤⣤⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⡿⠋⠁⠀⠀⠀⣠⣾⡁⠀
            ⠈⢻⣿⡍⠉⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⣽⣿⣿⣿⣯⣴⣿⣥⣶⡾⢟⠉⠀⠀
            ⠀⢨⣿⣿⣦⣿⣿⣿⡇⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⡿⠿⠿⠿⠾⠛⠁⠀⠀⠀
            ⠀⠀⠻⠿⢿⣿⣿⣿⣇⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⠶⠄⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠙⠛⠛⠻⠟⠛⠿⠿⠿⢿⣷⣤⡾⠯⠁⠀

    """)
    global cpu_score
    global p1_score
    print('SCORE: P1 ' + str(p1_score) + ' CPU ' + str(cpu_score))
    input('PRESS ENTER TO BEGIN')
    print("PLAYERS")
    print(' ')

    id = 1

    for character in characters:
        print(str(id) + ' - ' + character["name"])
        id += 1
    print('         ')
    p1_choice = input(
        'SELECT YOUR PLAYER (numeric choice, leave blank to randomize): ')
    if p1_choice == '':
        print('   ')
        print('RANDOM PLAYER!')
        print('   ')
        p1 = random.choice(characters)
        print('You will play as.....')
        print('   ')
        print(p1['name'] + '!!!')
    else:
        for index, character in enumerate(characters):
            if int(p1_choice) == index + 1:
                p1 = character
                print("You have chosen")
                print(p1["name"] + '!!!')
    cpu_choice = random.choice(characters)
    player_one = Character(p1["name"], p1["attacks"])
    cpu = Character(cpu_choice["name"], cpu_choice["attacks"])
    print('VERSUS.....')
    print(cpu.name + '!!!')
    battle = Battle(player_one, cpu)
    while (battle.P1.health < 150 and battle.CPU.health < 150):
        input('PRESS ENTER TO ATTACK')
        player_one.select_move()
        print(player_one.name + ' used ' +
              player_one.current_move['name'] + '!!')
        cpu.increment_damage(player_one.current_move['damage'])
        cpu.select_move()
        print(cpu.name + ' used ' +
              cpu.current_move['name'] + '!!')
        player_one.increment_damage(cpu.current_move['damage'])
        print(player_one.name + ': ' + str(player_one.health) +
              '%  VS. ' + cpu.name + ': ' + str(cpu.health) + '%')
    if player_one.health < cpu.health:
        p1_score += 1
        print(cpu.name + ' DIED!!')
        print(player_one.name + ' WINS!!!!!!')
    else:
        cpu_score += 1
        print(player_one.name + ' DIED!!')
        print(cpu.name + ' WINS!!!!!!')
    play_again = input('Play Again? Y/N')
    if play_again == 'Y' or play_again == 'y':
        game()
    else:
        return


game()
