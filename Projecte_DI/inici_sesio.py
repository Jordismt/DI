import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import json
from menu import *
from inici import *
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


class Inici_Sesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealtMate: Iniciar sesión/Registrarse')
        self.setGeometry(250, 250, 650, 250)
        self.setStyleSheet(
            "background-color: rgb(70, 130, 180); font-size: 14px; font-family: Arial; color: #333333;"
        )
        self.users = self.load_users()  # Cargar usuarios desde el archivo JSON
        self.initUI()


    def initUI(self):
        self.label_username = QLabel('Usuario:', self)
        self.label_password = QLabel('Contraseña:', self)

        self.input_username = QLineEdit(self)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_toggle_password = QPushButton(self)
        self.btn_toggle_password.setIcon(QIcon("Projecte_DI/images/show_password_icon.png"))
        self.btn_toggle_password.setCheckable(True)
        self.btn_toggle_password.toggled.connect(self.toggle_password_visibility)

        self.btn_google = QPushButton(self)
        self.btn_google.setIcon(QIcon("Projecte_DI/images/google.png"))
        self.btn_google.clicked.connect(self.google_login)

        self.btn_login = QPushButton('Iniciar Sesión', self)
        self.btn_login.clicked.connect(self.login)

        self.btn_register = QPushButton('Registrarse', self)
        self.btn_register.clicked.connect(self.register)

        # Botón para volver atrás
        self.btn_back = QPushButton('Volver atrás', self)
        self.btn_back.clicked.connect(self.go_back)

        layout = QFormLayout()
        layout.addRow(self.label_username, self.input_username)
        layout.addRow(self.label_password, self.create_password_layout())
        layout.addRow(self.btn_login)
        layout.addRow(self.btn_register)
        layout.addRow(self.btn_google)
        layout.addRow(self.btn_back)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def create_password_layout(self):
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.input_password)
        password_layout.addWidget(self.btn_toggle_password)
        password_layout.setAlignment(Qt.AlignCenter)
        return password_layout

    def toggle_password_visibility(self, checked):
        if checked:
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    def load_users(self):
        try:
            with open('Projecte_DI/datos/usuarios.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open('Projecte_DI/datos/usuarios.json', 'w') as file:
            json.dump(self.users, file)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username in self.users and self.users[username] == password:
            QMessageBox.information(self, 'Inicio de Sesión', 'Inicio de Sesión Exitoso')
            self.close()
            self.open_menu()
        else:
            QMessageBox.warning(self, 'Inicio de Sesión', 'Usuario o Contraseña Incorrectos')

    def register(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == '' or password == '':
            QMessageBox.warning(self, 'Registro', 'Por favor, ingrese un usuario y una contraseña válidos')
            return

        if username in self.users:
            QMessageBox.warning(self, 'Registro', 'El usuario ya existe')
        else:
            self.users[username] = password
            self.save_users()
            QMessageBox.information(self, 'Registro', 'Registro Exitoso')

    def addUsuarioInvitado(self):
        username_invitado = "Invitado"
        password_invitado = "invitado"  # Puedes establecer cualquier contraseña para el invitado

        # Añadir el usuario invitado al diccionario de usuarios
        self.users[username_invitado] = {"password": password_invitado}

        # Guardar el diccionario actualizado en el archivo JSON
        self.save_users()

    def google_login(self):
        # Fer duncio per iniciar secio en google
        pass

    def go_back(self):
        self.close()
        self.input_username.clear()
        self.input_password.clear()


    def open_menu(self):
        self.close()
        menu = Menu()
        menu.show()

def main():
    app = QApplication(sys.argv)
    login_window = Inici_Sesion()
    login_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()