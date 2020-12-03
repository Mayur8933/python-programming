import random

def dice_sum():
    num =int(input("Desired dice sum: "))

    dice1 = random.randint(1,7)
    dice2 = random.randint(1,7)
    dice_sum = dice1 + dice2

 #ONLY ONE TASTE CASE FAILED IN CODE STEP BY STEP

    while dice_sum!=num:
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        dice_sum = dice1 + dice2
        print(f"{dice1} and {dice2} = {dice_sum}")

dice_sum()