# SRP or SOC says the each calss must be responsible only and only for the one job NOT more
class Jurnal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}:{text}')

    def remove(self, id):
        del self.entries[id]


    def __str__(self) -> str:
        return '\n'.join(self.entries)
    # So far the class jus dead with creating a new entry for jurnal
    # ==================================================================================

    # Now adding the ability to save/load is somthing else and breaks the rule.

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()


    # def load(self, filename):
    #     file = open(filename, 'r')
    #     file.close
#=========================================================================================

# The way that we should deal with such issuse is like below:

class saveManager:

    @staticmethod
    def save(jurnal, filename):

        file = open(filename, 'w')
        file.write(str(jurnal))
        file.close()


j = Jurnal()
#j.add_entry("من بهنام شاکرمی هستم و خوشحالم که داری اینا رو میخونی امیدوارم بهت گمک کنه:))")

j.add_entry("Hi")

file = r'./text.txt'

saveManager.save(j, file)

with open(file) as r:
    print(r.read())
