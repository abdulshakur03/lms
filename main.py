import json
import shutil
import os
from datetime import datetime, timezone


def load_data(file):
    data = []
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found")
    except json.decoder.JSONDecodeError:
        timestamp = datetime.now(timezone.utc).strftime("%y%m%d_%H%M%S")
        print(f"Broken json file: {file}")
        os.makedirs("backups", exist_ok=True)
        print("Directory tree 'backups' is ready.")
        copied_path = shutil.copy(file, f"backups/data_{timestamp}.json")
        print(f"File {file} copied to: {copied_path}")
    except OSError as error:
        print(f"Directory creation failed: {error}")

    return data


def main():

    file = "data.json"
    data = load_data(file)
    # print(data)

    class Book:
        def __init__(self):
            self.title = title
            self.author = author

        @staticmethod
        def get_input(text):
            while True:
                prompt = input(text).strip()
                if prompt == "":
                    print("Input cannot be empty")
                else:
                    return prompt

        @staticmethod
        def get_int_input(self, text):
            while True:
                try:
                    int_prompt = int(self.get_input(text))
                    if int_prompt < 0:
                        print("Negative numbers are not allowed")
                    else:
                        return int_prompt
                except ValueError:
                    print("Value must be a whole number")

        @staticmethod
        def add_book(self):
            title = self.get_input("Enter book title: ")
            author = self.get_input("Enter author's name: ")
            isbn = ""
            available = True
            data.append(
                {title: title, author: author, available: available, isbn: isbn}
            )

    b1 = Book()
    b1.add_book()
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
