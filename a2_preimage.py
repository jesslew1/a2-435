import hashlib
import random
import string
def find_preimage(target, n):
    n =2
    counter = 0
    test = False
    while not test:
        x = hashlib.sha256()
        new_string = ''.join(random.choice(string.printable) for i in range(random.randint(1, 32)))
        x.update(new_string.encode("ascii"))
        result = x.digest()
        if result[:n] == target[:n]:
            counter += 1
            print(counter)
            return new_string
        