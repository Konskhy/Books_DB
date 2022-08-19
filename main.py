import input_menu as menu

print('Welcome to our library!')
while not menu.InputMenu().print_menu():
    continue
