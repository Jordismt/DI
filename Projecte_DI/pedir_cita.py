import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from calendari import CalendarioApp


class PedirCita(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate')
        self.setGeometry(250, 250, 550, 850)
        self.setStyleSheet("background-color: rgb(70, 130, 180);")

        self.initUI()
    
    def initUI(self):
        


        # Agregar el calendario directamente al QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        calendario_widget = CalendarioApp()

        # Añadir un cuadro de texto para mostrar las citas
        self.cuadro_texto = QTextEdit(self)
        self.cuadro_texto.setReadOnly(True)

        # Añadir el calendario y el cuadro de texto al diseño
        layout = QVBoxLayout()
        layout.addWidget(calendario_widget)
        layout.addWidget(self.cuadro_texto)

        # Crear un widget contenedor y asignar el diseño
        container_widget = QWidget(self)
        container_widget.setLayout(layout)

        self.stacked_widget.addWidget(container_widget)
        self.setCentralWidget(self.stacked_widget)

        # Mostrar directamente el calendario
        self.stacked_widget.setCurrentIndex(0)

        # Conectar la señal de la cita al método para mostrarla en el cuadro de texto
        calendario_widget.cita_agendada.connect(self.mostrarCita)

        # Agregar botón para volver al menú
        self.btn_volver_menu = QPushButton('Volver al Menú', self)
        self.btn_volver_menu.clicked.connect(self.mostrarMenu)
        layout.addWidget(self.btn_volver_menu, alignment=Qt.AlignTop | Qt.AlignLeft)

    def mostrarCita(self, fecha, usuario):
        # Agregar la cita al cuadro de texto
        texto_cita = f'Cita agendada para el día {fecha.toString("dd-MM-yyyy")} por el usuario {usuario}\n'
        self.cuadro_texto.append(texto_cita)

    def mostrarMenu(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    pedir_cita = PedirCita()
    pedir_cita.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
