# 捕获扫描枪的包
from pynput import keyboard, keyboard

from PyQt6.QtCore import QObject, pyqtSignal


class ScanMonitor(QObject):
    signal_scan_init = pyqtSignal()
    signal_ready = pyqtSignal(object)

    def __init__(self):
        super(ScanMonitor, self).__init__()
        self.code = None
        self.state = 0

    def on_release(self, key):
        try:
            self.code += key.char
            # print(1)
        except Exception as e:
            try:
                if key == key.enter:
                    # if "http" in CODE:
                    #     message = CODE.replace("http;","http:")
                    #     print(message)
                    # print(self.code)
                    self.signal_ready.emit(self.code)
                    self.code = ""
            except Exception as e:
                # self.code = ""
                self.code = key.char

    def scan_monitor_init(self):
        # 监听键盘扫码枪输入
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()
