import random
import time

import pyinputplus as pyip

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    # Выбираем два случайных числа
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = "#%s: %s x %s = " % (question_number, num1, num2)
    try:
        # Правильные ответы задаются аргументом allowRegexes
        # Неправильные ответы задаются аргументом blockRegexes
        # В случае неправильного ответа отображается пользовательское сообщение
        pyip.inputStr(prompt, allowRegexes=["^%s$" % (num1 * num2)],
                      blockRegexes=[(".*", "Неправильно!")],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Время истекло!")
    except pyip.RetryLimitException:
        print("Закончилось количество попыток!")
    else:
        # Этот блок выполняется, если в блоке try не возникло исключений
        print("Правильно!")
        correct_answers += 1
    time.sleep(1)  # короткая пауза, позволяющая пользователю увидеть результат

print("Счёт: %s/%s" % (correct_answers, number_of_questions))
