import os

from dotenv import load_dotenv
from google import genai
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QListWidgetItem
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
        item = QListWidgetItem(reply)
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.scrollToBottom() 
        self.ui.lineEdit.setPlaceholderText("Thinking")
        QtWidgets.QApplication.processEvents()
        
        try:
            result = callapi(reply)
            item = QListWidgetItem(result)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.scrollToBottom()
            self.ui.lineEdit.setPlaceholderText("Type Here")
        except Exception as e:
            result = f"Error {e}" 
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("There is something wrong")
            msg.setDetailedText(result)
            msg.setIcon(QMessageBox.Icon.Warning)
            self.ui.lineEdit.setPlaceholderText("Type Here")
            x = msg.exec()

        




               
# ----------------------
# RUN
# ----------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())