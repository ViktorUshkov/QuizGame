"""
Мини-проект "Викторина"
"""

if __name__ == '__main__':
    print("Добро пожаловать в викторину!")
    playing: str = input("Хотите ли вы сыграть? Введите 'Y' или 'N': ")
    match playing:
        case 'Y':
            ...
        case 'N':
            print("Увидимся в следующий раз!")
            quit()
        case _:
            ...