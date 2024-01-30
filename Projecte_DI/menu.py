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
        

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate')
        self.setGeometry(250, 250, 550, 850)

        # Añadir estilos CSS a la aplicación
        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: white;
                color: #336699;
            }

            QMenuBar {
                background-color: #f0f0f0;
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
            '''
        )
        self.initUI()

    def initUI(self):
        exit_action = QAction('Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # Menú para el icono del menú desplegable
        popup_menu = QMenu(self)
        popup_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; ')

        popup_menu.addAction(exit_action)
        popup_menu.addSeparator()

        # Crear 5 opciones para probar
        for i in range(5):
            action = QAction(f'Opción {i+1}', self)
            popup_menu.addAction(action)

        popup_menu.aboutToShow.connect(lambda: self.adjustMenuHeight(popup_menu))

        # Icono del menú desplegable
        icon_path_menu = "Projecte_DI/images/icono_menu.png"
        menu_icon = QIcon(icon_path_menu)
        menu_action = menubar.addAction(menu_icon, '')
        menu_action.setMenu(popup_menu)

        # Menú para el icono del perfil
        profile_menu = QMenu(self)
        profile_menu.setStyleSheet('background-color: #336699; color: white; border: 3px solid #336699; ')


        profile_action = QAction(self)
        profile_action.setIcon(QIcon("Projecte_DI/images/perfil.jpg"))
        profile_action.setText('Perfil')
        profile_menu.addAction(profile_action)

        menubar.addMenu(profile_menu)

        self.adjustMenuHeight(popup_menu)  # Ajustar la altura del menú desplegable
        # Agregar el calendario directamente al QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        calendario_widget = CalendarioApp()
        self.stacked_widget.addWidget(calendario_widget)
        self.setCentralWidget(self.stacked_widget)

        # Mostrar directamente el calendario
        self.stacked_widget.setCurrentIndex(0)


    def adjustMenuHeight(self, menu):
        # Ajustar el menú para que se acople a la ventana
        menu_height = self.height() - self.menuBar().height() - 2
        menu.setFixedHeight(menu_height)

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
