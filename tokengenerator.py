#как по мне говно код но мне похуй :troll: / иди нахуй вард
import random
import time
import colorama
phrases = {"ruenter": "Введите количество токенов: ", "enenter": "Enter the number of tokens: ", "rucheck": "посмотри tokens.txt", "encheck": "check tokens.txt", "rutoken": "Токен: ", "entoken": "Token: "}
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321__-"
chars2 = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
colorama.init()
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
if laung.lower() != "ru" and laung.lower() != "en":
    print(f"""{colorama.Fore.RED}
ERROR/ОШИБКА """)
    input()
    exit()

rang = int(input(phrases[f"{laung.lower()}enter"]))

for iru in range(rang):
    ch2 = ''.join((random.choice(chars2) for iru in range (3)))
    odin = ''.join((random.choice(chars) for iru in range (21)))
    dva = ''.join((random.choice(chars) for iru in range (6)))
    tri = ''.join((random.choice(chars) for iru in range (24)))
    print(phrases[f"{laung.lower()}token"] + ch2 + odin + "." + dva + "." + tri)
    result = ch2 + odin + "." + dva + "." + tri
    output = open("tokens.txt", "a")
    output.write(result + "\n")
    print(phrases[f"{laung.lower()}check"])

input("exit...")