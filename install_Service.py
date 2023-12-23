import ctypes
import os
import sys
import subprocess

def run_as_admin(command, wait=True):
    # Solicitar derechos de administrador
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    # Ejecutar el comando
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
        sys.exit(1)

if __name__ == '__main__':
    current_directory = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_directory, 'dist\\CreateService.exe')

    command_to_run = 'sc create TEST_SERVICE binPath= "{}" start= auto'.format(script_path)

    # Llama a la función run_as_admin pasando el comando como argumento
    run_as_admin(command_to_run)
