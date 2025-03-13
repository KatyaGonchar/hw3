# YAML

import yaml

filename = "books.yaml"


def create_yaml(filename):
    data = [
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "Shantaram", "author": "Gregory David Roberts", "year": 2003},
        {"title": "11/22/63", "author": "Stephen King", "year": 2011}
    ]

    try:
        with open(filename, "w") as file:
            yaml.dump(data, file)
            print(f"YAML file '{filename}' was created.")
    except Exception as e:
        print(f"Error: {e}")


def read_and_add_books(filename):
    try:
        with open(filename, "r") as file:
            books = yaml.load(file, Loader=yaml.FullLoader)

        print("Registered books list:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

        add_new_book = input("Do you want to add a book? (Y/N): ").upper()
        if add_new_book == 'Y':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))

            books.append({"title": title, "author": author, "year": year})

            with open(filename, "w") as file:
                yaml.dump(books, file, default_flow_style=False)
            print(f"The book '{title}' was added.")
        else:
            print("Exiting.")

    except Exception as e:
        print(f"Error: {e}")


create_yaml(filename)
read_and_add_books(filename)
