import time
import pyautogui
import keyboard
import json
import clipboard


def key_press(key):
    global stop
    if key.name == 'f10':
        stop = 1


keyboard.on_press(key_press)
try:
    with open('viber-spammer.json', "r", encoding='utf8') as file:
        spammer = json.load(file)
except:
    spammer = {"pause": 0, "message": "SPAM", "count": 0}
    with open('spammer.json', "w", encoding='utf8') as file:
        json.dump(spammer, file)
print("Кароч зайдите в файл с конфигурацией (spammer.json), и настройте кол-во сообщений (1-5000). \nИ еще кое-что: эта хрень спамит в открытый заранее чат, so сначaлa oткройте то, куда хотите спамит, потом стартуйте прогу.\nИ еще кое-что: перед использованием поставьте язык на английский\nИ еще кое-что: если нужно срочно закрыть программу - ЗАжмите f10")


pyautogui.PAUSE = spammer["pause"]
pyautogui.hotkey('alt', 'tab')
time.sleep(0.2)


stop = 0


def spam(spammer):
    global stop
    for _ in range(spammer["count"]):
        clipboard.copy(spammer["message"])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        if stop:
            return
    while True:
        _ = input().lower()
        if stop:
            return


spam(spammer)
