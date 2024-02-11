from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class VentanaCrearCuenta(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Crear Compte')
        self.setFixedSize(400, 200)  
        self.setStyleSheet(
            '''
            QDialog {
                background-color: #f0f0f0; /* Canviar el color de fons */
            }
            QLabel {
                font-size: 14px;  /* Mida del text */
                color: black; /* Color del text */
            }
            QLineEdit {
                padding: 5px; /* Espaiat intern */
                border: 1px solid #cccccc; /* Vora */
                border-radius: 5px; /* Vora arrodonida */
                background-color: #ffffff; /* Fons blanc */
                color: black; /* Color del text */
            }
            QPushButton {
                background-color: #007bff; /* Color de fons */
                color: #ffffff; /* Color del text */
                border: none; /* Sense vora */
                padding: 8px 16px; /* Espaiat intern */
                border-radius: 5px; /* Vora arrodonida */
            }
            QPushButton:hover {
                background-color: #0056b3; /* Canvi de color al passar el cursor */
            }
            '''
        )
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()


        compte_layout = QFormLayout()
        usuari_label = QLabel('Nombre de usuario:')
        self.usuari_input = QLineEdit()
        compte_layout.addRow(usuari_label, self.usuari_input)
        contrasenya_label = QLabel('Contraseña:')
        self.contrasenya_input = QLineEdit()
        self.contrasenya_input.setEchoMode(QLineEdit.Password)  # Ocultar la contrasenya
        compte_layout.addRow(contrasenya_label, self.contrasenya_input)
        confirmar_contrasenya_label = QLabel('Confirmar Contraseña:')
        self.confirmar_contrasenya_input = QLineEdit()
        self.confirmar_contrasenya_input.setEchoMode(QLineEdit.Password)  # Ocultar la contrasenya
        compte_layout.addRow(confirmar_contrasenya_label, self.confirmar_contrasenya_input)


        button_layout = QHBoxLayout()
        crear_compte_button = QPushButton('Crear Cuenta')
        crear_compte_button.clicked.connect(self.crearCompte)
        cancelar_button = QPushButton('Cancelar')
        cancelar_button.clicked.connect(self.close)
        button_layout.addWidget(crear_compte_button)
        button_layout.addWidget(cancelar_button)

        main_layout.addLayout(compte_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def crearCompte(self):
        # Verificar que els camps no estiguen buits
        nom_usuari = self.usuari_input.text().strip()
        contrasenya = self.contrasenya_input.text().strip()
        confirmar_contrasenya = self.confirmar_contrasenya_input.text().strip()

        if not nom_usuari or not contrasenya or not confirmar_contrasenya:
            QMessageBox.warning(self, 'Error', 'Por favor, complete todos los campos.')
            return

        if contrasenya != confirmar_contrasenya:
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden.')
            return


        QMessageBox.information(self, 'Exito', 'La cuenta se ha creado con exito!')
        self.close()
