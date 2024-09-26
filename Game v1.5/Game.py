import os
import random
import time
import pyglet
import Save_F
from colorama import *
from colorama import init
init(autoreset=True)


Sys_status = True


class Game_1:
    D_1 = False
    D_2 = False
    D_3 = False

    @staticmethod
    def print_D_stat():
        print(f"Датчик 1: {Fore.LIGHTGREEN_EX + 'Есть' if Game_1.D_1 else Fore.LIGHTRED_EX + 'Пусто'}")
        print(f"Датчик 2: {Fore.LIGHTGREEN_EX + 'Есть' if Game_1.D_2 else Fore.LIGHTRED_EX + 'Пусто'}")
        print(f"Датчик 3: {Fore.LIGHTGREEN_EX + 'Есть' if Game_1.D_3 else Fore.LIGHTRED_EX + 'Пусто'}")

    @staticmethod
    def level_1():
        song_1 = pyglet.media.load('Jump_sc.mp3')
        song_2 = pyglet.media.load('Power_Off.mp3')
        song_3 = pyglet.media.load('End_Night.mp3')

        status_D = True
        Door_status = False
        D_Fall = False

        Game_1.D_1 = False
        Game_1.D_2 = False
        Game_1.D_3 = False

        time_status = 0.5
        power = 100

        def hud(time_status, power):
            print(str(Save_F.lv) + " Ночь")
            print("Время: " + str(time_status) + " Часов(а)")
            print("Энергия: " + str(power) + "%")

        while time_status <= 6:
            hud(time_status, power)
            if not status_D:
                print("Датчики: Выключены")
            else:
                print("Датчики: Включены")
                Game_1.print_D_stat()

            if not D_Fall:
                print(Fore.GREEN + "Датчики: ONLINE")
            else:
                print(Fore.RED + "Датчики: ERROR")
                status_D = False

            if not Door_status:
                print(Fore.GREEN + "Дверь: Открыта")
            else:
                print(Fore.RED + "Дверь: Закрыта")

            if power <= 0:
                print("У вас кончилась энергия")
                song_2.play()
                time.sleep(2.2)
                print(Fore.LIGHTRED_EX + "GAME OVER")
                time.sleep(0.4)
                print("Вы прожили до " + str(time_status) + " Часов")
                Save_F.dead += 1
                input()
                os.system('cls')
                break
            elif time_status == 0.5:
                time.sleep(0.5)
                if Save_F.lv > 1:
                    print("Вы вернулиь? Хорошо... Напоминаю")
                    time.sleep(0.4)
                else:
                    print("Вы новый охранник на складе с аниматраниками")
                    time.sleep(0.4)
                print("Ваша цель: Дожить до 6 утра.")
                time.sleep(0.4)
                print("Правила: Используйте следующие команды:")
                time.sleep(0.2)
                print("Sensor - для включения или выклячения Датчиков")
                print("Door - для открытия или закрытия Двери")
                if Save_F.lv > 1:
                    print("Save_Power - Востановит 10 %")
                print("Reset - для перезапуска Датчиков")
                print("Exit - для Выхода")

            command = input("Введите команду в консоль: ")

            if command == 'Sensor' or command == 'sensor':
                status_D = not status_D
                power -= 5
            elif command == 'Door' or command == 'door':
                Door_status = not Door_status
                power -= 10
            elif command == 'Reset' or command == 'reset':
                print("Reset System...")
                time.sleep(0.35)
                D_Fall = False
                status_D = True
                print("System Online.")
            elif command == 'Save_Power' or command == 'Save' or command == 'save' and Save_F.lv > 1:
                if power <= 100:
                    power += 10
            elif command == 'Exit' or command == 'exit':
                print("Вы хотите выйти в Меню? Y/N")
                ver = input()
                if ver == 'Y' or ver == 'y':
                    os.system('cls')
                    break
                else:
                    time_status -= 0.5
            else:
                print("Вы ждёте...")


            if Save_F.lv <= 6:
                power -= 3
                time.sleep(1)
            elif Door_status == True:
                power -= 15
                time.sleep(1)
            elif status_D == True:
                power -= 5
                time.sleep(1)
            else:
                power -= 1
                time.sleep(1)


            if power > 0:
                time_status += 0.5

            if random.randint(Save_F.a_1, 10) > 6:
                Game_1.D_1 = False
                Game_1.D_2 = True
                Game_1.D_3 = False
            elif random.randint(Save_F.a_1, 7) <= 4:
                Game_1.D_1 = False
                Game_1.D_2 = False
                Game_1.D_3 = True
            else:
                Game_1.D_1 = True
                Game_1.D_2 = False
                Game_1.D_3 = False

            if Game_1.D_3 == True:
                print("К вам кто-то приближается!")
                time.sleep(1.6)
                if not Door_status:
                    time.sleep(1.2)
                    print("Аниматроник зашёл к вам комнату!")
                    song_1.play()
                    time.sleep(4.2)
                    print(Fore.LIGHTRED_EX + "GAME OVER")
                    time.sleep(0.4)
                    print("Вы прожили до " + str(time_status) + " Часов")
                    Save_F.dead += 1
                    input()
                    os.system('cls')
                    break

            if random.randint(1, 9) > 5:
                D_Fall = True
                status_D = False

            print(" ")

            os.system("cls")
        if time_status >= 6 and power > 0:
            print("Смена закончилась!!")
            song_3.play()
            Save_F.lv += 1
            Save_F.a_1 += 1
            pyglet.app.exit()
            input()
            time.sleep(0.55)
            os.system('cls')

    @staticmethod
    def level_2():
        time.sleep(0.5)
        print("Своей ночи нет")
        time.sleep(1.5)
        print("Так как")
        time.sleep(1.5)
        print("Это конец DEMO")
        input()
        os.system('cls')

    def status_U():
        time.sleep(0.5)
        print("Ночь: " + str(Save_F.lv))

        time.sleep(0.4)
        print("Кол-во смертей: " + str(Save_F.dead))
        input("Нажмите 'Enter' что бы вернутся в Меню. ")
        os.system('cls')

    @staticmethod
    def main():
        time.sleep(1.5)
        print("Five Nights in a Warehouse")
        print("For Python")
        time.sleep(0.6)
        print("1.New Game")
        time.sleep(0.4)
        print("2.Continue: " + str(Save_F.lv) + " Ночь")
        time.sleep(0.4)
        print("3.Статистика")
        time.sleep(0.4)
        print("4.Exit")
        time.sleep(0.4)
        c = input("Команда: ")
        os.system('cls')

        if c == '1':
            Save_F.lv = 1
            Save_F.dead = 0
            Game_1.level_1()
        elif c == '2':
            if Save_F.lv == 6:
                Game_1.level_2()
            else:
                Game_1.level_1()
        elif c == '3':
            Game_1.status_U()
        else:

            global Sys_status
            Sys_status = not Sys_status




def Load():
    print('....Запуск программы....')
    progressbar = ["▒▒▒▒▒▒▒▒▒▒",  # 0-10%[0]
                   "█▒▒▒▒▒▒▒▒▒",  # 10-20%[1]
                   "██▒▒▒▒▒▒▒▒",  # 20-30%[2]
                   "███▒▒▒▒▒▒▒",  # 30-40%[3]
                   "████▒▒▒▒▒▒",  # 40-50%[4]
                   "█████▒▒▒▒▒",  # 50-60%[5]
                   "██████▒▒▒▒",  # 60-70%[6]
                   "███████▒▒▒",  # 70-80%[7]
                   "████████▒▒",  # 80-90%[8]
                   "█████████▒",  # 90-99%[9]
                   "██████████"]  # 99-100%[10]

    for i in range(101):
        time.sleep(0.06)

        if i < 10:
            print('\r', progressbar[0], str(i), "%", end='')
        if 10 < i < 20:
            print('\r', progressbar[1], str(i), "%", end='')
        if 20 < i < 30:
            print('\r', progressbar[2], str(i), "%", end='')
        if 30 < i < 40:
            print('\r', progressbar[3], str(i), "%", end='')
        if 40 < i < 50:
            print('\r', progressbar[4], str(i), "%", end='')
        if 50 < i < 60:
            print('\r', progressbar[5], str(i), "%", end='')
        if 60 < i < 70:
            print('\r', progressbar[6], str(i), "%", end='')
        if 70 < i < 80:
            print('\r', progressbar[7], str(i), "%", end='')
        if 80 < i < 90:
            print('\r', progressbar[8], str(i), "%", end='')
        if 90 < i < 100:
            print('\r', progressbar[9], str(i), "%", end='')
        if i == 100:
            print('\r', progressbar[10], str(i), "%", end='')

    input('\nЗагрузка завершена')
    os.system('cls')
    print(Fore.LIGHTRED_EX + "Внимание!!")
    time.sleep(1.5)
    print(Fore.LIGHTRED_EX + "Данная игра содержит ГРОМКИЕ ЗВУКИ!")
    time.sleep(1.6)
    print(Fore.LIGHTGREEN_EX + "Для полного экпирианса НАДЕНЬТЕ НАУШНИКИ")
    input()



if Save_F.lv > 6:
    Save_F.lv -= 1
Load()

os.system('cls')
time.sleep(1.3)
while Sys_status == True:
    Game_1.main()

    if Sys_status == False:
        print("Учьтите!! Ваш прогрес после выхода НЕ сохранится.")
        time.sleep(1)
        print("Спасибо за игру!")
        break
