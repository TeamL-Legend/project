from prolouge import *

print()
print(colored("Регистрация", 'red'))
print(colored("-----------", 'red'))
auth = input("Логин: ")
auth_pass = input("Пароль: ")
auth_len = len(auth)
auth_pass_len = len(auth_pass)

if auth_len == 0 or auth_pass_len == 0:
    print("Полля ввода не должны быть пустыми")
else:
    print()
    print(colored("Уcпешно: " + auth + " " + auth_pass, 'green'))
    print()
    mainoption = input(colored("Выбери как развлечся | Угадай число-1 | Квест-2 | Пифагор-3 | : ", 'black'))
#_________________________________________________

    if mainoption == "1":
        print(colored("Авторизуйтесь", 'red'))
        check_auth = input("Логин: ")
        check_auth_pass = input("Пароль: ")

        if check_auth != auth:
            print("Неверный логин")
        if check_auth_pass != auth_pass:
            print("Неверный пароль")
        else:
            print("Угадай число")
            print()
            let_s_go = input("Чтобы начать, напиши, Начать: ")
            if let_s_go == "Начать":
                print()
                answer = False
                secret_number = 77
                while not answer:
                    user_input = input("Введите ваше предположение: ")
                    guess = int(user_input)
                    if guess < secret_number:
                       print("Слишком маленькое число!")
                    elif guess > secret_number:
                       print("Слишком большое число!")
                    else:
                       guessed = True
                       print("Поздравляю! Вы угадали число", secret_number)
#_________________________________________________
    elif mainoption == "2":
        print(colored("Авторизуйтесь", 'red'))
        check_auth = input("Логин: ")
        check_auth_pass = input("Пароль: ")

        if check_auth != auth:
            print("Неверный логин")
        if check_auth_pass != auth_pass:
            print("Неверный пароль")
        else:
            print()
            choise_1 = input("Вы очнулись, вы злы и хотите выбраться отсюда, начать приключение? "+"|"+(colored("Да", 'green'))+"|"+(colored("Нет", 'red'))+"|: ")
            if choise_1 == "Да":
                print(prologue)
                choise_2 = input("Начать? " +"|"+(colored("Да", 'green'))+"|"+(colored("Нет", 'red'))+"|: ")
                print()
                if choise_2 == "Да":
                    print(choise_2_option_1)
                    print(choise_2_option_2)
                    print(choise_2_option_3)
                    print()
                    choise_3 = input(colored("Каков твой выбор, попытаться выломать окно, дверь или поспать на кровати? |1|2|3|: ", 'black'))
                    print()
                    if choise_3 == "1":
                        print(choise_3_answer_1)
                        print()
                        choise_4 = input("Пойти, в качалку или искать набор инструментов? |Качалка|Инструменты|: ")
                        print()
                        if choise_4 == "Качалка":
                            print(choise_4_answer_1)
                        elif choise_4 == "Инструменты":
                            print(choise_4_answer_2)
                    elif choise_3 == "2":
                        print(choise_3_answer_2)
                        print()
                    elif choise_3 == "3":
                        print(choise_3_answer_3)
                        print()
                        choise_5 = input("У тебя есть оружие, ты хочешь вернутся в качалку? |Да|Нет|: ")
                        print()
                        if choise_5 == "Да":
                            print("Вы чувстыуете себя уверенно")
                            print(cs)
                        elif choise_5 == "Нет":
                            print("Вы собираетесь духом")
                            print(cs)
                    else:
                        print(wrongoption)
                elif choise_2 == "Нет":
                            print(bb)
                else:
                    print(wrongoption)
            elif choise_1 == "Нет":
                print(bb)
            else:
                print(wrongoption)
#________________________________________               

    elif mainoption == "3":
        print(colored("Авторизуйтесь", 'red'))
        check_auth = input("Логин: ")
        check_auth_pass = input("Пароль: ")

        if check_auth != auth:
            print("Неверный логин")
        if check_auth_pass != auth_pass:
            print("Неверный пароль")
        else:
            choise_3_main = input("1 - bmi, 2 - Пифагор, 3 - Виета: ")
            if choise_3_main == "1":
                wheight = int(input("Вес: "))
                height = int(input("Рост: "))
                bmi = wheight / (height/100)**2
                print(float(bmi))
            elif choise_3_main == "2":
                a = int(input("катет_a: "))
                b = int(input("катет_b: "))
                c = (a * a + b * b) ** 0.5
                print("гипотенуза", float(c))
            else:
                if choise_3_main == "3":
                    print("нельзя юзать math :(")
    else:
        print(wrongoption)
#________________________________________   