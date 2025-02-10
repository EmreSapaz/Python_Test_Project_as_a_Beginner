from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLayout, QVBoxLayout
import sys
from PyQt6.QtCore import QTimer,QTime,Qt
from PyQt6.QtGui import QFont,QFontDatabase


class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(500,300,500,150)

        v_box = QVBoxLayout()
        v_box.addWidget(self.time_label)
        self.setLayout(v_box)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label.setStyleSheet("font-size:150px;"
                                      "color : Aqua ;")

        font_id = QFontDatabase.addApplicationFont("Technology.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)

        self.setStyleSheet("background-color : black")

        self.timer.timeout.connect(self.update_time)

        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digital_Clock()
    clock.show()
    sys.exit(app.exec())