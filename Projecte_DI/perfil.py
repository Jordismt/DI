import sys
import random
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from crear_cuenta import VentanaCrearCuenta
from ofertas import Ofertas

class Perfil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Perfil')
        self.setGeometry(250, 250, 550, 600)  # Se ajusta la altura de la ventana
        self.oferta = Ofertas()
        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: #f0f0f0;  /* Cambiar el fondo de la ventana a un tono gris claro */
                color: #333333;  /* Cambiar el color del texto a un tono gris oscuro */
            }
            QLabel {
                font-size: 18px;  /* Reducir el tamaño del texto */
                margin-bottom: 10px;  /* Reducir el margen inferior */
                color: #333333; /* Color del texto */
            }
            QPushButton {
                background-color: #007bff; /* Color de fondo del botón (azul) */
                color: #ffffff; /* Color del texto del botón (blanco) */
                border: none; /* Eliminar borde */
                padding: 8px 16px; /* Espaciado interno del botón */
                border-radius: 5px; /* Borde redondeado */
            }
            QPushButton:hover {
                background-color: #0056b3; /* Cambio de color al pasar el cursor sobre el botón */
            }
            QLineEdit {
                padding: 8px; /* Espaciado interno del cuadro de texto */
                border: 1px solid #cccccc; /* Borde del cuadro de texto */
                border-radius: 5px; /* Borde redondeado */

            }
            QComboBox {
                padding: 5px; /* Espaciado interno del combo box */
                border: 1px solid #cccccc; /* Borde del combo box */
                border-radius: 5px; /* Borde redondeado */
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

        # Crear un widget con política de tamaño expansiva para poner la imagen al otro lado
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

        # Abrir el archivo que contiene el nombre del usuario
        try:
            with open('Projecte_DI/datos/temp_username.txt', 'r') as file:
                nombre_usuario = file.read()
        except FileNotFoundError:
            nombre_usuario = "Usuario Desconocido"

        # Mostrar el nombre del usuario en un QLabel
        nombre_label = QLabel(f"<b>Nombre:</b> {nombre_usuario}")  # Negrita para el nombre

        # Generar un ID aleatorio entre 1 y 100
        id_usuario = random.randint(1, 100)
        id_label = QLabel(f"<b>ID:</b> {id_usuario}")  # Negrita para el ID

        # Configurar alineación para las etiquetas
        nombre_label.setAlignment(Qt.AlignCenter)
        id_label.setAlignment(Qt.AlignCenter)

        # Agregar las etiquetas al layout
        layout.addWidget(nombre_label)
        layout.addWidget(id_label)

        # Agregar campos de entrada para la información de contacto y los datos de la mascota
        contacto_label = QLabel("<b>Información de Contacto:</b>")  # Negrita para la etiqueta
        contacto_text = QLineEdit()  # Campo de entrada para la información de contacto
        mascota_label = QLabel("<b>Datos de la Mascota:</b>")  # Negrita para la etiqueta
        mascota_text = QLineEdit()  # Campo de entrada para los datos de la mascota

        layout.addWidget(contacto_label)
        layout.addWidget(contacto_text)
        layout.addWidget(mascota_label)
        layout.addWidget(mascota_text)

        # Agregar sección para mostrar el historial de citas
        historial_label = QLabel("<b>Historial de Citas:</b>")  # Negrita para la etiqueta
        historial_text = QTextEdit()
        historial_text.setReadOnly(True)  # El historial de citas es solo para lectura

        # Simular algunos datos de historial de citas
        historial_text.append("<b>Fecha:</b> 2024-01-01, <b>Servicio:</b> Vacunación, <b>Veterinario:</b> Dr. Pérez")
        historial_text.append("<b>Fecha:</b> 2024-01-15, <b>Servicio:</b> Revisión, <b>Veterinario:</b> Dra. Martínez")

        layout.addWidget(historial_label)
        layout.addWidget(historial_text)

        # Agregar sección para configurar las preferencias de notificación
        notificacion_label = QLabel("<b>Preferencias de Notificación:</b>")  # Negrita para la etiqueta
        notificacion_combo = QComboBox()
        notificacion_combo.addItems(["Seleccionar...", "Teléfono", "Correo"])

        notificacion_cuadro_label = QLabel("<b>Correo electrónico o Teléfono:</b>")  # Negrita para la etiqueta
        notificacion_cuadro = QLineEdit()
        notificacion_cuadro.setVisible(False)  # Ocultar el cuadro de texto inicialmente

        # Conectar la señal de cambio en el combo box a una función que muestre u oculte el cuadro de texto según la selección
        notificacion_combo.currentTextChanged.connect(lambda text: notificacion_cuadro.setVisible(text != "Seleccionar..."))

        layout.addWidget(notificacion_label)
        layout.addWidget(notificacion_combo)
        layout.addWidget(notificacion_cuadro_label)
        layout.addWidget(notificacion_cuadro)

        # Crear un botón para ver ofertas
        ver_ofertas_button = QPushButton("Ver Ofertas")
        ver_ofertas_button.clicked.connect(self.verOfertas)

        # Agregar el botón de ver ofertas al layout
        layout.addWidget(ver_ofertas_button)

        # Crear un botón para crear cuenta
        crear_cuenta_button = QPushButton("Crear Cuenta")
        crear_cuenta_button.clicked.connect(self.crearCuenta)

        # Agregar el botón de crear cuenta antes del botón de cerrar sesión
        layout.addWidget(crear_cuenta_button)

        # Crear un botón para cerrar sesión
        cerrar_sesion_button = QPushButton("Cerrar Sesión")
        cerrar_sesion_button.clicked.connect(self.close_sesion)

        # Agregar el botón de cerrar sesión al layout
        layout.addWidget(cerrar_sesion_button)

        # Agregar un espacio en blanco al final para que la ventana no se vea demasiado apretada
        layout.addStretch(1)

        # Establecer espaciado y margen para el layout principal
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def back(self):
        self.close()

    def close_sesion(self):
        if os.path.exists('Projecte_DI/datos/temp_username.txt'):
            os.remove('Projecte_DI/datos/temp_username.txt')
        self.close()

    def verOfertas(self):
        self.oferta.show()

    def crearCuenta(self):
        ventana = VentanaCrearCuenta()
        ventana.exec_()



def main():
    app = QApplication(sys.argv)
    perfil = Perfil()
    perfil.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
