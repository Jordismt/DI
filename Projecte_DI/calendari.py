import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class CalendarioApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendario en PyQt")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Agregar el widget de calendario
        self.calendario = QCalendarWidget()
        self.calendario.setFixedSize(250, 150)  # Establecer un tamaño fijo para el calendario
        self.layout.addWidget(self.calendario)
        #Añadirlo al centro
        self.layout.addWidget(self.calendario, alignment=Qt.AlignHCenter)

        # Agregar un botón para solicitar una cita
        self.button_pedir_cita = QPushButton('Pedir Cita', self)
        self.layout.addWidget(self.button_pedir_cita)

        #Añadir espai en blanc baix per a centrar el calendari dalt
        self.layout.addStretch()

        # Conectar la señal selectionChanged del calendario a la función de verificación de citas
        self.calendario.selectionChanged.connect(self.verificarCitas)

        # Inicializar el contador de citas por día
        self.citas_por_dia = {}

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

        QMessageBox.information(self, 'Cita Agendada', 'Se ha agendado una nueva cita para el día: {}'.format(fecha_seleccionada.toString("dd-MM-yyyy")))
        