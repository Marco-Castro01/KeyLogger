import os
from install_Service import run_as_admin

if __name__ == '__main__':
    current_directory = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_directory, 'dist/CreateService.exe')

    command_to_run = 'sc create TEST_SERVICE binPath= "{}" start= auto'.format(script_path)

    # Llama a la función run_as_admin pasando el comando como argumento
    run_as_admin(command_to_run)
    run_as_admin("net start TEST_SERVICE")
