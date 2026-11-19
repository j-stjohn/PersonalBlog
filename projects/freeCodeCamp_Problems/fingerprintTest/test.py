def checkCase(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return 0
    else:
        if fingerprint_a.islower() == True and fingerprint_b.islower() == True:
            return 1
        return -1


def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    counter = 0
    iterator = 0
    for i in fingerprint_b:
        if i == fingerprint_a[iterator]:
            counter += 1
        iterator += 1
    matchRate = counter / len(fingerprint_a)
    if matchRate >= 0.9:
        return True
    else:
        return False

def main(fingerprint_a, fingerprint_b):
    if checkCase(fingerprint_a, fingerprint_b) == 1:
        return is_match(fingerprint_a, fingerprint_b)
    else:
        return False