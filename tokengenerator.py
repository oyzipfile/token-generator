#как по мне говно код но мне похуй :troll:
import random
import time
import colorama
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321__-"
chars2 = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
colorama.init()
laung = input("Language [RU/EN] :  ")
print(f"""{colorama.Fore.MAGENTA}
 _______ _______ ___   _ _______ __    _ 
|       |       |   | | |       |  |  | |
|_     _|   _   |   |_| |    ___|   |_| |
  |   | |  | |  |      _|   |___|       |
  |   | |  |_|  |     |_|    ___|  _    |
  |   | |       |    _  |   |___| | |   |
  |___| |_______|___| |_|_______|_|  |__|   
                        by pighax

 """)
laung = input("Language [RU/EN] :  ")
if laung != "RU" and laung != "EN" and laung != "ru" and laung != "en":
    print(f"""{colorama.Fore.RED}
ERROR/ОШИБКА """)
    time.sleep(3)
    exit()

if laung=="RU" or laung=="ru":
    rang = int(input("Введите количество токенов: "))

if laung=="EN" or laung=="en":
    rang = int(input("Enter the number of tokens: "))

if laung=="RU" or laung=="ru":
    for iru in range(rang):
        ch2 = ''.join((random.choice(chars2) for iru in range (3)))
        odin = ''.join((random.choice(chars) for iru in range (21)))
        dva = ''.join((random.choice(chars) for iru in range (6)))
        tri = ''.join((random.choice(chars) for iru in range (24)))
        print("Токен: " + ch2 + odin + "." + dva + "." + tri)
        result = ch2 + odin + "." + dva + "." + tri
        output = open("tokens.txt", "a")
        output.write(result + "\n")
    print("посмотри tokens.txt")

if laung=="EN" or laung=="en":
    for ien in range(rang):
        ch2 = ''.join((random.choice(chars2) for ien in range (3)))
        odin = ''.join((random.choice(chars) for ien in range (21)))
        dva = ''.join((random.choice(chars) for ien in range (6)))
        tri = ''.join((random.choice(chars) for ien in range (24)))
        print("Token: " + ch2 + odin + "." + dva + "." + tri)
        result = ch2 + odin + "." + dva + "." + tri
        output = open("tokens.txt", "a")
        output.write(result + "\n")

    print("check tokens.txt")

print("exit... 3 sec")
time.sleep(3)
