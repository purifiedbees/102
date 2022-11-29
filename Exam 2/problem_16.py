# Helper function
def process_line(line: str, changeToFloat: bool) -> list[str]:
    items = line.split(" ")

    # CLean items
    for i in range(len(items)-1, -1, -1):
        items[i] = items[i].strip()

        # If not an actual item, remove
        if items[i] == "":
            items.pop(i)
        elif changeToFloat:
            items[i] = float(items[i])

    return items

# Read the file
with open("peanut.dat", "r") as f:
    # Use first line to grab headers
    headers = process_line(f.readline(), False)
    headers.append("Ratio")

    # Start output
    print(f"{' '.join(headers)}")

    # Extract the data
    for line in f:
        values = process_line(line, True)
        ratio = values[1] / values[2]

        # Output
        print(f"{int(values[0]):^6} {values[1]:^8.2f} {values[2]:^8.2f} {ratio:^5.2f}")