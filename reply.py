import os

from dotenv import load_dotenv
from google import genai
from PyQt6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import sys

load_dotenv()

apikey = genai.Client(api_key=os.getenv("API_KEY"))

def callapi(user_input):
    response = apikey.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    return response.text

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.addtolist)

    def addtolist(self):
        reply = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        self.ui.listWidget.addItem("Sen: \n " + reply + "\n")
        self.ui.listWidget.scrollToBottom() 
        self.ui.lineEdit.setPlaceholderText("Thinking")
        QtWidgets.QApplication.processEvents()
        
        try:
            result = callapi(reply)
        except Exception as e:
            result = f"Error {e}" 
        self.ui.listWidget.addItem("Gemini: \n " + result + "\n")
        self.ui.listWidget.scrollToBottom()
        self.ui.lineEdit.setPlaceholderText("Type Here")



               
# ----------------------
# RUN
# ----------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())