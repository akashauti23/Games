import random
from colorama import Fore, Style

# ASCII art for dice faces
dice_faces = [
    [
        ' ------- ',
        '|       |',
        '|   *   |',
        '|       |',
        ' ------- '
    ],
    [
        ' ------- ',
        '| *     |',
        '|       |',
        '|     * |',
        ' ------- '
    ],
    [
        ' ------- ',
        '| *     |',
        '|   *   |',
        '|     * |',
        ' ------- '
    ],
    [
        ' ------- ',
        '| *   * |',
        '|       |',
        '| *   * |',
        ' ------- '
    ],
    [
        ' ------- ',
        '| *   * |',
        '|   *   |',
        '| *   * |',
        ' ------- '
    ],
    [
        ' ------- ',
        '| *   * |',
        '| *   * |',
        '| *   * |',
        ' ------- '
    ]
]

# Colors for dice faces
dice_colors = [
    Fore.WHITE,  # Color for face with 1 dot
    Fore.GREEN,  # Color for face with 2 dots
    Fore.BLUE,   # Color for face with 3 dots
    Fore.YELLOW, # Color for face with 4 dots
    Fore.RED,    # Color for face with 5 dots
    Fore.MAGENTA # Color for face with 6 dots
]


def number_of_dice():
    while True:
        try:
            input_number = int(input("How many dice would you like to roll? "))
            if input_number <= 0:
                raise ValueError
            return input_number
        except ValueError:
            print("Please enter a valid positive integer.")


def roll_dice(number):
    return [random.randint(1, 6) for _ in range(number)]


def print_dice_face(number):
    print(dice_colors[number - 1] + '\n'.join(dice_faces[number - 1]) + Style.RESET_ALL)


def main():
    number = number_of_dice()
    rolls = roll_dice(number)
    print("You rolled:")
    for roll in rolls:
        if roll <= 6:
            print_dice_face(roll)
        else:
            print("Unknown dice face")


if __name__ == '__main__':
    main()
