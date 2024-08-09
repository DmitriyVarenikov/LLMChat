import sys
import os
from datetime import datetime

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QTextCursor, QTextBlockFormat, Qt
from openai import OpenAI

import balance
from untitled import Ui_Form


class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.pushButton.clicked.connect(self._push_msg)
        self._file_name = datetime.now().strftime("%y%m%d_%H%M%S") + '.txt'
        self._set_balance()

    def _set_balance(self):
        try:
            many = balance.get_balance()
            self._ui.lbl_balance.clear()
            self._ui.lbl_balance.setText(str(many))
        except Exception as er:
            print(er)

    def _push_msg(self):
        prompt = self._ui.plainTextEdit.toPlainText()
        msg = f"User: {prompt}\n"
        self._write_chat(msg)

        if prompt:
            self._ui.textEdit.append(msg)
            self._ui.plainTextEdit.clear()
            answer = self._server(prompt)
            msg = f"GPT: {answer}\n"
            self._ui.textEdit.append(msg)
            self._write_chat(msg)

        self._set_balance()

    def _server(self, prompt):
        client = OpenAI(
            api_key="sk-or-vv-25dc501d046524024b08d4d7b288e0803b2695bf795a751ef233770dd542b69c",
            base_url="https://api.vsegpt.ru/v1",
        )
        messages = []
        messages.append({"role": "user", "content": prompt})

        response_big = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            n=1,
            max_tokens=3000,
            extra_headers={"X-Title": "My App"},
        )

        response = response_big.choices[0].message.content
        return response

    def _chat(self, msg):
        self._ui.textEdit.append(msg)

    def _write_chat(self, msg):
        with open(self._file_name, 'a') as file:
            # Записываем данные в конец файла
            file.write(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Chat()
    window.show()
    sys.exit(app.exec())
