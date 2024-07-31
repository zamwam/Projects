import os
os.system('cls')
import time
print("Would you like to update? Y/N")
ino = input("")
if ino == "y" and "Y":
    try:
        os.system('pip install ffmpeg-python PyQt5 PyQtWebEngine Selenium yt-dlp pygame')
    except:
        time.sleep(0)
import sys
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QMenu, QFileDialog, QSlider
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import yt_dlp
from moviepy.editor import *


class YouTubeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ENHYouTube")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("font-weight: bold; font-family: Ariel-sans;")

        self.create_webview()
        self.create_menu()
    
    def create_webview(self):
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/"))
        self.setCentralWidget(self.webview)

    def create_menu(self):
        menu_bar = self.menuBar()

        home_action = QAction("Home", self)
        home_action.triggered.connect(self.go_to_home)

        back_action = QAction("Back", self)
        back_action.triggered.connect(self.webview.back)

        download_action = QAction("Download", self)
        download_action.triggered.connect(self.confirm_download)

        #mp3_action = QAction("Convert", self)
        #mp3_action.triggered.connect(self.convert_action)


        settings_menu = QMenu("Settings", self)
        preset_options = settings_menu.addMenu("Graphical Options")
        option1_action = QAction("BG Color - Sky Blue", self)
        option1_action.triggered.connect(lambda: self.apply_preset("Option 1"))
        preset_options.addAction(option1_action)
        
        preset_options = settings_menu.addMenu("Sound Options")
        option2_action = QAction("Custom Message", self)
        option2_action.triggered.connect(lambda: self.apply_preset("Option 2"))
        preset_options.addAction(option2_action)
        
        preset_options = settings_menu.addMenu(" Options")
        option3_action = QAction("???", self)
        option3_action.triggered.connect(lambda: self.apply_preset("Option 3"))
        preset_options.addAction(option3_action)
        
        preset_options = settings_menu.addMenu("Fullscreen")
        option4_action = QAction("On", self)
        option4_action.triggered.connect(lambda: self.apply_preset("Option 4"))
        preset_options.addAction(option4_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.confirm_quit)

        menu_bar.addAction(home_action)
        menu_bar.addAction(back_action)
        menu_bar.addAction(download_action)
        #menu_bar.addAction(mp3_action)
        menu_bar.addMenu(settings_menu)
        menu_bar.addAction(quit_action)

    def confirm_download(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you want to download the video?")
        msg.setWindowTitle("Download Confirmation")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            self.download()

    def download(self):
        video_url = self.webview.url().toString()
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
        download_dir = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        if download_dir:
            os.chdir(download_dir)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                    QMessageBox.information(self, "Download Complete", "Video downloaded successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Download Error", str(e))
        else:
            QMessageBox.information(self, "Download Cancelled", "Download cancelled by user.")

    def go_to_home(self):
        self.webview.setUrl(QUrl("https://www.youtube.com/"))

    def show_settings(self):
        msg = QMessageBox()
        msg.setWindowTitle("Settings")
        msg.setText("Customize your settings here.")
        msg.exec_()

    def apply_preset(self, preset_name):
        print(f"Applying preset: {preset_name}")
        if preset_name == "Option 1":
            self.setStyleSheet("background-color: lightblue;")
        elif preset_name == "Option 2":
            msg = QMessageBox()
            msg.setWindowTitle("Custom Message")
            msg.setText("This is a custom message for Option 2.")
            msg.exec_()
        elif preset_name == "Option 3":
            url = "https://zamwam.github.io/home"
            self.webview.setUrl(QUrl(url))
        elif preset_name == "Option 4":
            self.showMaximized()
            print("option 4")
        else:
            print("Unknown preset option selected.")

    def confirm_quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you really want to quit")
        msg.setWindowTitle("Download Confirmation")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            exit()

    #def mp3_action(self):
    #    current_directory = os.getcwd()
    #    os.chdir(current_directory)
#
    #def convert_action(self):
    #    print('1098209188108201281092091821902889028180812')
    #    mp4_file_location = input("Enter the full path of the input MP4 file: ")
    #    if not os.path.exists(mp4_file_location):
    #        print("File not found. Please enter a valid file path.")
    #        return
    #    mp4_filename, mp4_extension = os.path.splitext(os.path.basename(mp4_file_location))
    #    mp3_file_location = os.path.join(os.path.dirname(mp4_file_location), mp4_filename + ".mp3")
    #    video = VideoFileClip(mp4_file_location)
    #    audio = video.audio
    #    audio.write_audiofile(mp3_file_location)
    #    print("MP4 file converted to MP3 successfully. MP3 file saved at:", mp3_file_location)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.webview.back()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = YouTubeViewer()
    Uname = input("Enter your name: ")
    viewer.show()
    if Uname == "RyanC":
        while True:
            dev_menu = print("Press Ctrl + C & type quit to exit") + input(": ")
            if dev_menu == '0001':
                os.system('cls')
                import configparser
                import logging
                import os
                config = configparser.ConfigParser()
                config.read('settings.ini')
                print(f"Sections: {config.sections()}")
                for section in config.sections():
                    print(f"Keys in {section}: {config.options(section)}")

                window_size = config['DEFAULT'].get('window_size')
                if window_size is not None:
                    window_size = int(window_size)
                else:
                    print("window_size key not found in settings.ini file")
                if window_size is not None:
                    print(f"window_size: {window_size}")
                else:
                    print("window_size key not found in settings.ini file")
                os.system(f'mode con: cols={window_size} lines={window_size}')

                log_levels = {
                    'DEBUG': logging.DEBUG,
                    'INFO': logging.INFO,
                    'WARNING': logging.WARNING,
                    'ERROR': logging.ERROR,
                    'CRITICAL': logging.CRITICAL
                }

                log_level = config['DEFAULT'].get('log_level')
                if log_level is not None and log_level in log_levels:
                    logging.basicConfig(level=log_levels[log_level])
                else:
                    print("log_level key not found in settings.ini file or invalid log level")

                if log_level is not None:
                    print(f"log_level: {log_level}")
                else:
                    print("log_level key not found in settings.ini file")

                debug_state_dict = {
                    'DEBUG': logging.DEBUG,
                    'INFO': logging.INFO,
                    'WARNING': logging.WARNING,
                    'ERROR': logging.ERROR,
                    'CRITICAL': logging.CRITICAL
                }

                debug_state = config['DEFAULT'].get('debug_state')
                if debug_state is not None and debug_state in debug_state_dict:
                    logging.basicConfig(level=debug_state_dict[debug_state])
                else:
                    print("debug_state key not found in settings.ini file or invalid debug state")

                if debug_state is not None:
                    print(f"debug_state: {debug_state}")
                else:
                    print("debug_state key not found in settings.ini file")

                logging.basicConfig(level=log_level)
                logging.info('This is an info message')
                logging.warning('This is a warning message')
                logging.error('This is an error message')
                print()
                print("""Useful Commands:
                      Help
                      debug_state = INFO, LOCAL, TRUE, FALSE
                      fullscreen = TRUE, FALSE
                      pcwd (print's cwd)""")
                print()


            elif dev_menu.lower() == 'quit':
                break
            else:
                time.sleep(0)
    else:
        sys.exit(app.exec_())

os.system('cls')
