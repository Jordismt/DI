import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import json
from menu import *


class Inici_Sesion(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Iniciar sesión/Registrarse')
        self.setGeometry(250, 250, 650, 250)
        self.setStyleSheet(
            '''
            background-color: rgb(70, 130, 180); 
            font-size: 14px; 
            font-family: Arial; 
            color: white;
            '''
        )
        self.users = self.load_users()  # Cargar usuarios desde el archivo JSON
        self.initUI()


    def initUI(self):
        botones_layout = QHBoxLayout()

        self.label_username = QLabel('Usuario:', self)
        self.label_username.setStyleSheet("color: white;")
        self.label_password = QLabel('Contraseña:', self)
        self.label_password.setStyleSheet("color: white;")

        self.input_username = QLineEdit(self)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_toggle_password = QPushButton(self)
        self.btn_toggle_password.setIcon(QIcon("Projecte_DI/images/show_password_icon.png"))
        self.btn_toggle_password.setCheckable(True)
        self.btn_toggle_password.toggled.connect(self.toggle_password_visibility)

        # Crear QLabel para la imagen de Google
        self.google_image_label = QLabel(self)
        pixmap = QPixmap("Projecte_DI/images/google.png")
        self.google_image_label.setPixmap(pixmap.scaledToWidth(50))  # Ajustar el tamaño de la imagen
        self.google_image_label.setAlignment(Qt.AlignCenter)
        self.google_image_label.mousePressEvent = self.show_coming_soon_popup  # Conectar evento de clic

        self.btn_login = QPushButton('Iniciar Sesión', self)
        self.btn_login.setStyleSheet("background-color: white; color: rgb(70, 130, 180); font-size: 14px;")
        self.btn_login.clicked.connect(self.login)

        self.btn_register = QPushButton('Registrarse', self)
        self.btn_register.setStyleSheet("background-color: white; color: rgb(70, 130, 180); font-size: 14px;")
        self.btn_register.clicked.connect(self.register)

        botones_layout.addWidget(self.btn_login)
        botones_layout.addWidget(self.btn_register)

        # Botón para volver atrás
        self.btn_back = QPushButton('Volver atrás', self)
        self.btn_back.setStyleSheet("background-color: white; color: rgb(70, 130, 180); font-size: 14px;")
        self.btn_back.clicked.connect(self.go_back)

        layout = QFormLayout()
        layout.addRow(self.label_username, self.input_username)
        layout.addRow(self.label_password, self.create_password_layout())
        layout.addRow(botones_layout)
        layout.addRow(self.google_image_label)  # Agregar la QLabel con la imagen de Google
        layout.addRow(self.btn_back)
        layout.setSpacing(20)
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
            # Guardar el nombre de usuario en un archivo aparte
            with open('Projecte_DI/datos/temp_username.txt', 'w') as file:
                file.write(username)
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
        password_invitado = "invitado"  

        # Añadir el usuario invitado al diccionario de usuarios
        self.users[username_invitado] = {"password": password_invitado}

        # Guardar el diccionario actualizado en el archivo JSON
        self.save_users()

    def show_coming_soon_popup(self, event):
        QMessageBox.information(self, 'Próximamente', 'Disponible próximamente')

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
