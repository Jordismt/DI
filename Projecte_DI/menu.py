import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pedir_cita import PedirCita

from calendari import CalendarioApp

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate')
        self.setGeometry(250, 250, 550, 850)
        self.pedir_cita=PedirCita()

        # Añadir estils CSS a la aplicació
        self.setStyleSheet(
            '''
            QMainWindow {
                background-color: rgb(70, 130, 180);
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

        # Crear tres opciones para abrir diferentes ventanas
        action_pedir_cita = QAction('Pedir Cita', self)
        action_opcion2 = QAction('Opción 2', self)
        action_opcion3 = QAction('Opción 3', self)

        # Conectar cada acción con su respectiva función al hacer clic
        action_pedir_cita.triggered.connect(self.abrirVentanaPedirCita)
        action_opcion2.triggered.connect(self.abrirVentanaOpcion2)
        action_opcion3.triggered.connect(self.abrirVentanaOpcion3)

        # Agregar las acciones al menú
        popup_menu.addAction(action_pedir_cita)
        popup_menu.addAction(action_opcion2)
        popup_menu.addAction(action_opcion3)
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
    


    def abrirVentanaPedirCita(self):
        print("Abriendo ventana de pedir cita")
        try:
           
            self.pedir_cita.show()
            

        except Exception as e:
            print(f"Error al abrir la ventana de pedir cita: {e}")


    def abrirVentanaOpcion2(self):
        # Implementa la lógica para abrir la ventana de la opción 2
        print("Abrir ventana de la opción 2")

    def abrirVentanaOpcion3(self):
        # Implementa la lógica para abrir la ventana de la opción 3
        print("Abrir ventana de la opción 3")

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
