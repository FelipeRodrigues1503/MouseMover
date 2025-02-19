import pyautogui
import time

import pyautogui
import time

def mover_mouse():
    while True:
        x, y = pyautogui.position()  # Captura a posição atual do mouse
        pyautogui.moveTo(x + 1, y + 1, duration=0.2)  # Move um pixel para diagonal
        pyautogui.moveTo(x, y, duration=0.2)  # Retorna para a posição original
        time.sleep(10)  # Espera 10 segundos antes de repetir

if __name__ == "__main__":
    print("Movendo o mouse... Pressione Ctrl+C para parar.")
    mover_mouse()

