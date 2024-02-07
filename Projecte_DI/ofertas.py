import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class Ofertas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Ofertas')
        self.setFixedSize(550, 400)  # Fijar el tamaño de la ventana
        self.setStyleSheet("background-color: rgb(70, 130, 180);")
        self.initUI()

    def initUI(self):
        # Crear un menú de barra
        menubar = self.menuBar()
        volver_menu = menubar.addMenu('Volver al Menú')

        # Acción para volver al menú principal
        volver_action = QAction('Volver', self)
        volver_action.triggered.connect(self.mostrarMenu)
        volver_menu.addAction(volver_action)

        # Crear un layout vertical para organizar las etiquetas y widgets
        layout = QVBoxLayout()

        # Título con imagen
        title_widget = QWidget()
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 20, 0, 20)

        title_image_label = QLabel(self)
        title_pixmap = QPixmap("title_image.png")  # Agrega tu propia imagen aquí
        title_image_label.setPixmap(title_pixmap)
        title_image_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title_image_label)
        title_widget.setLayout(title_layout)
        layout.addWidget(title_widget)

        # Ofertas
        font_title = QFont()
        font_title.setPointSize(24)

        title_ofertas = QLabel("¡DESCUENTOS DE APERTURA!", self)
        title_ofertas.setAlignment(Qt.AlignCenter)
        title_ofertas.setFont(font_title)
        title_ofertas.setStyleSheet("color: white;")
        layout.addWidget(title_ofertas)

        # Lista de ofertas y disponibilidad
        ofertas_disponibilidad = [
            ("20% en tu primera Revisión", True),
            ("20% en tu primera vacunación", False),
            ("15% por visitar la tienda más de 4 veces", True),
            ("10% en tu primera cita online", True)
        ]

        # Crear un widget contenedor para las ofertas
        offers_widget = QWidget()
        offers_layout = QVBoxLayout()

        font_offer = QFont()
        font_offer.setPointSize(18)

        for oferta, disponible in ofertas_disponibilidad:
            oferta_layout = QHBoxLayout()
            #oferta_layout.setContentsMargins(20, 0, 20, 0)

            # Texto de la oferta y su disponibilidad
            oferta_label = QLabel(oferta)
            oferta_label.setFont(font_offer)
            oferta_layout.addWidget(oferta_label)
            
            # Texto de disponibilidad
            disponible_label = QLabel("Disponible" if disponible else "No Disponible")
            disponible_label.setFont(QFont("Arial", 10))  # Cambiar el tamaño de la fuente
            oferta_layout.addWidget(disponible_label)

            # Botón "Aplicar Oferta"
            btn_aplicar = QPushButton("Aplicar Oferta")
            btn_aplicar.clicked.connect(self.aplicarOferta)
            oferta_layout.addWidget(btn_aplicar)

            offers_layout.addLayout(oferta_layout)

        # Agregar el layout de las ofertas al widget contenedor
        offers_widget.setLayout(offers_layout)
        layout.addWidget(offers_widget)

        # Agregar un espacio en blanco elástico al final
        layout.addStretch()

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrarMenu(self):
        # Implementa la lógica para mostrar el menú principal aquí
        print("Mostrar menú principal")
        self.close()

    def aplicarOferta(self):
        # Implementa la lógica para aplicar la oferta aquí
        print("Oferta aplicada")


def main():
    app = QApplication(sys.argv)
    ofertas = Ofertas()
    ofertas.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
