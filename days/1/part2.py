def get_dataset() -> list[str]:
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        print(f"Dataset contains {len(lines)} lines.")
        return lines
    print("Failed to read dataset.")
    return []

if __name__ == "__main__":
    data = get_dataset()
    zero_count = 0
    pos = 50
    for line in data:
        data = (line[0], int(line[1:]))

        print(f"{line} \t->{data} \t", end='')

        prev = pos

        if line.startswith("R"):
            pos += data[1]
        elif line.startswith("L"):
            pos -= data[1]

        if pos > 99:
            print(">", end='')
            zero_count += pos // 100
        elif pos <= 0:
            print("<", end='')
            if prev != 0:
                zero_count += (abs(pos)+100) // 100
            else:
                zero_count += abs(pos) // 100
        else:
            print(" ", end='')
        
        print(zero_count)
        
        pos %= 100

        print(f"pos: {pos}")

    print(f"0 count: {zero_count}")