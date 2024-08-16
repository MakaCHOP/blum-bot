from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
from termcolor import colored
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

putih = '\033[1;97m'
red_text = '\033[1;91m'
green_text = '\033[1;92m'
yellow_text = '\033[1m\033[93m'
biru = '\033[1;94m'
reset = '\033[0m'
putihmerah = '\033[97m\033[41m'
putihhijau = '\033[97m\033[42m'
merahhijau = '\033[1;91m\033[42m'


def anjaymabar():
    print(f"""{green_text}
  {green_text}|      |                         {yellow_text}  |             |   
  {green_text}__ \   |  |   |  __ `__ \        {yellow_text}  __ \    _ \   __| 
  {green_text}|   |  |  |   |  |   |   | {red_text}_____|{yellow_text}  |   |  (   |  |   
 {green_text}_.__/  _| \__,_| _|  _|  _|       {yellow_text} _.__/  \___/  \__| {reset}
    """)

    print(f"""
          {yellow_text}_ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`{red_text}\\ ' . /{yellow_text}`~~`
{red_text}              ;   ;
{red_text}              /   \\
{green_text}_____________{red_text}/_ __ \{green_text}_____________
    """)

anjaymabar()
print(f" {putihmerah}Author: Ali Borsalani{reset}")
print(f" {putihhijau}Contact me on telegram: @Bor420{reset}")
print(f" {yellow_text}Donations (TON):{putih} UQBBhOnsXHMYskY5Z4Ifol4jc6hFjgMR30R1tZiFTG7erXMU{reset}")
print(f" {yellow_text}Donations (ETH):{putih} 0x00000000036027D03fA1a7A218b56815A7629074{reset}")
print()

window_input = f"\n{putih} [?] | Enter Window {green_text}(1 - TelegramDesktop){putih}: {reset}"
window_not_found = f"{putih} [>] | Your Window - {{}} {yellow_text}not found!{reset}"
window_found = f"{green_text} [>] | Window found - {{}}\n{green_text} Now bot working... {putih}Press {yellow_text}'K'{putih} on the keyboard to pause.{reset}"
pause_message = f"{biru} Bot paused...\n{putih} Press {yellow_text}'K'{putih} again on the keyboard to continue{reset}"
continue_message = f"{biru} Bot continue working...{reset}"


def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)


window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
    print(
        f" {putihmerah}EN:{reset}\n   {putihmerah}Make sure you use the TelegramDesktop application (not Telegram "
        f"Web).{reset}\n   {putihmerah}And have opened the Blum bot on your TelegramDesktop.{reset}\n   "
        f"{putihmerah}Until the Blum window is available{reset}")
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False

    while True:
        if keyboard.is_pressed('K'):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)

        if paused:
            continue

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        )

        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size
        pixel_found = False
        if pixel_found:
            break

        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = scrn.getpixel((x, y))
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break

