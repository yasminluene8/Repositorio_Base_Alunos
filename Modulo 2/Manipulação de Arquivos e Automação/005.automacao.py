# Crie um programa que use um comando com o Pyautogui 
# para abrir a calculadora do Windows
# Faça um calculo de 8 + 2 e apresente o resultado

import pyautogui

pyautogui.press("win") # abrimos o windows
pyautogui.sleep(1) # aguardamos 1 segundo
pyautogui.write("calculadora") # comando para abrir a calculadora
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.write("2 + 8") # digito a operação
pyautogui.press("enter") # pressiona enter 