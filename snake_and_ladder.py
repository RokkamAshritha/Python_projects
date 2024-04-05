#Snake and ladder game using Python

#importing all the required modules
import time
import random
import sys


#function for printing the text for player turn
text_for_plr_turn = [
    "Its your turn. Hit enter to roll the dice.",
    "Are you prepared?",
    "Lets Go.",
    "Please move along.",
    "You are doing great.",
    "Ready to be a champion.",
    "",
]

#function for printing the text for snake bite
text_for_snake_bite = [
    "boom!",
    "bang!",
    "snake bite",
    "oops!",
    "dang",
    "oh shit",
    "alas!"
]

#function for printing the text for ladder jump
text_for_ladder_jump = [
    "yipee!",
    "wahoo!",
    "hurrah!",
    "oh my Goodness...",
    "you are on fire",
    "you are a champion",
    "you are going to win this"
]

# Dictionary containing snake bite positions

#Snake Postions where key is the head of snake and value is the tail of snake
snake_position = {
    12: 4,
    18: 6,
    22: 11,
    36: 7,
    42: 8,
    53: 31,
    67: 36,
    73: 28,
    80: 41,
    84: 53,
    90: 48,
    94: 65,
    96: 80,
    99: 2
}

#Ladder Positions where key is the bottom of ladder and value is the top of ladder
ladders_position = {
    3: 26,
    5: 15,
    13: 44,
    25: 51,
    29: 74,
    36: 57,
    42: 72,
    49: 86,
    57: 76,
    61: 93,
    77: 86,
    81: 98,
    88: 91
}

#function for printing the rules of the game
def first_msg():
    msg = """"""

    print(msg)

# Delay of 1 second between each action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6


#function define for taking input (Name of player) from user
def get_player_names():
    p1_name = None
    while not p1_name:
        p1_name = input("Name of first player: ").strip()

    p2_name = None
    while not p2_name:
        p2_name = input("Name of second player: ").strip()

    print("\n'" + p1_name + "' and '" + p2_name + " You will play against each other'\n")
    return p1_name, p2_name


#function define for rolling the dice
def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Dice value " + str(dice_value))
    return dice_value


#function define for snake bite
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_snake_bite).upper() + " ~~~~~~~~>")
    print("\n"" " + player_name + " got a bite from snake. Going down from " + str(old_value) + " to " + str(current_value))


#function define for ladder jump
def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_ladder_jump).upper() + " ########")
    print("\n" + player_name + " is clibing the ladder from " + str(old_value) + " to " + str(current_value))

#function define for snake and ladder
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake_position:
        final_value = snake_position.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders_position:
        final_value = ladders_position.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

#function define for checking the winner
def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n" + player_name + "has  won the game.")
        print("Congratulations " + player_name +"You are the winner")
        sys.exit(1)

#function define for playing the game
def start():
    first_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    p1_name, p2_name = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    p1_current_position = 0
    p2_current_position = 0

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = input("\n" + p1_name + ": " + random.choice(text_for_plr_turn) + " Press enter for rolling the dice: ")
        print("\n d\Dice is being rolled...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(p1_name + " moving....")
        p1_current_position = snake_ladder(p1_name, p1_current_position, dice_value)

        check_win(p1_name, p1_current_position)

        input_2 = input("\n" + p2_name + ": " + random.choice(text_for_plr_turn) + " Press enter for rolling the dice: ")
        print("\n Dice is being rolled...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(p2_name + " moving....")
        p2_current_position = snake_ladder(p2_name, p2_current_position, dice_value)

        check_win(p2_name, p2_current_position)


if __name__ == "__main__":
    start()
