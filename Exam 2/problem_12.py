# Match characters with numbers
phone_map = {"ABC": "2", "DEF": "3", "GHI": "4", "JKL": "5", "MNO": "6", "PQRS": "7", "TUV": "8", "WXYZ": "9"}

# Get input
phone_number = input("Enter the phone number: ")
front, back = phone_number.split("-")

# Convert
back = list(back)

for char_index in range(len(back)):
    char = back[char_index].upper()

    for key in phone_map.keys():
        if char in key:
            back[char_index] = phone_map[key]

# Output
full_number = list(front) + back
part_one, part_two, part_three = "".join(full_number[0:3]), "".join(full_number[3:6]), "".join(full_number[6:])

print(f"{phone_number} is equivalent to {part_one}-{part_two}-{part_three}")