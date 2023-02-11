# modules
import random

# variables
colors = ['R', 'G', 'B', 'Y', 'W', 'O']
tries = 10
code_length = 4


# functions
def generate_code():
    code = []

    for i in range(code_length):
        color = random.choice(colors)
        code.append(color)
    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != code_length:
            print(f"you must guess {code_length} colors.")
            continue

        for color in guess:
            if color != colors:
                print(f"invalid colour: {color}. try again.")
            else:
                break
    return guess


def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color != color_count:
            color_count[color] = 0
        color_count[color] += 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"welcome to mastermind, you have {tries} to gues the code...")
    print("the values colors are", *colors)
    code = generate_code()
    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print(f"you guessed the code in {attempts} tries!")
            break
        print(f"correct position: {correct_pos} | incorrect position: {incorrect_pos}")
    else:
        print("you ran out of tries, the code was: ", *code)


if __name__ == '__main__':
    game()
