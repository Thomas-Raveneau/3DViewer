from PyQt5.QtWidgets import QPushButton


class ButtonCustom(QPushButton):
    btn: QPushButton
    def __init__(self, parent=None, _name = 'button') -> None:
        QPushButton.__init__(self, parent)
        self.setText(_name)
        self.move(0,0)
        self.setStyleSheet(
            "QPushButton {" + 
                "border: 1px solid red;" +
                "width: 100px;" +
                "}"
            )

    def paint(self):
        self.show()

    def dialog(self):
        print(self.action)
        return self.action



