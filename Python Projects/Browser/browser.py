# ### 
    # 0000 - loading
        # 1000 - user interaction
            # 2000 - exec
            # 3000 - query
        # 4000 - error
    # 5000 - exit    
# # ###
import os
os.system('cls')
user = os.environ.get('USERNAME')
import time
print("Would you like to update? Y/N")
ino = input(": ")
if ino == "y" and "Y":
    try:
        os.system('pip install PyQt5 PyQtWebEngine')
    except:
        time.sleep(0)
import sys
from PyQt5.QtWidgets import *
import tkinter as tk
from tkinter import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class faf(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Llama Online")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("font-weight: bold; font-family: Arial, sans-serif;")

        self.create_webview()
        self.create_toolbar()   
        print("> 0100")     

    def create_webview(self):
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl("https://www.duckduckgo.com/chat"))
        self.setCentralWidget(self.webview)
        print("> 0200")

    def search(self):
        query = self.search_edit.text()
        url = f"https://www.duckduckgo.com/html/?q={query}"
        self.webview.setUrl(QUrl(url))
        if query == "youtube" and "Youtube" and "yotube" and "yt" and "yutube" and "tootube" and "youttube" and "yourube" and "yuotube" and "yuotbue" and "ytbe" and "youtube":
            self.webview.setUrl(QUrl("https://www.youtube.com/"))
            print("> 1100")
        elif query == "gpt":

            print("> 1400")
        elif query == "":
            self.webview.setUrl(QUrl(""))
            print("> 1200")
        else:
            print("> 1000")

    def create_toolbar(self):
        toolbar = QToolBar()

        home_action = QAction("Home", self)  
        home_action.triggered.connect(self.go_to_home)
        toolbar.addAction(home_action) 
        
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.webview.back)
        toolbar.addAction(back_action)

        self.search_edit = QLineEdit()
        self.search_edit.returnPressed.connect(self.search) 
        toolbar.addWidget(self.search_edit)

        # Add a spacer item to the toolbar
        #spacer = QWidget()
        #spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #toolbar.addWidget(spacer)

        # Create a QToolButton for the options

        options_button = QToolButton()
        options_button.setText("Options")
        options_button.setPopupMode(QToolButton.InstantPopup)

        # Create a QMenu for the options
        # Template
        #   option#_action = QAction("#", self)
        #   option#_action.triggered.connect(lambda: self.apply_preset("Option #"))
        #   options_menu.addAction(option#_action)

        options_menu = QMenu()

        option1_action = QAction("Black", self)
        option1_action.triggered.connect(lambda: self.apply_preset("Option 1"))
        options_menu.addAction(option1_action)

        option11_action = QAction("White", self)
        option11_action.triggered.connect(lambda: self.apply_preset("Option 11"))
        options_menu.addAction(option11_action)


        option4_action = QAction("Panel", self)
        option4_action.triggered.connect(lambda: self.apply_preset("Option 4"))
        options_menu.addAction(option4_action)

        option5_action = QAction("Restart", self)
        option5_action.triggered.connect(lambda: self.apply_preset("Option 5"))
        options_menu.addAction(option5_action)


        option3_action = QAction("About", self)
        option3_action.triggered.connect(lambda: self.apply_preset("Option 3"))
        options_menu.addAction(option4_action)




        # End of options menu

        options_button.setMenu(options_menu)
        toolbar.addWidget(options_button)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.confirm_quit)
        toolbar.addAction(quit_action)

        self.addToolBar(toolbar)
        print("> 0300")

    def go_to_home(self):
        self.webview.setUrl(QUrl("https://www.duckduckgo.com/chat")) 

    def confirm_quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you really want to quit?")
        msg.setWindowTitle("Confirmation Dialog")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            exit()

    def apply_preset(self, preset_name):
        print(f"Applying preset: {preset_name}")
        if preset_name == "Option 1":
            self.setStyleSheet("background-color: black; color: white;")
        elif preset_name == "Option 11":
            self.setStyleSheet("background-color: white; color: black;")
        elif preset_name == "Option 2":
            msg = QMessageBox()
            msg.setWindowTitle("Custom Message")
            msg.setText("This is a custom message for Option 2.")
            msg.exec_()
        elif preset_name == "Option 5":
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif preset_name == "Option 3":
            url = "https://zamwam.github.io/home"
            self.webview.setUrl(QUrl(url))


        elif preset_name == "Option 4":
            class Panel:
                def __init__(self, master):
                    self.master = master
                    master.title("Panel")

                    # Left Frame
                    self.left_frame = tk.Frame(master, width=200, height=400, bg="gray")
                    self.left_frame.grid(row=0, column=0, padx=10, pady=10)

                    # Add some widgets to the left frame
                    tk.Label(self.left_frame, text="Left Frame", bg="white").pack(pady=10)
                    tk.Button(self.left_frame, text="Button 1").pack()
                    tk.Button(self.left_frame, text="Button 2").pack()
                    tk.Button(self.left_frame, text="Button 3").pack()

                    # Right Frame
                    self.right_frame = tk.Frame(master, width=400, height=400, bg="gray")
                    self.right_frame.grid(row=0, column=1, padx=10, pady=10)

                    # Add some widgets to the right frame
                    tk.Label(self.right_frame, text="Right Frame", bg="black").pack(pady=10)
                    tk.Text(self.right_frame, width=40, height=10).pack()

            root = tk.Tk()
            my_panel = Panel(root)
            root.mainloop()



        else:
            print("Unknown preset option selected.")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = faf()
    viewer.show()
    sys.exit(app.exec_())
print("> 5000")
time.sleep(0.2)
