import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Generator:
    def __init__(self):
        self.password_list = []
        self.password = ""

    def create(self):
        nr_letters = random.randint(8, 10)
        nr_numbers = random.randint(2, 4)
        nr_symbols = random.randint(2, 4)

        self.password_list += [random.choice(LETTERS) for _ in range(nr_letters)]
        self.password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]
        self.password_list += [random.choice(NUMBERS) for num in range(nr_numbers)]

        # for num in range(nr_letters):
        #     self.password_list += random.choice(LETTERS)
        # for num in range(nr_symbols):
        #     self.password_list += random.choice(SYMBOLS)
        # for num in range(nr_numbers):
        #     self.password_list += random.choice(NUMBERS)

        random.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        # for char in self.password_list:
        #     self.password += char
