import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime


class CalendarioApp(QMainWindow):
    # Agregar la señal 'cita_agendada'
    cita_agendada = Signal(QDate, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendario en PyQt")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Agregar el widget de calendario
        self.calendario = QCalendarWidget()
        self.calendario.setFixedSize(400, 230)
        self.layout.addWidget(self.calendario, alignment=Qt.AlignHCenter)

        # Agregar un botón para solicitar una cita
        self.button_pedir_cita = QPushButton('Pedir Cita', self)
        self.button_pedir_cita.setFixedSize(self.calendario.width(), 20)
        self.layout.addWidget(self.button_pedir_cita, alignment=Qt.AlignHCenter)

        # Añadir espacio en blanco abajo para centrar el calendario arriba
        self.layout.addStretch()

        # Conectar la señal selectionChanged del calendario a la función de verificación de citas
        self.calendario.selectionChanged.connect(self.verificarCitas)

        # Inicializar el contador de citas por día
        self.citas_por_dia = {}

        # Inicializar el usuario logueado como None (nadie logueado)
        self.usuario_logueado = None

        # Conectar el botón para solicitar una cita a la función correspondiente
        self.button_pedir_cita.clicked.connect(self.solicitarCita)

    def verificarCitas(self):
        # Obtener la fecha seleccionada
        fecha_seleccionada = self.calendario.selectedDate()

        # Verificar si hay más de 5 citas en el día seleccionado
        if fecha_seleccionada in self.citas_por_dia and self.citas_por_dia[fecha_seleccionada] >= 5:
            QMessageBox.warning(self, 'Limite de Citas', 'Ya se han agendado 5 citas para este día. Elija otra fecha.')
            # Deshacer la selección
            self.calendario.setSelectedDate(self.fecha_anterior)
        else:
            # Guardar la fecha actual para futuras comparaciones
            self.fecha_anterior = fecha_seleccionada

    def solicitarCita(self):
        # Obtener la fecha seleccionada
        fecha_seleccionada = self.calendario.selectedDate()

        # Incrementar el contador de citas para la fecha seleccionada
        self.citas_por_dia[fecha_seleccionada] = self.citas_por_dia.get(fecha_seleccionada, 0) + 1

        # Emitir la señal con la fecha y el usuario logueado
        self.cita_agendada.emit(fecha_seleccionada, self.usuario_logueado)

        # Mostrar información en el cuadro de texto
        texto_cita = f'Nueva cita para el día {fecha_seleccionada.toString("dd-MM-yyyy")} por el usuario {self.usuario_logueado}\n'
        self.cuadro_texto.append(texto_cita)

        # Guardar los datos actualizados en el JSON
        self.guardarCitasEnJSON()

        QMessageBox.information(self, 'Cita Agendada',
                                f'Se ha agendado una nueva cita para el día: {fecha_seleccionada.toString("dd-MM-yyyy")} '
                                f'para el usuario: {self.usuario_logueado}')

    def setUsuarioLogueado(self, usuario):
        self.usuario_logueado = usuario

    def guardarCitasEnJSON(self):
        with open('Projecte_DI/datos/citas.json', 'w') as file:
            json.dump(self.citas_por_dia, file)

def main():
    app = QApplication(sys.argv)
    calendario_app = CalendarioApp()
    calendario_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
