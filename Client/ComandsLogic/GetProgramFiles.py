import os

def GetProgramFiles():
    # Verificar si el sistema operativo es Windows
    if os.name == 'nt':
        # Usar la variable de entorno 'ProgramFiles' para obtener la ruta de "Archivos de programa"
        ruta_archivos_programa = os.environ.get('ProgramFiles')
        if ruta_archivos_programa:
            return ruta_archivos_programa
        else:
            print("No se pudo obtener la ruta de 'Archivos de programa'")
            return None
    else:
        print("Este script está diseñado para ejecutarse en un sistema Windows.")
        return None

