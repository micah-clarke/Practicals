

import random

numbers_per_line = 6
minimum_number = 1
maximum_number = 45

def main():
    number_of_picks = int(input("How many quick picks do you want? "))
    while number_of_picks < 0:
        print("Invalid number, must be above 0")
        number_of_picks = int(input("How many quick picks do you want? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum_number, maximum_number)
            while number in quick_pick:
                number = random.randint(minimum_number, maximum_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()