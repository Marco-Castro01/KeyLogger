import os
import ctypes
import sys
from ComandsLogic.GetProgramFiles import *


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    program_files_path = GetProgramFiles()

    CiberSeguridad_Project_path = os.path.join(program_files_path, 'CiberSeguridad_Project')

    exe_path = os.path.join(CiberSeguridad_Project_path, 'CreateService.exe')

    exe_in_program_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        'dist',
        'CreateService.exe'
    )
    createService_command = 'sc create TEST_SERVICE binPath= "{}" start= auto'.format(
        os.path.join(
            CiberSeguridad_Project_path,
            exe_path
        )
    )
    print('exe path {}'.format(exe_path))
    COMMAND = (
        'mkdir "{}" & copy "{}" "{}"'
        .format(
            CiberSeguridad_Project_path,
            exe_in_program_path,
            exe_path
        )
    )

    if is_admin():
        os.system(COMMAND)
        os.system(createService_command)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    run_as_admin()
