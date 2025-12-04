def get_dataset() -> list[str]:
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        print(f"Dataset contains {len(lines)} lines.")
        return lines
    print("Failed to read dataset.")
    return []

if __name__ == "__main__":
    data = get_dataset()
    pos_count = [0] * 100
    pos = 50
    for line in data:
        data = (line[0], int(line[1:]))
        if line.startswith("R"):
            pos += data[1]
        elif line.startswith("L"):
            pos -= data[1]
        pos %= 100
        pos_count[pos] += 1
        print(f"{line} \t->{data}\tpos: {pos}")

    print("Position counts:")
    for i, count in enumerate(pos_count):
        print(f"Position {i}: {count}")
    print(f"0 visits: {pos_count[0]}")