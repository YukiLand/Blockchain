import uuid
import json


class Wallet:

    def generate_uuid(self):
        unique_id = uuid.uuid4()
        return unique_id

    def __init__(self, balance, history):
        self.balance = balance
        self.history = history

    def add_balance(self, balance, addingValue):
        self.balance = balance + addingValue
        return self.balance

    def sub_balance(self, balance, subValue):
        self.balance = balance + subValue
        return self.balance

    def send(self):
        pass

    def save(self):
        with open("../content/wallets/{}.json".format(self.unique_id), "x") as file:
            file.write(json.dumps({"id": self.unique_id, "balance": self.balance, "history": self.history}))



