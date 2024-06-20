from moviepy.editor import *
import os

def convert_mp4_to_mp3():
    mp4_file_location = input("Enter the full path of the input MP4 file: ")
    
    if not os.path.exists(mp4_file_location):
        print("File not found. Please enter a valid file path.")
        return
    
    mp4_filename, mp4_extension = os.path.splitext(os.path.basename(mp4_file_location))
    mp3_file_location = os.path.join(os.path.dirname(mp4_file_location), mp4_filename + ".mp3")
    
    video = VideoFileClip(mp4_file_location)
    audio = video.audio
    audio.write_audiofile(mp3_file_location)

    print("MP4 file converted to MP3 successfully. MP3 file saved at:", mp3_file_location)


#import sys
#
#from PyQt5.QtWidgets import (
#    QApplication,
#    QCheckBox,
#    QComboBox,
#    QDateEdit,
#    QDateTimeEdit,
#    QDial,
#    QDoubleSpinBox,
#    QFontComboBox,
#    QLabel,
#    QLCDNumber,
#    QLineEdit,
#    QMainWindow,
#    QProgressBar,
#    QPushButton,
#    QRadioButton,
#    QSlider,
#    QSpinBox,
#    QTimeEdit,
#    QVBoxLayout,
#    QWidget,
#)
#
## Subclass QMainWindow to customize your application's main window
#class MainWindow(QMainWindow):
#    def __init__(self):
#        super().__init__()
#
#        self.setWindowTitle("Widgets App")
#
#        layout = QVBoxLayout()
#        widgets = [
#            QCheckBox,
#            QComboBox,
#            QDateEdit,
#            QDateTimeEdit,
#            QDial,
#            QDoubleSpinBox,
#            QFontComboBox,
#            QLCDNumber,
#            QLabel,
#            QLineEdit,
#            QProgressBar,
#            QPushButton,
#            QRadioButton,
#            QSlider,
#            QSpinBox,
#            QTimeEdit,
#        ]
#
#        for w in widgets:
#            layout.addWidget(w())
#
#        widget = QWidget()
#        widget.setLayout(layout)
#
#        # Set the central widget of the Window. Widget will expand
#        # to take up all the space in the window by default.
#        self.setCentralWidget(widget)
#
#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#app.exec()