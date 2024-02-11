import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from inici_sesio import Inici_Sesion
from menu import *


class Inici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealtMate - Inicio')
        self.setGeometry(250, 250, 550, 850)
        self.setStyleSheet("background-color: rgb(70, 130, 180);")
        self.initUI()

    def initUI(self):
        self.main_menu = Menu() 
        self.inici_secio=Inici_Sesion()
        self.main_menu.setWindowFlags(Qt.Widget)
        self.inici_secio.setWindowFlag(Qt.Widget)
        logo_label = QLabel(self)
        pixmap = QPixmap("Projecte_DI/images/Logo.png") 
        
        # Redondear la imagen
        rounded_pixmap = self.roundImage(pixmap)
        logo_label.setPixmap(rounded_pixmap)
        
        window_width = self.frameGeometry().width()
        image_width = pixmap.width()
        image_height = pixmap.height()
        center_x = (window_width - image_width) // 2
        logo_label.setGeometry(center_x, 0, image_width, image_height)

        # Crear un widget y un layout vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Añadir la etiqueta del logo al layout
        layout.addWidget(logo_label)
        layout.addStretch()  # Añadir espacio para separar los botones y ponerlos al final


        btn_login = QPushButton('Iniciar Sesión/Registrarse', self)
        btn_login.setStyleSheet("background-color: blue; color: white; font-size: 16px;")
        layout.addWidget(btn_login)
        btn_login.setMinimumWidth(200) 
        btn_login.setMinimumHeight(50)  
        btn_login.clicked.connect(self.showInici)


        btn_guest = QPushButton('Acceder como Invitado', self)
        btn_guest.setStyleSheet("background-color: blue; color: white; font-size: 16px;")
        layout.addWidget(btn_guest)
        btn_guest.setMinimumWidth(200) 
        btn_guest.setMinimumHeight(50)  
        btn_guest.clicked.connect(self.showMainMenu)


        layout.setAlignment(Qt.AlignHCenter)

    def showInici(self):
        self.inici_secio.show()

    def showMainMenu(self):
        # Si se hace clic en "Acceder como Invitado", agrega el usuario invitado al JSON
        if self.sender().text() == 'Acceder como Invitado':
            self.inici_secio.addUsuarioInvitado()

        self.close()
        self.main_menu.show() 

    def roundImage(self, pixmap):
        # Redondear la imagen y devolver un QPixmap
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        path = QPainterPath()
        path.addEllipse(0, 0, pixmap.width(), pixmap.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        return rounded_pixmap

def main():
    app = QApplication(sys.argv)
    inici = Inici()
    inici.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
