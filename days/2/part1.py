def get_dataset() -> list[tuple[int, int]]:
    with open("input.txt", "r") as f:
        values = [
            val.split('-')
            for val in f.read().replace("\n", "").split(",")
        ]
        values = [
            (int(val[0]), int(val[1]))
            for val in values
        ]
        print(f"Dataset contains {len(values)} values.")
        return values
    print("Failed to read dataset.")
    return []

def isInvalid(input: str) -> bool:
    length = len(input)
    halfLen = length // 2
    return input[:halfLen] == input[halfLen:]

def get_invalids(start: int, end: int) -> list[int]:
    invalids = []
    for i in range(start, end + 1):
        if isInvalid(str(i)):
            invalids.append(i)
    return invalids

if __name__ == "__main__":
    dataset = get_dataset()
    print(dataset)

    invalids = []

    for valRange in dataset:
        print(f"from {valRange[0]} to {valRange[1]}: ", end='')
        rangeInvalids = get_invalids(valRange[0], valRange[1])
        invalids.extend(rangeInvalids)
        print(', '.join([str(v) for v in rangeInvalids]))

    print(f"Invalids sum: {sum(invalids)}")
