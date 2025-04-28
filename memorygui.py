import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QPushButton, QLabel, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt,QTimer
import psutil



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Stats")
        self.setGeometry(480, 200, 600, 600)
        self.setWindowIcon(QIcon("stats.png"))
        self.background_label = QLabel()

        pixmap = QPixmap('computer_back.jpg')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)


        # Merkezi widget oluşturuluyor
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        self.stats_button = QPushButton("View Computer Stats")
        self.stop_button = QPushButton("Stop Computer Stats")

        self.free_ram = QLabel("Free RAM:")
        self.available_ram = QLabel("Available RAM:")
        self.usage_ram = QLabel("RAM in usage:")
        self.total_ram = QLabel("Total RAM:")

        vbox.addWidget(self.background_label)
        vbox.addWidget(self.stats_button,alignment=Qt.AlignCenter)
        vbox.addWidget(self.stop_button,alignment=Qt.AlignCenter)
        vbox.addWidget(self.free_ram,alignment=Qt.AlignLeft)
        vbox.addWidget(self.available_ram,alignment=Qt.AlignLeft)
        vbox.addWidget(self.usage_ram,alignment=Qt.AlignLeft)
        vbox.addWidget(self.total_ram,alignment=Qt.AlignLeft)

        self.stats_button.setObjectName("stats")
        self.stop_button.setObjectName("stop")
        central_widget.setLayout(vbox)

        self.setStyleSheet("""QMainWindow{
            background-color:black;
        }
        QLabel {
            font-size: 20px;
            font-weight:bold;
            font-family: Arial;
            padding: 10px;
            color:hsl(0, 74%, 36%);
        }QPushButton{
            font-size:20px;
            font-weight:bold;
            font-family:Arial;
            padding:10px;
            background-color:white;
            color:black;
            border:2px solid green;
            transition-duration:0.4s;
        }QPushButton#stats:hover{
            background-color:green;
            color:white;
        }QPushButton#stop:hover{
            background-color:green;
            color:white;
        }
        """)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_stats)

        self.stats_button.clicked.connect(self.start_stats)
        self.stop_button.clicked.connect(self.stop_stats)


    def start_stats(self):
        self.timer.start(1000)  # 3 saniyede bir güncelle
        self.display_stats()  # İlk verileri hemen göster

    def stop_stats(self):
        self.timer.stop()
        self.free_ram.clear()
        self.available_ram.clear()
        self.usage_ram.clear()
        self.total_ram.clear()


    def display_stats(self):
        mem = psutil.virtual_memory()
        self.free_ram.setText(f"Free RAM: {mem.free / (1024 ** 2):.2f} MB")
        self.available_ram.setText(f"Available RAM: {mem.available / (1024 ** 2):.2f} MB")
        self.usage_ram.setText(f"Used RAM: {mem.used / (1024 ** 2):.2f} MB")
        self.total_ram.setText(f"Total RAM: {mem.total / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())