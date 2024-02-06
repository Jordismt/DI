import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class Perfil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate')
        self.setGeometry(250, 250, 550, 850)
        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: rgb(70, 130, 180);  /* Cambiar el fondo de la ventana a negro */
                color: #ffffff;  /* Cambiar el color del texto a blanco */
            }
            QToolBar {
                background-color: black;  /* Cambiar el fondo del app bar a blanco */
                border-bottom: 2px solid #cccccc;
            }
            QAction {
                color: black;  /* Cambiar el color del texto del botón de atrás a negro */
            }
            QLabel {
                font-size: 16px;
                margin-bottom: 10px;
            }
            QComboBox, QPushButton {
                font-size: 16px;
                padding: 8px 16px;
            }
            QPushButton {
                background-color: #336699;
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #428bca;
            }
            '''
        )
        self.initUI()

    def initUI(self):
        # Crear el appbar
        appbar = QToolBar(self)
        appbar.setFixedHeight(50)  # Establecer una altura fija para el appbar

        # Agregar un botón de atrás al appbar
        back_button = QAction('Atrás', self)
        back_button.triggered.connect(self.back)
        appbar.addAction(back_button)

        # Crear un widget con política de tamaño expansiva para empujar la imagen al otro lado
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        appbar.addWidget(spacer)

        # Agregar la imagen de perfil al appbar
        icon_path_perfil = "Projecte_DI/images/perfil.jpg"
        icon_perfil = QIcon(icon_path_perfil)
        appbar.addAction(icon_perfil, "")

        # Configurar el appbar como widget de la ventana
        self.addToolBar(Qt.TopToolBarArea, appbar)

        # Crear un layout vertical para organizar las etiquetas y widgets
        layout = QVBoxLayout()

        # Crear un combo box para seleccionar el tipo de mascota
        tipo_mascota_combo = QComboBox()
        tipo_mascota_combo.addItems(["Tipo de mascota", "Perro", "Gato", "Ave", "Reptil", "Roedor", "Pez", "Conejo", "Caballo", "Otro"])
        tipo_mascota_combo.setCurrentText("Tipo de mascota")  # Establecer "Tipo de mascota" como la opción por defecto
        layout.addWidget(tipo_mascota_combo)

        # Crear etiquetas para mostrar la información del usuario
        nombre_label = QLabel("Nombre: Usuario")
        id_label = QLabel("ID: 123456")
        correo_label = QLabel("Correo electrónico: usuario@example.com")

        # Establecer alineación para las etiquetas
        nombre_label.setAlignment(Qt.AlignCenter)
        id_label.setAlignment(Qt.AlignCenter)
        correo_label.setAlignment(Qt.AlignCenter)

        # Agregar las etiquetas al layout
        layout.addWidget(nombre_label)
        layout.addWidget(id_label)
        layout.addWidget(correo_label)

        # Crear un widget para organizar las etiquetas y el combo box
        info_widget = QWidget()
        info_widget.setLayout(layout)

        # Agregar el widget de información al layout principal
        layout.addWidget(info_widget)

        # Crear un botón para cerrar sesión
        cerrar_sesion_button = QPushButton("Cerrar Sesión")
        cerrar_sesion_button.clicked.connect(self.cerrarSesion)

        # Agregar el botón al layout
        layout.addWidget(cerrar_sesion_button)

        # Establecer espaciado y margen para el layout principal
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def back(self):
        self.close()

    def cerrarSesion(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    perfil = Perfil()
    perfil.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
