import dice

dice_results = []

for i in range(0,2):
    x = dice.dice_roll()
    dice_results.append(x)
    print(dice_results)

#roll_1 = dice.dice_roll()
#roll_2 = dice.dice_roll()

#print(f"You have rolled a {roll_1} and {roll_2} which have a sum of {roll_1 + roll_2} and a product of {roll_1 * roll_2}.")