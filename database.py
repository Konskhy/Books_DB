import json


with open('books.json', 'r') as file:
    books = json.load(file)
    print(books)


def _save():
    with open('books.json', 'w') as file:
        json.dump(books, file)


def add_book(title, author):
    book = {'title': title, 'author': author, 'read': False}
    books.append(book)
    _save()


def list_books():
    for book in books:
        print(f'"{book["title"]}" by {book["author"]} \tread:{book["read"]}')
    print()


def mark_read(title):
    book = search(title)
    book['read'] = True
    _save()


def remove_book(title):
    book = search(title)
    books.remove(book)
    _save()


def search(title):
    for book in books:
        if book['title'] == title:
            return book

