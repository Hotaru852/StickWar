from queue import Empty
from src.config import *


class file_manager:
    def __init__(self):
        self.path = database_path

    def load(self):
        f = open(self.path, "r")
        accounts = []
        while True:
            check = f.readline()
            if check == '':
                break
            else:
                informations = list(check.split())
                informations.append(list(f.readline().split()))
                accounts.append(informations)
        f.close()
        return accounts

    def save(self, accounts):
        f = open(self.path, "w")
        for account in accounts:
            f.write(' '.join(str(x) for x in account[0:6]) + "\n")
            if account[6] is not Empty:
                f.write(' '.join(str(x) for x in account[6]) + "\n")
            else:
                f.write("\n")
        f.close()