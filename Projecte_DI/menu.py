import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ofertas import Ofertas
from pedir_cita import PedirCita
from perfil import Perfil

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Menu')
        self.setGeometry(250, 250, 550, 850)
        self.pedir_cita=PedirCita()
        self.perfil=Perfil()
        self.ofertas=Ofertas()
        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: rgb(70, 130, 180);
                color: #336699;
            }

            QMenuBar {
                background-color: white;
                font-size: 40px;
            }

            QMenuBar::item {
                background-color: #f0f0f0;
                color: #336699;
                padding: 12px 12px;
                font-size: 30px;
            }

            QMenuBar::item:selected {
                background-color: #336699;
                color: white;
            }

            QMenu {
                background-color: #f0f0f0;
                color: #336699;
                border: 1px solid #336699;
            }

            QMenu::item {
                padding: 6px 24px;
            }

            QMenu::icon {
                width: 40px;
                height: 40px;
            }
            QLabel#titleLabel {
                font-size: 40px;
                color: white;
                background-color: #336699;
                padding: 20px;
                text-align: center;
            }
            '''
        )
        self.initUI()

    def initUI(self):
        # Crear un layout vertical para organizar los elementos en la ventana principal
        layout = QVBoxLayout()

        font = QFont() 
        font.setPointSize(20)  

        # Agregar el título "Pedir Cita" al layout
        texto_pedir_cita = QLabel("Pedir Cita", self)
        texto_pedir_cita.setAlignment(Qt.AlignCenter)
        texto_pedir_cita.setFont(font)  # Aplica la fuente al QLabel
        layout.addWidget(texto_pedir_cita)

        imagen_pedir_cita = QLabel(self)
        imagen_pedir_cita.setPixmap(QPixmap("Projecte_DI/images/foto_menu1.png"))  # Ruta de la primera imagen
        imagen_pedir_cita.setAlignment(Qt.AlignCenter)
        layout.addWidget(imagen_pedir_cita)


        texto_ofertas = QLabel("Ofertas", self)
        texto_ofertas.setAlignment(Qt.AlignCenter)
        texto_ofertas.setFont(font)
        layout.addWidget(texto_ofertas)


        imagen_ofertas = QLabel(self)
        imagen_ofertas.setPixmap(QPixmap("Projecte_DI/images/foto_menu2.png"))  # Ruta de la segunda imagen
        imagen_ofertas.setAlignment(Qt.AlignCenter)
        layout.addWidget(imagen_ofertas)

        # Conectar las señales de clic de las imágenes a las funciones correspondientes
        imagen_pedir_cita.mousePressEvent = self.abrirVentanaPedirCita
        imagen_ofertas.mousePressEvent = self.abrirVentanaOfertas

        # Agregar el botón "Ver Menú" al layout
        btn_ver_menu = QPushButton("Ver Menú", self)
        btn_ver_menu.clicked.connect(self.mostrarMenu)
        layout.addWidget(btn_ver_menu, alignment=Qt.AlignCenter)

        # Crear un widget contenedor y asignar el layout
        container_widget = QWidget(self)
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

        exit_action = QAction('Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.confirmarSalir)  

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
       # Menú para el icono del menú desplegable
        popup_menu = QMenu(self)
        popup_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; ')


        action_pedir_cita = QAction('Pedir Cita', self)
        action_pedir_cita.setShortcut('Ctrl+P')
        action_opcion2 = QAction('Perfil', self)
        action_opcion2.setShortcut('Ctrl+O')
        action_ofertas=QAction("Ofertas", self)
        action_ofertas.setShortcut('Ctrl+A')

        action_pedir_cita.triggered.connect(self.abrirVentanaPedirCita)
        action_opcion2.triggered.connect(self.abrirVentanaPerfil)
        action_ofertas.triggered.connect(self.abrirVentanaOfertas)

        # Agregar las acciones al menú
        popup_menu.addAction(action_pedir_cita)
        popup_menu.addAction(action_ofertas)
        popup_menu.addAction(action_opcion2)


        popup_menu.addSeparator()
        popup_menu.addAction(exit_action)

        popup_menu.aboutToShow.connect(lambda: self.adjustMenuHeight(popup_menu))

        # Icono del menú desplegable
        icon_path_menu = "Projecte_DI/images/icono_menu.png"
        menu_icon = QIcon(icon_path_menu)
        menu_action = menubar.addAction(menu_icon, '')
        menu_action.setMenu(popup_menu)

        # Menú para el icono del perfil
        profile_menu = QMenu(self)
        profile_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; align:rigth ')

        profile_action = QAction(self)
        profile_action.setIcon(QIcon("Projecte_DI/images/perfil.jpg"))
        profile_menu.addAction(profile_action)

        menubar.addMenu(profile_menu)

        self.adjustMenuHeight(popup_menu)  # Ajustar la altura del menú desplegable

    def confirmarSalir(self):
        confirmar_salida = QMessageBox.question(
            self, 'Confirmar salida', '¿Estás seguro de que deseas salir?',
            QMessageBox.Yes | QMessageBox.No)
        if confirmar_salida == QMessageBox.Yes:
            QApplication.quit()

    # Definir la función para abrir la ventana de ofertas(Completar la pagina Oferta)
    def abrirVentanaOfertas(self, event):
        print("Abriendo ventana de ofertas")
        try:
            self.ofertas.show()
        except Exception as e:
                print(f"Error al abrir la ventana de pedir cita: {e}")

    def abrirVentanaPedirCita(self, event):
        print("Abriendo ventana de pedir cita")
        try:
            self.pedir_cita.show()
        except Exception as e:
            print(f"Error al abrir la ventana de pedir cita: {e}")

    def abrirVentanaPerfil(self):
        print("Abriendo ventana de perfil")
        try:
            self.perfil.show()
        except Exception as e:
            print(f"Error al abrir la ventana de perfil: {e}")

    def adjustMenuHeight(self, menu):
        # Ajustar el menú para que se acople a la ventana
        menu_height = self.height() - self.menuBar().height() - 2
        menu.setFixedHeight(menu_height)

    def mostrarMenu(self):
        # Mostrar el menú desplegable dentro de la ventana
        print("Mostrando menú desplegable")
        menu_action = self.menuBar().actions()[0]  # Obtener la acción del menú
        menu = menu_action.menu()  # Obtener el menú desplegable asociado a la acción del menú
        if menu is not None:  # Verificar si la acción del menú está asociada con un menú desplegable
            self.adjustMenuHeight(menu)  # Ajustar la altura del menú
            menu.show()  # Mostrar el menú desplegable
        else:
            print("La acción del menú no está asociada con un menú desplegable")

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
