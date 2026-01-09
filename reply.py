import os

from dotenv import load_dotenv
from google import genai
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMessageBox, QListWidgetItem, QWidget, QHBoxLayout, QLabel
)
from mainwindow import Ui_MainWindow
import sys

load_dotenv()

apikey = genai.Client(api_key=os.getenv("API_KEY"))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addtolist)
        self.ui.lineEdit.setFocus()
        self.setStyleSheet("""
            QMainWindow, QListWidget {
                background-color: #21282a; /* İstediğin modern renk */
                border: none;
            }
        """)

    def addtolist(self):
        reply = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        item = QListWidgetItem(self.ui.listWidget)
        msg_widget = MessageWidget(reply, True)
        item.setSizeHint(msg_widget.sizeHint())
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, msg_widget)
        self.ui.listWidget.scrollToBottom()
        self.ui.lineEdit.setPlaceholderText("Thinking")
        QtWidgets.QApplication.processEvents()
        self.callback_ai(reply)

    def callback_ai(self, text):
        try:
            result = self.callapi(text)
            item = QListWidgetItem(self.ui.listWidget)
            msg_widget = MessageWidget(result, False)
            item.setSizeHint(msg_widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, msg_widget)
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

    def callapi(self, user_input):
        response = apikey.models.generate_content(
            model="gemini-2.5-flash", contents=user_input
        )
        return response.text


class MessageWidget(QWidget):
    def __init__(self, text, is_mine=True):
        super().__init__()
        layout = QHBoxLayout(self)

        # Mesaj Baloncuğu
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setContentsMargins(10, 5, 10, 5)

        # Stil: is_mine (benimse) mavi ve sağa, (karşı tarafsa) gri ve sola
        if is_mine:
            bg_color = "#0984e3"  # Mavi
            text_color = "white"
            layout.addStretch()  # Sola boşluk ekle (sağa yasla)
            layout.addWidget(self.label)
        else:
            bg_color = "#dfe6e9"  # Gri
            text_color = "black"
            layout.addWidget(self.label)
            layout.addStretch()  # Sağa boşluk ekle (sola yasla)

        self.label.setStyleSheet(f"""
            background-color: {bg_color};
            color: {text_color};
            border-radius: 10px;
            padding: 8px;
        """)


def add_message(self, text, is_mine):
    # 1. Boş bir item oluştur (boyut tutucu olarak)
    item = QListWidgetItem(self.listWidget)

    # 2. Kendi widget'ımızı oluştur
    msg_widget = MessageWidget(text, is_mine)

    # 3. Item'ın boyutunu widget'a göre ayarla
    item.setSizeHint(msg_widget.sizeHint())

    # 4. Widget'ı listeye yerleştir
    self.listWidget.addItem(item)
    self.listWidget.setItemWidget(item, msg_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
