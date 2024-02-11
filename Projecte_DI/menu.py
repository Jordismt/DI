import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from tienda import TiendaApp
from ofertas import Ofertas
from pedir_cita import PedirCita
from perfil import Perfil
from opiniones import OpinionWindow
from foro_comunity import CommunityForum
from Adopcion import VentanaAdopcion
from aseo_mascotas import VentanaAseo

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Menu')
        self.setGeometry(250, 250, 550, 850)
        self.pedir_cita = PedirCita()
        self.perfil = Perfil()
        self.ofertas = Ofertas()
        self.tienda = TiendaApp()
        self.opinion=OpinionWindow()
        self.foro=CommunityForum()
        self.adopcio=VentanaAdopcion()
        self.aseo=VentanaAseo()

        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: rgb(70, 130, 180);
                color: #ffffff;
            }

            QMenuBar {
                background-color: #336699;
                font-size: 16px;
                color: #ffffff;
            }

            QMenuBar::item {
                background-color: #336699;
                color: #ffffff;
                padding: 8px 16px;
                font-size: 16px;
            }

            QMenuBar::item:selected {
                background-color: #ffffff;
                color: #336699;
            }

            QMenu {
                background-color: #ffffff;
                color: #336699;
                border: 1px solid #336699;
            }

            QMenu::item {
                padding: 6px 24px;
            }

            QMenu::icon {
                width: 24px;
                height: 24px;
            }

            QLabel#titleLabel {
                font-size: 36px;
                color: white;
                background-color: #336699;
                padding: 20px;
                text-align: center;
            }

            QLabel#sectionLabel {
                font-size: 24px;
                color: #336699;
                padding: 20px;
                text-align: center;
            }

            QLabel#imageLabel {
                padding: 40px;
            }
            '''
        )
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        font = QFont() 
        font.setPointSize(18)  

        title_label = QLabel("HealthMate", self)
        title_label.setObjectName("titleLabel")

        layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        scroll_layout.addWidget(self.createSection("Pedir Cita", "Projecte_DI/images/foto_menu1.png", self.abrirVentanaPedirCita))
        scroll_layout.addWidget(self.createSection("Ofertas", "Projecte_DI/images/foto_menu2.png", self.abrirVentanaOfertas))

        # Redimensionar la imagen 
        image_path_tienda = "Projecte_DI/images/tienda.jpeg"
        pixmap_tienda = QPixmap(image_path_tienda)
        small_pixmap_tienda = pixmap_tienda.scaled(250, 250) 
        scroll_layout.addWidget(self.createSection("Tienda", small_pixmap_tienda, self.abrirVentanaTienda))


        image_path_adopcio= "Projecte_DI/images/adopcio.jpeg"
        pixmap_adopcio=QPixmap(image_path_adopcio)
        small_pixmap_adopcio=pixmap_adopcio.scaled(255,255)
        scroll_layout.addWidget(self.createSection("Adoptar Mascota", small_pixmap_adopcio, self.abrirVentanaAdopcio))


        image_path_aseo= "Projecte_DI/images/aseo_mascota.jpeg"
        pixmap_aseo=QPixmap(image_path_aseo)
        small_pixmap_aseo=pixmap_aseo.scaled(255,255)
        scroll_layout.addWidget(self.createSection("Aseo Mascotas", small_pixmap_aseo, self.abrirVentanaAseo))


        btn_opiniones=QPushButton("Opiniones")
        btn_opiniones.setStyleSheet("padding:10px; margin:auto ; background-color: blue; color: white; ")
        btn_opiniones.clicked.connect(self.abrirVentanaOpiniones)

        btn_forum=QPushButton("Foro de la comunidad")
        btn_forum.setStyleSheet("padding:10px; margin:auto ; background-color: blue; color: white; ")
        btn_forum.clicked.connect(self.abrirVentanaForo)


        scroll_layout.addWidget(btn_opiniones)
        scroll_layout.addWidget(btn_forum)


        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        container_widget = QWidget(self)
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

        exit_action = QAction('Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.confirmarSalir)  

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        ayuda_menu = menubar.addMenu('Ayuda')

        ayuda_pedir_cita = QAction('Ayuda al Pedir Cita', self)
        ayuda_pedir_cita.triggered.connect(self.mostrarAyudaPedirCita)
        ayuda_menu.addAction(ayuda_pedir_cita)

        ayuda_crear_cuenta = QAction('Ayuda al Crear Cuenta', self)
        ayuda_crear_cuenta.triggered.connect(self.mostrarAyudaCrearCuenta)
        ayuda_menu.addAction(ayuda_crear_cuenta)

        popup_menu = QMenu(self)
        popup_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; ')

        action_pedir_cita = QAction('Pedir Cita', self)
        action_pedir_cita.setShortcut('Ctrl+P')
        action_perfil = QAction('Perfil', self)
        action_perfil.setShortcut('Ctrl+O')
        action_ofertas=QAction("Ofertas", self)
        action_ofertas.setShortcut('Ctrl+A')
        action_tienda=QAction("Tienda", self)
        action_tienda.setShortcut('Ctrl+T')
        action_opiniones=QAction("Opiniones", self)
        action_opiniones.setShortcut('Ctrl+M')
        action_foro=QAction("Foro", self)
        action_foro.setShortcut("Ctrl+F")
        action_adopcion=QAction("Adopcion", self)
        action_adopcion.setShortcut("Ctrl+Z")
        action_cuidado=QAction("Cuidado Mascotas", self)
        action_cuidado.setShortcut("Ctrl+C")

        action_pedir_cita.triggered.connect(self.abrirVentanaPedirCita)
        action_perfil.triggered.connect(self.abrirVentanaPerfil)
        action_ofertas.triggered.connect(self.abrirVentanaOfertas)
        action_tienda.triggered.connect(self.abrirVentanaTienda)
        action_opiniones.triggered.connect(self.abrirVentanaOpiniones)
        action_foro.triggered.connect(self.abrirVentanaForo)
        action_adopcion.triggered.connect(self.abrirVentanaAdopcio)
        action_cuidado.triggered.connect(self.abrirVentanaAseo)

        popup_menu.addAction(action_pedir_cita)
        popup_menu.addAction(action_ofertas)
        popup_menu.addAction(action_perfil)
        popup_menu.addAction(action_tienda)
        popup_menu.addAction(action_opiniones)
        popup_menu.addAction(action_foro)
        popup_menu.addAction(action_adopcion)
        popup_menu.addAction(action_cuidado)

        popup_menu.addSeparator()
        popup_menu.addAction(exit_action)

        popup_menu.aboutToShow.connect(lambda: self.adjustMenuHeight(popup_menu))

        icon_path_menu = "Projecte_DI/images/icono_menu.png"
        menu_icon = QIcon(icon_path_menu)
        menu_action = menubar.addAction(menu_icon, '')
        menu_action.setMenu(popup_menu)

        profile_menu = QMenu(self)
        profile_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; align:rigth ')

        profile_action = QAction(self)
        profile_action.setIcon(QIcon("Projecte_DI/images/perfil.jpg"))
        profile_menu.addAction(profile_action)

        menubar.addMenu(profile_menu)

        self.adjustMenuHeight(popup_menu)

        # Footer
        footer_widget = self.createFooter()
        layout.addWidget(footer_widget)

    def createSection(self, title, image_path, click_handler):
        section_layout = QVBoxLayout()

        font = QFont() 
        font.setPointSize(16)  

        section_label = QLabel(title, self)
        section_label.setObjectName("sectionLabel")
        section_label.setFont(font)
        section_label.setAlignment(Qt.AlignCenter)

        section_layout.addWidget(section_label)

        image_label = QLabel(self)
        image_label.setPixmap(QPixmap(image_path))
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setObjectName("imageLabel")

        section_layout.addWidget(image_label)

        image_label.mousePressEvent = click_handler

        section_widget = QWidget(self)
        section_widget.setLayout(section_layout)

        return section_widget

    def confirmarSalir(self):
        confirmar_salida = QMessageBox.question(
            self, 'Confirmar salida', '¿Estás seguro de que deseas salir?',
            QMessageBox.Yes | QMessageBox.No)
        if confirmar_salida == QMessageBox.Yes:
            QApplication.quit()

    def abrirVentanaOfertas(self, event):
        print("Abriendo ventana de ofertas")
        try:
            self.ofertas.show()
        except Exception as e:
                print(f"Error al abrir la ventana de ofertas: {e}")

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

    def abrirVentanaTienda(self, event):
        self.tienda.show()

    def abrirVentanaOpiniones(self, event):
        self.opinion.show()

    def abrirVentanaForo(self, event):
        self.foro.show()

    def abrirVentanaAdopcio(self, event):
        self.adopcio.show()

    def abrirVentanaAseo(self, event):
        self.aseo.show()


    def adjustMenuHeight(self, menu):
        menu_height = self.height() - self.menuBar().height() - 2
        menu.setFixedHeight(menu_height)


    def mostrarAyudaPedirCita(self):
        ayuda = "Instrucciones para pedir una cita: \n\n1. Selecciona la opción 'Pedir Cita' del menú.\n2. Completa el formulario con tus datos personales y la fecha/hora deseada.\n3. Confirma la cita para finalizar el proceso."
        QMessageBox.information(self, 'Ayuda al Pedir Cita', ayuda)

    def mostrarAyudaCrearCuenta(self):
        ayuda = "Instrucciones para crear una cuenta: \n\n1. Selecciona la opción 'Crear Cuenta' del menú.\n2. Completa el formulario con tu información personal.\n3. Verifica tu dirección de correo electrónico.\n4. ¡Listo! Ya puedes acceder a tu perfil y otras funcionalidades."
        QMessageBox.information(self, 'Ayuda al Crear Cuenta', ayuda)


    def createFooter(self):
        footer_widget = QWidget()
        layout = QHBoxLayout()

        # Espacio flexible para centrar las imágenes
        layout.addStretch()

        # YouTube image
        youtube_label = QLabel()
        youtube_pixmap = QPixmap("Projecte_DI/images/youtube.png")  
        youtube_label.setPixmap(youtube_pixmap.scaledToWidth(30))  #Ancho de la imagen
        layout.addWidget(youtube_label)

        # Instagram image
        instagram_label = QLabel()
        instagram_pixmap = QPixmap("Projecte_DI/images/instagram.png")  
        instagram_label.setPixmap(instagram_pixmap.scaledToWidth(30))  
        instagram_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(instagram_label)

        tiktok_label=QLabel()
        tiktok_pixmap=QPixmap("Projecte_DI/images/tiktok.png")
        tiktok_label.setPixmap(tiktok_pixmap.scaledToWidth(30))
        tiktok_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(tiktok_label)


        # Espacio flexible para centrar las imágenes
        layout.addStretch()

        footer_widget.setLayout(layout)

        return footer_widget



def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
