import pyautogui as py
import pyperclip as 

# py.click -> clicar
# py.write -> escrever
# py.press -> pressionar
# py.hotkey -> atalho
py.PAUSE = 1
# Passo 1 - Entra no sistema da empresa (no link driver)
py.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
py.hotkey("ctrl", "v")
py.hotkey("enter")

time.sleep(5)

# Passo 2 - Navegar ate o local do relatorio (entrar na pasta exportar)
py.click(x=398, y=277, clicks=2)

time.sleep(2)

# Passo 3 - Exporta o relatorio (fazer dawnload)

py.click(x=423, y=384)     #button= left / center / right
py.click(x=1709, y=155)
py.click(x=1491, y=568),

time.sleep(5)

# PassEnviar um e-mail para a diretoriao 4 -

# Abrir entrar no e-mail
py.hotkey("ctrl", "t") #abre aba google
pyperclip.copy(r"https://mail.google.com/mail/u/0/#inbox")
py.hotkey("ctrl", "v")
py.press("enter")

time.sleep(5)
#clicar no botao escrever
py.click(x=101, y=170)

# preencher informaçoes do e-mail
# destinario
py.write("juninhogonzaga006@gmail.com")
py.press("tab") # selecionar e-mail
py.press("tab") # pular pro campo de assunto

# assunto
py.write("Relatorio de vendas")

# corpo
texto = """BOMM DIAAA CLIENTES
O VALOR FATURADO HOJE FOI DE 15,000,00
AS VENDAS FOI DE 158
FE QUE A NOITES EM CLARO ESTUDANDO NAO VAI SER EM VÃO
DEUS NO COMANDO"""

py.write(texto)
py.hotkey("ctrl", "enter")


import time
time.sleep(5)
py.position()