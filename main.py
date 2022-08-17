import json


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.read = False


with open('books.json', 'r') as _:
    book_list = json.load(_)
    print(book_list)


def add_book():
    title = input("Please enter book's title: ")
    author = input("Please enter book's author: ")
    book = Book(title, author)
    book_list.append(book.__dict__)
    with open('books.json', 'w') as file:
        json.dump(book_list, file)


def remove_book():
    pass


def list_books():
    for book in book_list:
        print(f'"{book["name"]}" by {book["author"]}')
    print()


def mark_read():
    pass


print('Welcome to our library!')
menu = {1: ('Add book', add_book),
        2: ('Remove book', remove_book),
        3: ('List books', list_books),
        4: ('Mark book as read', mark_read),
        0: ('Quit', None)
        }

while True:
    for key, val in menu.items():
        print(f'{key}. {val[0]}')
    user_input = int(input('Please choose an option: '))
    if user_input == 0:
        break
    else:
        f = menu[user_input][1]
        f()
