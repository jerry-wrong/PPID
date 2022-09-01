import sys
import time


import pyautogui
import pyperclip
import qrcode
from PIL import Image, ImageQt
from pynput.keyboard import Controller,Key

from PyQt6.QtCore import pyqtSignal, QSettings, QThread
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

import label_ui
import scan_monitor



class InitForm(QWidget):
    # 点击Find Position之后改变界面
    signal_position = pyqtSignal()

    # 处理数据
    signal_Pushbutton_start_state = pyqtSignal()

    # 处理界面
    signal_Pushbutton_start_flage = pyqtSignal(int)

    def __init__(self):
        super(InitForm, self).__init__()
        self.keycode = None
        self.ui =label_ui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Dell UN3481 QR Label Generator")
        self.ui_init()
        self.monitor()

        self.state = 0
        self.flag = 0
        # 定义whole_label，没有点击开始直接回车，后边的whole_label.lower()就不会报错
        self.whole_label = ""


    def ui_init(self):
        # 初始化配置参数
        # self.init_login_info()
        #
        # # 点击按键的信号绑定
        # # 点击确定位置案件
        # self.ui.pushButtonFindPos.clicked.connect(self.slot_check_position)
        # # 点击确定位置按键之后更新界面
        # self.signal_position.connect(self.update_position)
        # # 点击确认位置按键，会自动找位置和存储配置
        # self.ui.pushButtonCheckPos.clicked.connect(self.slot_find_position)

        # 点击开始，合成数据，并生成二维码
        self.ui.pushButtonStart.clicked.connect(self.merge_label)
        self.signal_Pushbutton_start_state.connect(self.slot_change_state)
        self.signal_Pushbutton_start_flage.connect(self.slot_Pushbutton_start_flage)
        # self.ui.pushButtonStart.clicked.connect(self.slot_Pushbutton_s_flage)

        # 上一个码和下一个码
        self.ui.pushButtonNext.clicked.connect(self.next_image)
        self.ui.pushButtonLast.clicked.connect(self.last_image)

        # 扫码之后，回车
        # self.ui.lineEditCaptureLabel.returnPressed.connect(self.handleTextEntered)
        self.ui.lineEditCaptureLabel.textChanged.connect(self.handleTextEntered)

    def monitor(self):
        self.keyboard = Controller()

        self.monitor_scan = QThread()
        self.monitor_scan_function = scan_monitor.ScanMonitor()
        self.monitor_scan_function.moveToThread(self.monitor_scan)
        self.monitor_scan.start()
        # start monitor
        self.monitor_scan_function.signal_scan_init.connect(self.monitor_scan_function.scan_monitor_init)
        self.monitor_scan_function.signal_scan_init.emit()
        self.monitor_scan_function.signal_ready.connect(self.scan_ready_show)

    def slot_check_position(self):
        # print(1111)
        self.b = pyautogui.locateOnScreen('AX.png')
        if self.b == None:
            QMessageBox.warning(self, "warning", "请不要挡住AX目标界面/AX显示比例为100%")
            return
        print(self.b)
        self.signal_position.emit()

    # def update_position(self):
    #     self.ui.lineEditXPosition.setText(str(self.b.left + self.b.width*4/5))
    #     self.ui.lineEditYPosition.setText(str(self.b.top + self.b.height/2))
    #
    # def slot_find_position(self):
    #     pyautogui.moveTo(int(float(self.ui.lineEditXPosition.text())),int(float(self.ui.lineEditYPosition.text())))
    #     self.save_login_info()

    # 保存上次的设置
    # def save_login_info(self):
    #     settings = QSettings("config.ini",QSettings.Format.IniFormat)
    #     settings.setValue("x_position",self.ui.lineEditXPosition.text())
    #     settings.setValue("y_position",self.ui.lineEditYPosition.text())

    # 载入上次的值
    # def init_login_info(self):
    #     settings = QSettings("config.ini", QSettings.Format.IniFormat)
    #     x_position = settings.value("x_position")
    #     y_position = settings.value("y_position")
    #     self.ui.lineEditXPosition.setText(x_position)
    #     self.ui.lineEditYPosition.setText(y_position)

    def merge_label(self):
        self.set_widget_enable(True)
        self.signal_Pushbutton_start_state.emit()
        # 准备数据
        # 步长
        self.step = int(self.ui.lineEditStep.text())
        if self.step > 5:
            QMessageBox.warning(self, "warning", "请输入0-5之间的数字")
            return
        # 数据
        self.whole_label = self.ui.lineEditFirstLine.text() + self.ui.lineEditSecondLine.text()
        if len(self.whole_label) != 28:
            QMessageBox.warning(self, "warning", "请检查输入信息")
            return
        self.ui.lineEditCurrentLabel.setText(self.whole_label)
        # 每次更改合成，都需要重新生成生成器以使得数字重新开始
        self.gen = None
        if self.gen is None:
            self.gen = self.num_generator()
        # 调试的时候不能生成图片，因为占用内存太大
        self.make_qrcode(self.whole_label)

    # 设置按键有效性
    # 一开始是无效的，防止乱点
    # 点了start之后就可以使用了
    def set_widget_enable(self,enable):
        self.ui.pushButtonNext.setEnabled(enable)
        self.ui.pushButtonLast.setEnabled(enable)
        self.ui.lineEditCaptureLabel.setEnabled(enable)

    def slot_change_state(self):
        if self.state == 0:
            self.signal_Pushbutton_start_flage.emit(self.state)
            self.state = 1
        else:
            self.signal_Pushbutton_start_flage.emit(self.state)
            self.state = 0


    def slot_Pushbutton_start_flage(self,state):
        # print("11111")
        if state == 0:
            # self.ui.lineEditXPosition.setEnabled(False)
            # self.ui.lineEditYPosition.setEnabled(False)
            # self.ui.pushButtonFindPos.setEnabled(False)
            # self.ui.pushButtonCheckPos.setEnabled(False)
            self.ui.lineEditFirstLine.setEnabled(False)
            self.ui.lineEditSecondLine.setEnabled(False)
            self.ui.lineEditStep.setEnabled(False)
            self.ui.pushButtonStart.setText("Close")
            self.ui.pushButtonStart.setStyleSheet("color:red")
            self.ui.pushButtonNext.setEnabled(True)
            self.ui.pushButtonLast.setEnabled(True)
            self.ui.lineEditCaptureLabel.setEnabled(True)

        else:
            # self.ui.lineEditXPosition.setEnabled(True)
            # self.ui.lineEditYPosition.setEnabled(True)
            # self.ui.pushButtonFindPos.setEnabled(True)
            # self.ui.pushButtonCheckPos.setEnabled(True)
            self.ui.lineEditFirstLine.setEnabled(True)
            self.ui.lineEditSecondLine.setEnabled(True)
            self.ui.lineEditStep.setEnabled(True)
            self.ui.pushButtonStart.setText("Start")
            self.ui.pushButtonStart.setStyleSheet("color:black")
            self.ui.pushButtonNext.setEnabled(False)
            self.ui.pushButtonLast.setEnabled(False)
            self.ui.lineEditCaptureLabel.setEnabled(False)



    # 扫码枪输入自动换行
    def handleTextEntered(self):
        if self.flag == 1:
            self.flag = 0
        # 判断没有扫错码

        if self.ui.lineEditCaptureLabel.text().lower() == self.whole_label.lower():
            if self.gen is None:
                self.gen = self.num_generator()
                # 生成下一个数据
            self.new_label = next(self.gen)
            print(1)
            # print("self.newlabel",self.new_label)

            self.ui.lineEditCurrentLabel.setText(self.new_label)
            # pyautogui.click(int(float(self.ui.lineEditXPosition.text())),int(float(self.ui.lineEditYPosition.text())))
            # time.sleep(0.2)
            # pyautogui.doubleClick(int(float(self.ui.lineEditXPosition.text())),int(float(self.ui.lineEditYPosition.text())))
            # pyautogui.doubleClick(int(float(self.ui.lineEditXPosition.text())),int(float(self.ui.lineEditYPosition.text())))
            # pyautogui.write(str(self.new_label))
            # pyautogui.write([str(self.new_label),'enter'])
            # pyperclip.write(str(self.new_label))
            # pyperclip.write([])
            # 自动生成图像
            self.make_qrcode(self.new_label)
            # 再次输入之前要清空
            self.ui.lineEditCaptureLabel.clear()
        else:
            # QMessageBox.warning(self, "warning", "请输入正确的信息")
            pass

    def next_image(self):
        self.flag = 0
        if self.gen is None:
            self.gen = self.num_generator()
        # 生成下一个数据
        self.new_label = next(self.gen)
        print(self.new_label)
        self.ui.lineEditCurrentLabel.setText(self.new_label)
        # 自动生成二维码并显示
        self.make_qrcode(self.new_label)

    # 调用生成器
    def last_image(self):
        self.flag = 1
        if self.gen is None:
            self.gen = self.num_generator()
        # 生成下一个数据
        self.new_label = next(self.gen)
        print(self.new_label)
        self.ui.lineEditCurrentLabel.setText(self.new_label)
        # 自动生成二维码并显示
        self.make_qrcode(self.new_label)


    def make_qrcode(self,data):
        # 生成二维码
        img = qrcode.make(data)
        # print(type(img))
        # 转化为QLabel可以显示的格式
        qpixmap = ImageQt.toqpixmap(img)
        # print(type(qpixmap))
        self.ui.labelQr.setPixmap(qpixmap)
        # 生成二维
        # self.ui.labelQr.setPixmap(qpixmap)

    # 进制
    def num_generator(self):
        # 获取步长
        self.step = int(self.ui.lineEditStep.text())
        # 1.列出正序每一位的字母
        self.single_digits = [str(i) for i in range(10)]
        self.single_char = [chr(cha) for cha in range(65, 91)]
        self.single_digits.extend(self.single_char)
        # (1).列出倒叙每一位的字母
        self.single_digits_rev = [chr(cha) for cha in range(90, 64, -1)]
        self.single_char_rev = [str(i) for i in range(9, -1, -1)]
        self.single_digits_rev.extend(self.single_char_rev)

        # 调试第：23位
        # 3.实现第23位的增减
        while True:
            self.step = int(self.ui.lineEditStep.text())
            if self.step > 5:
                QMessageBox.warning(self, "warning", "请输入0-5之间的数字,先将步长设置为1")
                # print(self.step)
                self.ui.lineEditStep.setText("1")
                self.step = 1
            # next递增
            if self.flag == 0:
                # 2.获取本位字母的下标
                self.index_num_23 = self.single_digits.index(self.whole_label[23])
                self.index_num_22 = self.single_digits.index(self.whole_label[22])
                self.index_num_21 = self.single_digits.index(self.whole_label[21])
                self.index_num_20 = self.single_digits.index(self.whole_label[20])
                # 4. 点一下自增1
                self.index_num_23 += self.step
                # 5. 更新下标，共36个数字，z的下标是35
                if self.index_num_23 >= 36:
                    self.index_num_23 = self.index_num_23 - 36
                    # 获得第22位的对应搜索列表的下标，并加1
                    self.index_num_22 = self.single_digits.index(str(self.whole_label[22])) + 1

                    if self.index_num_22 >= 36:
                        self.index_num_22 = 0
                        # 获得第21位的对应搜索列表的下标，并加1
                        self.index_num_21 = self.single_digits.index(str(self.whole_label[21])) + 1

                        if self.index_num_21 >= 36:
                            self.index_num_21 = 0
                            # 获得第21位的对应搜索列表的下标，并加1
                            self.index_num_20 = self.single_digits.index(str(self.whole_label[20])) + 1

                # 4.1 更新whole_label的值
                self.whole_label = list(self.whole_label)
                self.whole_label[23] = self.single_digits[self.index_num_23]
                self.whole_label[22] = self.single_digits[self.index_num_22]
                self.whole_label[21] = self.single_digits[self.index_num_21]
                self.whole_label[20] = self.single_digits[self.index_num_20]
            # last递减
            if self.flag == 1:
                # 2.获取本位字母的下标
                self.index_num_23 = self.single_digits_rev.index(self.whole_label[23])
                self.index_num_22 = self.single_digits_rev.index(self.whole_label[22])
                self.index_num_21 = self.single_digits_rev.index(self.whole_label[21])
                self.index_num_20 = self.single_digits_rev.index(self.whole_label[20])
                # 4. 点一下自减1
                self.index_num_23 += self.step
                # 5. 更新下标，共36个数字，0的下标是35
                if self.index_num_23 >= 36:
                    self.index_num_23 = self.index_num_23 - 36
                    # 获得第22位的对应搜索列表的下标，并加1
                    self.index_num_22 = self.single_digits_rev.index(str(self.whole_label[22])) + 1

                    if self.index_num_22 >= 36:
                        self.index_num_22 = 0

                        # 获得第21位的对应搜索列表的下标，并加1
                        self.index_num_21 = self.single_digits_rev.index(str(self.whole_label[21])) + 1

                        if self.index_num_21 >= 36:
                            self.index_num_21 = 0

                            # 获得第21位的对应搜索列表的下标，并加1
                            self.index_num_20 = self.single_digits_rev.index(str(self.whole_label[20])) + 1

                # 4.1 修改
                self.whole_label = list(self.whole_label)
                self.whole_label[23] = self.single_digits_rev[self.index_num_23]
                self.whole_label[22] = self.single_digits_rev[self.index_num_22]
                self.whole_label[21] = self.single_digits_rev[self.index_num_21]
                self.whole_label[20] = self.single_digits_rev[self.index_num_20]

            # 4.2 变换完之后换为字符串
            self.whole_label = str(self.whole_label)
            # 4.3 处理字符串
            self.whole_label = self.whole_label.replace("['", "")
            self.whole_label = self.whole_label.replace("']", "")
            self.whole_label = self.whole_label.replace("', '", "", 40)
            self.whole_label = self.whole_label.replace("', ", "")
            self.whole_label = self.whole_label.replace(", '", "")
            # 4.4 输出结果
            yield self.whole_label
            # 4.5 为下次修改变为列表
            self.whole_label = list(self.whole_label)

    # 接受到扫描数据之后
    def scan_ready_show(self, code):
        self.ui.lineEditCaptureLabel.setText(code.upper())
        # self.ui.lineEditCaptureLabel.enterEvent()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon('adell.ico'))
    w1 = InitForm()
    w1.show()

    sys.exit(app.exec())
