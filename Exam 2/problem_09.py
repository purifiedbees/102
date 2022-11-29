# Helper variables
item_name = ""
item_cost = -1

# # Open the file and read
with open("item_cost.dat", "r") as file:
    file.readline()

    for line in file:
        name, cost = line.split(",")
        cost = float(cost)

        # Compare and replace
        if item_cost == -1 or item_cost > cost:
            item_name, item_cost = name, cost

# Output
print(f"The cheapest item is {item_name}. It costs ${item_cost}.")