import time
import hashlib


class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hashlib.sha256(str(self.index) + self.previous_hash + str(self.timestamp) + self.data).hexdigest()


def main():
    block1 = Block(0, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', time.time(), 'Hello friend')
    print block1.hash


if __name__ == '__main__':
    main()
