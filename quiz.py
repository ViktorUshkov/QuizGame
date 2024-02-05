"""
Мини-проект "Викторина"
"""
from random import sample

# список вопросов для викторины: первое значение в кортеже - вопрос, второе - ответ
QUESTIONS = [
    ("Столица Португалии?", "Лиссабон"),
    ("Чемпион мира по футболу 2022 года?", "Аргентина"),
    ("Устройство, с помощью которого производится ввод данных на компьютере?", "клавиатура"),
    ("Какой металл является самым тугоплавким?", "вольфрам"),
    ("На флаге какой страны изображен черный двуглавый орел на красном фоне?", "Албания"),
    ("Какой псевдоним у музыканта по имени Маршалл Мэтерс? (ввод латиницей)", "Eminem"),
    ("Какой подзаголовок имеет вторая часть фильма 'Мстители'?", "Эра Альтрона"),
    ("Как назывался фильм, в котором Дэниэл Крейг впервые сыграл Джеймса Бонда?", "Казино Рояль"),
    ("Джоуи, Росс, Моника, Фиби, Рейчел. Назовите шестого", "Чендлер"),
    ("Сборную какой страны обыграла сборная России в финале олимпийского турнира по хоккею 2018 года?", "Германия"),
    ("Какой код имеет аэропорт Домодедово?", "DME"),
    ("В какой части трилогии Кристофера Нолана о Бэтмене Хит Леджер сыграл Джокера?", "Тёмный рыцарь"),
    ("В какой вид спорта играют волшебники во вселенной Гарри Поттера?", "квиддич"),
    ("Какой фильм стал первой картиной не на английском языке, получившей «Оскар» в категории «Лучший фильм»", "Паразиты"),
    ("Назовите третью цифру после запятой числа пи", "1")
]
# количество вопросов, которое будет задано в течение одной игры
QUESTIONS_IN_GAME = 5

def ask_questions() -> int:
    """
    Функция для проведения викторины. Игрок получает пять случайных вопросов: если он отвечает правильно - его счёт (score)
    увеличивается. В конце работы функция возвращает итоговый счёт игрока

    :return: количество вопросов, на которые игрок ответил правильно
    """
    # счёт игрока
    score: int = 0
    # номера вопросов, которые будут заданы в течение игровой сессии
    questions: list[int] = sample(range(len(QUESTIONS)), QUESTIONS_IN_GAME)
    for question in questions:
        # выводим вопрос по индексу question и получаем ответ игрока
        get_answer: str = input(f"{QUESTIONS[question][0]} ")
        # сравниваем ответ игрока с правильным: если ответ верный - увеличиваем счёт игрока
        if get_answer.lower() == QUESTIONS[question][1].lower():
            print("Правильно!")
            score += 1
        else:
            print("Неправильно :(")

    return score

def game_cycle() -> None:
    """
    Основной цикл игры-викторины. Программа спрашивает, хочет ли игрок сыграть и в зависимости от ответа либо начинает
    викторину, либо заканчивает работу, либо просит повторить ввод
    """
    while True:
        # переменная, отображающая статус игрока
        playing: str = input("Хотите ли вы сыграть? Введите 'Y' или 'N': ")
        match playing:
            case 'Y':
                print("Игра начинается! Вводите ответы в именительном падеже, если не сказано иного")
                score: int = ask_questions()
                print(f"Количество правильных ответов: {score}. Вы можете попробовать свои силы снова.")
            case 'N':
                print("Увидимся в следующий раз!")
                quit()
            case _:
                print("Ваш ответ не ясен программе: нужно ввести либо 'Y', либо 'N'. Попробуйте ещё раз.")

if __name__ == '__main__':
    print("Добро пожаловать в викторину!")
    game_cycle()
