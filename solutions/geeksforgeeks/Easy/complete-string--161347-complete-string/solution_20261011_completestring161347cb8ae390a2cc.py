import string
def completeString(s):
    return set(string.ascii_lowercase).issubset(set(s))
