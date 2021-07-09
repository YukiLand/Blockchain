from pathlib import Path

class Block:

    def __init__(self, name, base_hash, hash, parent_hash, transactions):
        self.name = name
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = transactions

    def checkSize(self):
        if Path('../content/' + self.name + '.txt').stat().st_size > 256000 :
            pass

