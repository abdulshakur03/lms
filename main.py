import json

file = "data.json"
try:
    with open(file, "r") as f:
        data = json.load(f)
        # print(data)
except FileNotFoundError:
    print(f"File '{file}' not found")
except json.decoder.JSONDecodeError:
    print(f"Broken json file: {file}")


data = []


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_input(self, text):
        while True:
            prompt = input(text).strip()
            if prompt == "":
                print("Input cannot be empty")
            else:
                return prompt

    def get_int_input(self, text):
        while True:
            try:
                return int(self.get_input(text))
            except ValueError:
                print("Value must be a number")

    def add_book(self):
        pass


b1 = Book("GOT", "Lasisi")
number = b1.get_int_input("Input text: ")
digit = b1.get_int_input("Input a number: ")

with open(file, "w") as f:
    json.dump(data, f)
