

choices = {"Print":print}

def MainMenu():
    Loop = True
    while Loop:
        choice = input("""Options:
        Print
        """)
        choices[choice]("hello")


MainMenu()