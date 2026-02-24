import sys

def fifo(k, requests):
    pass

def lru(k, requests):
    pass

def optff(k, requests):
    pass

def main():
    filename = sys.argv[1]

    # Reads entire file and splits by whitespace into a list of strings
    with open(filename) as f:
        input = f.read().split()

    k = int(input[0])  # Cache capacity
    m = int(input[1])  # Number of requests

    requests = [] # Sequence of integer IDs

    for i in range(m):
        requests.append(int(input[2 + i]))

    FIFO_misses = fifo(k, requests)

    LRU_misses = lru(k, requests)

    OPTFF_misses = optff(k, requests)

    outputfile = filename.replace(".in", ".out")

    with open(outputfile, "w") as f:
        f.write(f"FIFO  : {FIFO_misses}\n")
        f.write(f"LRU   : {LRU_misses}\n")
        f.write(f"OPTFF : {OPTFF_misses}\n")


if __name__ == '__main__':
    main()

