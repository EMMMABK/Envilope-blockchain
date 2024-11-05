from hashlib import sha256

def updatehash(*args):
    for arg in args:
        print(arg)

updatehash("hello", "two", 5)

class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number


class Blockchain():
    pass

def main():
    pass