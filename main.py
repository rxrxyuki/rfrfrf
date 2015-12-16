import exp_calc
import monk
import barbarian
import crusader

lvl_input = float(input("What is the level you want to calculate experience from? \n"),)

if lvl_input < 1:
    print("You cannot go below Level 1.")
    quit()


exp = exp_calc.exp_calculation(lvl_input)

print("")
print("Result:")
print("Required exp for level", lvl_input, ":", exp)
print("")

level = exp_calc.level_calculation(exp)


cls_input = str(input("Which class do you like for your level input? \n",))

if cls_input.lower() in ["monk"]:
    monk_attack = monk.attack_calculation(level)
    monk_defense = monk.defense_calculation(level)
    monk_speed = monk.speed_calculation(level)
    print("")
    print("Your character statistics are as follows:")
    print("Your character Level is:", level)
    print("Your character Attack stat is:", monk_attack)
    print("Your character Defense stat is:", monk_defense)
    print("Your character Speed stat is:", monk_speed)

elif cls_input.lower() in ["barbarian"]:
    barbarian_attack = barbarian.attack_calculation(level)
    barbarian_defense = barbarian.defense_calculation(level)
    barbarian_speed = barbarian.speed_calculation(level)
    print("")
    print("Your character statistics are as follows:")
    print("Your character Level is:", level)
    print("Your character Attack stat is:", barbarian_attack)
    print("Your character Defense stat is:", barbarian_defense)
    print("Your character Speed stat is:", barbarian_speed)

elif cls_input.lower() in ["crusader"]:
    crusader_attack = crusader.attack_calculation(level)
    crusader_defense = crusader.defense_calculation(level)
    crusader_speed = crusader.speed_calculation(level)
    print("")
    print("Your character statistics are as follows:")
    print("Your character Level is:", level)
    print("Your character Attack stat is:", crusader_attack)
    print("Your character Defense stat is:", crusader_defense)
    print("Your character Speed stat is:", crusader_speed)

else:
    print("Your input doesn't correspond to a class.")
