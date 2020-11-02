import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QAction, qApp, QFileDialog, \
    QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()

        self.central_widget = QWidget()
        self.vbox = QVBoxLayout()
        self.lbl_img = QLabel()
        self.file_name = 'assets/lenna.png'

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Computer Vision Playground')
        self.setWindowIcon(QIcon('assets/app-icon.png'))

        self.init_menubar()

        self.init_central_widget()

        self.statusBar().showMessage('Ready')
        self.center()
        self.show()

    def center(self):
        # Adjust the window size
        self.central_widget.adjustSize()
        self.adjustSize()

        # Center the app
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_central_widget(self):
        # Show the sample image
        self.lbl_img.setPixmap(QPixmap(self.file_name))
        self.vbox.addWidget(self.lbl_img)

        self.central_widget.setLayout(self.vbox)
        self.setCentralWidget(self.central_widget)

    def init_menubar(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # File menus
        menu_file = menubar.addMenu('&File')
        # Open menu
        action_open = QAction('Open', self)
        action_open.setShortcut('Ctrl+O')
        action_open.setStatusTip('Open an image file')
        action_open.triggered.connect(self.open_file)
        menu_file.addAction(action_open)
        # Exit menu
        menu_file.addSeparator()
        action_exit = QAction('Exit', self)
        action_exit.setShortcut('Ctrl+Q')
        action_exit.setStatusTip('Quit application')
        action_exit.triggered.connect(qApp.quit)
        menu_file.addAction(action_exit)

    def open_file(self):
        self.file_name = \
            QFileDialog.getOpenFileName(self, 'Open an image file', '/home', 'Images (*.png *.jpg *.jpeg)')[0]

        if self.file_name:
            self.update_pixmap(self.file_name)

    def update_pixmap(self, file_name):
        pixmap = QPixmap(file_name)

        # Scale the pixmap if it's too large
        screen_avail = QDesktopWidget().availableGeometry()
        max_width = int(screen_avail.width() * 0.8)
        max_height = int(screen_avail.height() * 0.8)
        if pixmap.size().width() > max_width:
            pixmap = pixmap.scaledToWidth(max_width)
        if pixmap.size().height() > max_height:
            pixmap = pixmap.scaledToHeight(max_height)

        # Update the center widget with the pixmap
        self.lbl_img.setPixmap(pixmap)
        self.center()


# Main function
# Init the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit((app.exec_()))
