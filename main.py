import pyautogui
import random 

X_FISH = 138
Y_FISH = 42
RGB_FISH = (66, 164, 50)

X_BELLOSOM = 888
Y_BELLOSOM = 597
RGB_BELLOSOM = (130, 3, 0)

POKE_DEAD_POSITION = (878, 534) 
BP_LOOT_POSITION = (1747, 1002)

LIST_ATACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
LIST_OCEAN_POSITION = [(1254, 487), (1243, 631), (1104, 637), (1043, 726)]


USE_POKEBALL = True

def click_fish():
    pyautogui.click(X_FISH, Y_FISH)

def poke_atack():
    pyautogui.press(LIST_ATACK)

def get_loot():
    pyautogui.click(POKE_DEAD_POSITION, button='right')
    pyautogui.sleep(0.8)
    pyautogui.click(BP_LOOT_POSITION, clicks=5)

def use_pokeball():
    if USE_POKEBALL:
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click(POKE_DEAD_POSITION)


def check_poke_position():
    poke = pyautogui.pixelMatchesColor(X_BELLOSOM, Y_BELLOSOM, RGB_BELLOSOM)
    if not poke:
        pyautogui.press('f11')
        pyautogui.sleep(0.8)
        pyautogui.click(X_BELLOSOM, Y_BELLOSOM)

def use_fishing_rod():
    ocean_position = random.choice(LIST_OCEAN_POSITION)
    pyautogui.press('delete')
    pyautogui.click(ocean_position)


MAX_ATTEMPT = 800
attempt = 0

while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    attempt = attempt + 1
    print(attempt)
    if fish:
        click_fish()
        pyautogui.sleep(1.5)
        poke_atack()
        pyautogui.sleep(2)
        get_loot()
        use_pokeball()
        check_poke_position()
        pyautogui.sleep(4)
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0
        