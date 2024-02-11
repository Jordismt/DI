import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class VentanaAseo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Servicios de Aseo para Mascotas')
        self.setGeometry(100, 100, 600, 400)

        # Etiqueta de título
        titulo_label = QLabel('<h1 style="text-align: center; color: #3498db;">Servicios de Aseo para Mascotas</h1>')

        # Menú desplegable para seleccionar el tipo de mascota
        tipo_mascota_label = QLabel('Tipo de Mascota:')
        self.tipo_mascota_combo = QComboBox()
        self.tipo_mascota_combo.addItems(['Perro', 'Gato', 'Ave', 'Conejo', 'Otros'])
        self.tipo_mascota_combo.currentTextChanged.connect(self.mostrar_cuadro_otro)

        # Cuadro de texto para especificar el tipo de mascota si se selecciona "Otros"
        self.cuadro_otro = QLineEdit()
        self.cuadro_otro.setPlaceholderText('Especificar tipo de mascota')
        self.cuadro_otro.setVisible(False)

        # Botones para los diferentes servicios con iconos
        cortar_uñas_button = QPushButton('Cortar Uñas')
        lavado_button = QPushButton('Lavado')
        corte_pelo_button = QPushButton('Corte de Pelo')

        # Estilos para los botones
        self.estilo_botones([cortar_uñas_button, lavado_button, corte_pelo_button])

        # Conexiones de los botones con sus respectivas acciones
        cortar_uñas_button.clicked.connect(self.reservar_corte_uñas)
        lavado_button.clicked.connect(self.reservar_lavado)
        corte_pelo_button.clicked.connect(self.reservar_corte_pelo)

        # Diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(titulo_label)
        layout.addWidget(tipo_mascota_label)
        layout.addWidget(self.tipo_mascota_combo)
        layout.addWidget(self.cuadro_otro)
        layout.addSpacing(20)  # Espacio entre widgets
        layout.addWidget(cortar_uñas_button)
        layout.addWidget(lavado_button)
        layout.addWidget(corte_pelo_button)
        self.setLayout(layout)

    def estilo_botones(self, botones):
        for boton in botones:
            boton.setStyleSheet("background-color: #3498db; color: white; font-weight: bold; padding: 10px; border-radius: 10px;")
            boton.setIconSize(QSize(48, 48))
            boton.setCursor(Qt.PointingHandCursor)

    def mostrar_cuadro_otro(self, texto):
        if texto == 'Otros':
            self.cuadro_otro.setVisible(True)
        else:
            self.cuadro_otro.setVisible(False)

    def mostrar_dialogo_reserva(self, servicio):
        dialogo_reserva = QDialog(self)
        dialogo_reserva.setWindowTitle(f'Reservar {servicio}')
        dialogo_reserva.setFixedSize(300, 200)

        # Crear formulario de reserva
        nombre_label = QLabel('Nombre:')
        nombre_input = QLineEdit()
        fecha_label = QLabel('Fecha:')
        fecha_input = QDateEdit()
        fecha_input.setCalendarPopup(True)
        fecha_input.setDate(QDate.currentDate())
        hora_label = QLabel('Hora:')
        hora_input = QTimeEdit()
        hora_input.setDisplayFormat('HH:mm')
        hora_input.setTime(QTime.currentTime())

        aceptar_button = QPushButton('Aceptar')
        aceptar_button.clicked.connect(dialogo_reserva.accept)

        cancelar_button = QPushButton('Cancelar')
        cancelar_button.clicked.connect(dialogo_reserva.reject)

        layout = QGridLayout()
        layout.addWidget(nombre_label, 0, 0)
        layout.addWidget(nombre_input, 0, 1)
        layout.addWidget(fecha_label, 1, 0)
        layout.addWidget(fecha_input, 1, 1)
        layout.addWidget(hora_label, 2, 0)
        layout.addWidget(hora_input, 2, 1)
        layout.addWidget(aceptar_button, 3, 0)
        layout.addWidget(cancelar_button, 3, 1)

        dialogo_reserva.setLayout(layout)

        if dialogo_reserva.exec() == QDialog.Accepted:
            nombre = nombre_input.text()
            fecha = fecha_input.date().toString(Qt.ISODate)
            hora = hora_input.time().toString(Qt.ISODate)


    def reservar_corte_uñas(self):
        self.mostrar_dialogo_reserva('Corte de Uñas')

    def reservar_lavado(self):
        self.mostrar_dialogo_reserva('Lavado')

    def reservar_corte_pelo(self):
        self.mostrar_dialogo_reserva('Corte de Pelo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_aseo = VentanaAseo()
    ventana_aseo.show()
    sys.exit(app.exec())
