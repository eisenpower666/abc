import sys

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(1920, 1080)
widget.setWindowTitle("This is PyQt Widget example")
widget.show()
exit(app.exec_())