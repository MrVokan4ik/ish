import random
import os
import time
koloda = [6, 7, 8, 9, 10, 11] * 4
discord = [1, 2, 3, 4, 5, 6, 8, 9, 10] * 10

random.shuffle(koloda)
random.shuffle(discord)

print('21 очко')
count = 0
vip = 0
y = 0

print('Black Jack By Mr.Vokan4ik')

menu = int(input('Выберете: \n 1.Игра \n 2.Об игре\n'))
if menu == 1:
    game = input('\nВведите ключ: ')
    if game == 'blackkey' or 'flaconsip':

        igra = input('\nВыберете игру \n 1.BlackJack \n2.Угадай число\n')
        if igra == '1':
                while True:

                    choice = input('\nБудете брать карту? y/n\n')
                    if choice == 'y':
                        current = koloda.pop()
                        print('\nВам попалась карта %d' % current)
                        count += current

                        if count > 21:
                            print('\nИзвените, но вы проиграли!')
                            start = input('Будете играть сново? y/n:\n')
                            if start == 'y':
                                os.startfile('blackjack.exe')
                                break
                            else:
                                break

                    elif count == 21:
                        print('\nПоздравляю, вы набрали 21 очко!')
                        start = input('Будете играть сново? y/n:\n')
                        if start == 'y':
                            os.startfile('blackjack.exe')
                            break
                        else:
                            break

                

                    elif choice == 'n':
                        print('\nУ вас %d очков и вы закончили игру.' % count)
                        start = input('Будете играть сново? y/n:\n')
                        if start == 'y':
                            os.startfile('blackjack.exe')
                            break
                        else:
                            break
                    else:
                        print('У вас %d очков.' % count)
        elif igra == '2':
                x = discord.pop()
                y += x
                vip = input('Введите число от 1 до 10:\n')
                if vip == y :
                    print("Вы угадали число! Это число:\n")
                    print(y)
                
                else:
                    print('Вы не угадали!!! Число:\n')
                    print(y)
        
        else:
            print("Выберите коректное число!!")

    else:
        print('\nКлюч не рабочий или не существует!\nЧерез 5 секунд можно повторить сново.')
        time.sleep(5)
        os.startfile('blackjack.exe')

elif menu == 2:
    print('\nСоздано Mr.Vokan4ik \nВерсия:2.4.0 стабильная \nGitHub:https://github.com/MrVokan4ik/BlackJackByMrVokan4ik')
    time.sleep(30)
