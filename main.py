import textwrap

def menu():
    menu = """
        MY TO-DO APP
        
        [+] Add task
        [-] Remove task
        [C] Done task
        [V] Review
        [q] Quit
        => """
    return input(textwrap.dedent(menu))

def main():
    opcao = input(menu())

main()