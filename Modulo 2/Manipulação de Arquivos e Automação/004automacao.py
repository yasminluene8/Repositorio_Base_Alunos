import pyautogui
import webbrowser
import time

# Passo 1: Abrir o Youtube com uma música específica
url= "https://www.youtube.com/watch?v=3tweQ0CRZ8o"
webbrowser.open(url)

# Passo 2: Aguardar o carregamento da página
time.sleep(5) # ajustar de acordo com a velocidade da internet 

# Passo 3: Garantir que o vídeo comece ( apertar o espaço para o play)
pyautogui.press("space") # toca ou pausa o vídeo