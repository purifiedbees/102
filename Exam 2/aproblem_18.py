import random

# Set up warriors
warrior_1 = {"CRIT": 0, 
             "ARMOR": 0,
             "MIN": 0,
             "MAX": 0,
             "EVASION": 0,
             "HP": 0,
             "NAME": "WARRIOR 1"}

warrior_2 = {"CRIT": 0, 
             "ARMOR": 0,
             "MIN": 0,
             "MAX": 0,
             "EVASION": 0,
             "HP": 0,
             "NAME": "WARRIOR 2"}

# Get input for warrior 1
print("WARRIOR 1")
warrior_1["CRIT"] = int(input("Enter crit percentage: "))
warrior_1["ARMOR"] = int(input("Enter armor percentage: ")) / 100
warrior_1["MIN"] = int(input("Enter minimum attack: "))
warrior_1["MAX"] = int(input("Enter maximum attack: "))
warrior_1["EVASION"] = int(input("Enter evasion chance: "))
warrior_1["HP"] = int(input("Enter health pool: "))

# Get input for warrior 2
print("WARRIOR 2")
warrior_2["CRIT"] = int(input("Enter crit percentage: "))
warrior_2["ARMOR"] = int(input("Enter armor percentage: ")) / 100
warrior_2["MIN"] = int(input("Enter minimum attack: "))
warrior_2["MAX"] = int(input("Enter maximum attack: "))
warrior_2["EVASION"] = int(input("Enter evasion chance: "))
warrior_2["HP"] = int(input("Enter health pool: "))

# Main loop
turn = 0

while warrior_1["HP"] > 0 and warrior_2["HP"] > 0:
    print("+----------------------------+")
    print(f"HEALTH POOLS AFTER ROUND {turn+1}:\nWARRIOR 1: {warrior_1['HP']}\nWARRIOR 2: {warrior_2['HP']}")
    print("+----------------------------+")

    # Turn logic
    attacker = warrior_1 if turn % 2 == 0 else warrior_2
    defender = warrior_2 if turn % 2 == 0 else warrior_1
    atk_name = attacker["NAME"]
    def_name = defender["NAME"]

    print(f"Now {atk_name} attacks {def_name}!")

    # Check evasion
    evasion_roll = random.randint(1, 100)
    if 1 <= evasion_roll <= defender["EVASION"]:
        print(f"{def_name} evades!")
        turn += 1
        continue

    # Calculate the raw damage
    damage = random.randint(attacker["MIN"], attacker["MAX"])

    # Include crit if able
    crit_roll = random.randint(1, 100)
    if 1 <= crit_roll <= attacker["CRIT"]:
        print(f"{atk_name} crits!")
        damage *= 1.5

    # Reduce damage based on armor
    damage *= (1 - defender["ARMOR"])

    # Output the actual calculation
    print(f"{atk_name} deals {damage} point(s) to {def_name}")

    # Check for kill
    if damage >= defender["HP"]:
        print(f"{atk_name} wins!")

    # Do damage
    defender["HP"] -= damage

    # Next turn
    turn += 1
