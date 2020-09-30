import hashlib
import random
import string
def find_collision(n):
    n=2
    counter = 0
    dict = {}
    test = False
    while not test:
        x = hashlib.sha256()
        new_string = ''.join(random.choice(string.printable) for i in range(random.randint(1, 32)))
        x.update(new_string.encode("ascii"))
        result = x.digest()
        if result[:n] not in dict:
            counter += 1
            dict[result[:n]] = new_string;
        elif new_string != dict[result[:n]]:
            print(counter)
            return new_string, dict[result[:n]]