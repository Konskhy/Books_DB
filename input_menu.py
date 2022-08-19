import database as db


class InputMenu:
    def __init__(self):
        self.menu = {1: ('Add book', self.add_book),
                     2: ('List books', self.list_books),
                     3: ('Mark as read', self.mark_read),
                     4: ('Remove book', self.remove_book),
                     5: ('Search', self.search_menu),
                     0: ('Quit', None)}

    @staticmethod
    def add_book():
        title = input('Enter books title: ')
        author = input('Enter books author: ')
        db.add_book(title, author)

    @staticmethod
    def list_books():
        db.list_books()

    @staticmethod
    def mark_read():
        db.mark_read(input('Enter books title:'))

    @staticmethod
    def remove_book():
        db.remove_book(input('Enter books title:'))

    @staticmethod
    def search_menu():
        db.search(input('Enter title: '))

    def print_menu(self):
        for key, val in self.menu.items():
            print(f'{key}. {val[0]}')
        user_input = int(input('Please choose an option: '))
        if user_input == 0:
            return True
        else:
            f = self.menu[user_input][1]
            f()
