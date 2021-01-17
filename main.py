import random

ACTIONS = ('+', '-')
LIMIT = 10
AMOUNT_OF_QUESTIONS = 10


def get_action() -> str:
    return random.choice(ACTIONS)


def main() -> None:
    start = input("Добрый день! Давай с тобой позанимаемся! Напиши да или нет: ")
    while start not in ('да', 'нет'):
        start = input("Не понимаю тебя! Напиши да или нет: ")
    if start == 'нет':
        return
    amount_true_answers = 0
    for i in range(AMOUNT_OF_QUESTIONS):
        action = get_action()
        first_digit = random.randint(0, LIMIT)
        if action == '+':
            second_digit = random.randint(0, LIMIT - first_digit)
            result_calc = first_digit + second_digit
        elif action == '-':
            second_digit = random.randint(0, first_digit)
            result_calc = first_digit - second_digit
        else:
            print('Неизвестное действие. Попробуйте запустить меня еще раз')
            return
        result_int = -1
        first_true_answer = True
        while result_int != result_calc:
            while result_int not in range(11):
                result_str = input(f'{first_digit} {action} {second_digit} = ')
                try:
                    result_int = int(result_str)
                except ValueError:
                    print('Введите число от 0 до 10')
                if result_int not in range(11):
                    print('Введите число от 0 до 10')
            if result_int == result_calc:
                print('Молодец, верно')
            else:
                print('Нет, не правильно. Попробуй еще раз')
                result_int = -1
                first_true_answer = False
        if first_true_answer:
            amount_true_answers += 1
    print(f'Твой итоговый результат {amount_true_answers} баллов из {AMOUNT_OF_QUESTIONS}')
    input('Нажми любую кнопку для завершения')


if __name__ == '__main__':
    main()
