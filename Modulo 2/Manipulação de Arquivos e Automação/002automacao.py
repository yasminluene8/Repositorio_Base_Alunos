# Importar a biblioteca pyautogui
import pyautogui

# criamos um loop de 10 repetições para mover o mousse na forma de quadrado que se move 
for i in range(10): 
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25)