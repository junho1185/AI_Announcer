import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import airport_data_finder
import play
import script_maker
import simbrief_data_sync
import voice_maker


def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    # change this to match the location of cacert.pem
    return os.path.abspath("cacert.pem")


# is the program compiled?
if hasattr(sys, "frozen"):
    import certifi.core

    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where

    # delay importing until after where() has been replaced
    import requests.utils
    import requests.adapters
    # replace these variables in case these modules were
    # imported before we replaced certifi.core.where
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Announcer')
        self.setWindowIcon(QIcon('mic.png'))
        self.resize(700, 800)
        self.init_layout()
        self.center()
        self.show()

    def init_layout(self):
        self.simbrief_sync_button = QPushButton('Simbrief 연동')
        self.confirm_button = QPushButton('기내방송 만들기')
        self.simbrief_id = QLineEdit()
        self.status_label = QLabel('기내방송을 만들면\n버튼들이 활성화 됩니다.')
        self.flight_time_label = QLabel('비행시간')

        self.flight_hour = QComboBox(self)
        self.flight_minute = QComboBox(self)
        for i in range(120):
            self.flight_hour.addItem(str(i), userData=i)
        for i in range(60):
            self.flight_minute.addItem(str(i), userData=i)

        self.buttons = []
        self.buttons.append(QPushButton('Welcome and Boarding'))
        self.buttons.append(QPushButton('Jetway Disconnection'))
        self.buttons.append(QPushButton('Before Takeoff'))
        self.buttons.append(QPushButton('Seatbelt off and Safety Information'))
        self.buttons.append(QPushButton('Approach'))
        self.buttons.append(QPushButton('Before Landing'))
        self.buttons.append(QPushButton('After Landing'))


        self.confirm_button.setIcon(QIcon('mic.png'))

        self.departure_airport_icao = QLineEdit()
        self.arrival_airport_icao = QLineEdit()
        self.captain_name = QLineEdit()

        self.airline = QComboBox(self)
        self.airline.addItem('대한항공', userData=1)
        self.airline.addItem('아시아나항공', userData=2)
        self.airline.addItem('진에어', userData=3)
        self.airline.addItem('에어부산', userData=4)
        self.airline.addItem('에어서울', userData=5)
        self.airline.addItem('티웨이항공', userData=6)
        self.airline.addItem('AeroK', userData=7)
        self.airline.addItem('에어프레미아', userData=8)
        self.airline.addItem('플라이강원', userData=9)

        top_line_layout = QHBoxLayout()
        top_line_layout.addWidget(QLabel('Simbrief ID:'))
        top_line_layout.addWidget(self.simbrief_id)

        self.flight_time_label.setAlignment(Qt.AlignCenter)
        
        flight_time_box = QHBoxLayout()
        flight_time_box.addWidget(self.flight_hour)
        flight_time_box.addWidget(QLabel('시간'))
        flight_time_box.addWidget(self.flight_minute)
        flight_time_box.addWidget(QLabel('분'))
        flight_information_grid = QGridLayout()
        flight_information_grid.addWidget(self.airline, 0 , 0)
        flight_information_grid.addWidget(self.flight_time_label)
        flight_information_grid.addLayout(flight_time_box,2,0)
        flight_information_grid.addWidget(QLabel('출발 공항:'), 0, 1)
        flight_information_grid.addWidget(QLabel('도착 공항:'), 1, 1)
        flight_information_grid.addWidget(QLabel('  기장 :'), 2, 1)
        flight_information_grid.addWidget(self.departure_airport_icao, 0, 2)
        flight_information_grid.addWidget(self.arrival_airport_icao, 1, 2)
        flight_information_grid.addWidget(self.captain_name, 2, 2)
        flight_information_grid.addWidget(self.simbrief_sync_button, 0, 3)
        flight_information_grid.addWidget(self.confirm_button, 1, 3)
        flight_information_grid.addWidget(self.status_label, 2, 3)

        vbox = QVBoxLayout()
        vbox.addLayout(top_line_layout)
        vbox.addLayout(flight_information_grid)

        for i in range(7):
            self.buttons[i].setEnabled(False)
            vbox.addWidget(self.buttons[i])

        self.buttons[0].clicked.connect(lambda: play.play(0))
        self.buttons[1].clicked.connect(lambda: play.play(1))
        self.buttons[2].clicked.connect(lambda: play.play(2))
        self.buttons[3].clicked.connect(lambda: play.play(3))
        self.buttons[4].clicked.connect(lambda: play.play(4))
        self.buttons[5].clicked.connect(lambda: play.play(5))
        self.buttons[6].clicked.connect(lambda: play.play(6))

        self.setLayout(vbox)

        self.simbrief_sync_button.clicked.connect(self.simbrief_button_clicked)
        self.confirm_button.clicked.connect(self.confirm_button_clicked)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getUsername(self):
        file = open('username.txt', 'r')

    def simbrief_button_clicked(self):
        simbrief_data = simbrief_data_sync.get_simbrief_data(self.simbrief_id.text())
        if len(simbrief_data) == 0:
            self.status_label.setText('Simbrief ID를\n다시 확인해주세요.')
        else:
            self.status_label.setText('Simbrief 연동 완료!\n 정보를 확인해주세요.')
            flight_sec = int(simbrief_data[2])
            flight_hour = int(flight_sec/3600)
            flight_sec = flight_sec - (flight_hour * 3600)
            flight_minute = int(flight_sec/60)

            self.flight_hour.setCurrentIndex(flight_hour)
            self.flight_minute.setCurrentIndex(flight_minute)
            self.departure_airport_icao.setText(simbrief_data[0])
            self.arrival_airport_icao.setText(simbrief_data[1])
            self.captain_name.setText(simbrief_data[4])

    def confirm_button_clicked(self):
        play.stop()
        simbrief_data = simbrief_data_sync.get_simbrief_data(self.simbrief_id.text())
        if len(simbrief_data) == 0:
            self.status_label.setText('Simbrief ID를\n다시 확인해주세요.')
        else:
            self.status_label.setText('방송을 제작중입니다.\n잠시만 기다려주세요.')
            self.status_label.repaint()

            origin_airport_data = airport_data_finder.get_airport_data(self.departure_airport_icao.text())
            destination_airport_data = airport_data_finder.get_airport_data(self.arrival_airport_icao.text())

            if len(origin_airport_data) != 0 and len(destination_airport_data) != 0:
                kor_script = script_maker.kor_make_script(self.airline.currentData(), self.flight_hour.currentData(), self.flight_minute.currentData(), simbrief_data, origin_airport_data, destination_airport_data, self.captain_name.text())
                eng_script = script_maker.eng_make_script(self.airline.currentData(), self.flight_hour.currentData(), self.flight_minute.currentData(), simbrief_data, origin_airport_data, destination_airport_data, self.captain_name.text())
                voice_maker.voice_maker(kor_script, eng_script)
                for i in range(7):
                    self.buttons[i].setEnabled(True)
                self.status_label.setText('제작이 완료되었습니다.\n버튼을 눌러 재생하세요.')
            else:
                self.status_label.setText('Invalid ICAO code')
                self.status_label.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())