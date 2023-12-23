import multiprocessing

import get_Click_In_Keyboard as get_Click

if __name__ == '__main__':
    proceso = multiprocessing.Process(target=get_Click.get_click())
    proceso.start()