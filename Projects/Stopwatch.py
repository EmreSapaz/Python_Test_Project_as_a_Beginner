from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLayout, QHBoxLayout,QPushButton,QVBoxLayout
from PyQt6.QtCore import QTimer,QTime,Qt
import sys


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        v_box = QVBoxLayout()

        v_box.addWidget(self.time_label)

        self.setLayout(v_box)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        h_box = QHBoxLayout()

        h_box.addWidget(self.start_button)
        h_box.addWidget(self.stop_button)
        h_box.addWidget(self.reset_button)

        v_box.addLayout(h_box)


        self.setStyleSheet("""
            QPushButton,QLabel{
                padding:20px;
                font-family: Brush Script MT
            }
            QPushButton{
                font-size: 20px;
            }
            QLabel{
                font-size: 100px;
                font-weight: bold;
                background-color : hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.Start)
        self.stop_button.clicked.connect(self.Stop)
        self.reset_button.clicked.connect(self.Reset)
        self.timer.timeout.connect(self.Update_display)

    def Start(self):
        self.timer.start(10)

    def Stop(self):
        self.timer.stop()

    def Reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.Format_time(self.time))

    def Format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return  f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def Update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.Format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec())