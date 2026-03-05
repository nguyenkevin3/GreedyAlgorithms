import sys
from queue import Queue
from collections import OrderedDict

def fifo(k, requests):
    # To quickly check if item is present in cache
    s = set()

    # Cache with FIFO policy
    cache = Queue()

    number_of_misses = 0

    for request in requests:
        if request not in s: # Cache miss
            if len(s) == k: # If full, evict
                evict = cache.get()
                s.remove(evict)

            number_of_misses += 1
            # Insert item
            cache.put(request)
            s.add(request)

    return number_of_misses



def lru(k, requests):
    # In order from least recently used to most recently used
    cache = OrderedDict()

    number_of_misses = 0

    for request in requests:
        if request not in cache: # Cache miss
            if len(cache) == k: # If full, evict
                cache.popitem(last=False)  # Remove first item (least recently used)

            number_of_misses += 1

            # Insert item, arbitrary value
            cache[request] = 0
        else: # Cache hit, update most recently used
            cache.move_to_end(request)  # End side is most recently used

    return number_of_misses



# Find the request that is farthest in the future among items in the cache
def optff(k, requests):
    # To quickly check if item is present in cache
    s = set()

    # Array to hold items
    cache = []

    number_of_misses = 0

    # Index and value in requests list
    for index, request in enumerate(requests):
        if request not in s: # Cache miss
            number_of_misses += 1
            if len(cache) == k: # If full, replace with new item
                farthestInRequestList = index
                result = -1  # Index of cache item to evict

                # For each item in the cache
                for i in range(len(cache)):
                    j = index

                    # Iterate through requests list starting from index to scan future requests
                    while j < len(requests):
                        if cache[i] == requests[j]:  # Only amongst items currently in the cache
                            if j > farthestInRequestList:
                                farthestInRequestList = j
                                result = i
                            break
                        j += 1

                    # If cache item is never requested again, that is the item to evict
                    if j == len(requests):
                        result = i
                        break

                if result == -1:
                    result = 0


                s.remove(cache[result])

                cache[result] = request
                s.add(request)

            else:
                # Insert item
                cache.append(request)
                s.add(request)

    return number_of_misses



def main():
    filename = sys.argv[1]

    # Reads entire file and splits by whitespace into a list of strings
    with open(filename) as f:
        userinput = f.read().split()

    k = int(userinput[0])  # Cache capacity
    m = int(userinput[1])  # Number of requests

    requests = [] # Sequence of integer IDs

    for i in range(m):
        requests.append(int(userinput[2 + i]))

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

