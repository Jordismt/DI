import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from menu import *
from inici_sesio import *

class Inici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealtMate')
        self.setGeometry(250, 250, 550, 850)
        self.setStyleSheet("background-color: #FAEBD7")
        self.initUI()

    def initUI(self):
        self.main_menu = Menu() 
        self.inici_secio=Inici_Sesion()
        self.main_menu.setWindowFlags(Qt.Widget)
        self.inici_secio.setWindowFlag(Qt.Widget)
        logo_label = QLabel(self)
        pixmap = QPixmap("Projecte_DI/images/Logo.png") 
        logo_label.setPixmap(pixmap)
        window_width = self.frameGeometry().width()
        image_width = pixmap.width()
        image_height = pixmap.height()
        center_x = (window_width - image_width) // 2
        logo_label.setGeometry(center_x, 0, image_width, image_height)

        # Crear un widget i un layout vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Añadir la etiqueta del logo al layout
        layout.addWidget(logo_label)
        layout.addStretch()  #Añadir espai per a separar els botons i posarlos al final bax de tot

        # Botón para iniciar sesión
        btn_login = QPushButton('Iniciar Sesión/Registrarse', self)
        layout.addWidget(btn_login)
        btn_login.setMinimumWidth(200) 
        btn_login.setMinimumHeight(50)  
        btn_login.setStyleSheet("background-color: withe")
        btn_login.clicked.connect(self.showInici)

        # Botón para acceder como invitado
        btn_guest = QPushButton('Acceder como Invitado', self)
        layout.addWidget(btn_guest)
        btn_guest.setMinimumWidth(200) 
        btn_guest.setMinimumHeight(50)  
        btn_guest.setStyleSheet("background-color: withe")
        btn_guest.clicked.connect(self.showMainMenu)

        # Ajustar botons al centre
        layout.setAlignment(Qt.AlignHCenter)
        
      

    def showInici(self):
        self.inici_secio.show()
    def showMainMenu(self):
        self.close()
        self.main_menu.show()  
def main():
    app = QApplication(sys.argv)
    inici = Inici()
    inici.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()