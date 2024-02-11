import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import datetime

class Ofertas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate - Ofertas')
        self.setGeometry(250, 250, 650, 250)  # Fijar el tamaño de la ventana
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1E90FF; /* Cambiar el color de fondo a azul */
                color: #ffffff; /* Cambiar el color del texto a blanco */
            }
            QLabel {
                color: #ffffff; /* Cambiar el color del texto a blanco */
            }
            QPushButton {
                background-color: #ffffff; /* Color de fondo del botón */
                color: #1E90FF; /* Color del texto del botón */
                border: 2px solid #ffffff; /* Borde del botón */
                border-radius: 10px; /* Bordes redondeados */
                padding: 5px 10px; /* Espaciado interno del botón */
            }
            QPushButton:hover {
                background-color: #ffffff; /* Cambio de color al pasar el cursor sobre el botón */
                color: #1E90FF; /* Cambio de color del texto al pasar el cursor sobre el botón */
            }
            QProgressBar {
                color: #ffffff; /* Color del texto de la barra de progreso */
                background-color: #3d3d3d; /* Color de fondo de la barra de progreso */
                border: 2px solid #ffffff; /* Borde de la barra de progreso */
                border-radius: 5px; /* Bordes redondeados */
            }
            """
        )
        self.initUI()

    def initUI(self):
        # Crear un menú de barra
        menubar = self.menuBar()
        volver_menu = menubar.addMenu('Volver al Menú')

        # Acción para volver al menú principal
        volver_action = QAction('Volver', self)
        volver_action.triggered.connect(self.mostrarMenu)
        volver_menu.addAction(volver_action)

        # Crear un layout de cuadrícula para organizar las etiquetas y widgets
        layout = QGridLayout()

        # Título con imagen
        title_image_label = QLabel(self)
        title_pixmap = QPixmap("title_image.png")  # Agrega tu propia imagen aquí
        title_image_label.setPixmap(title_pixmap)
        title_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_image_label, 0, 0, 1, 2)

        # Título de las ofertas
        title_ofertas = QLabel("¡DESCUENTOS DE APERTURA!", self)
        title_ofertas.setAlignment(Qt.AlignCenter)
        title_ofertas.setStyleSheet("color: #ffffff; font-size: 24px;")
        layout.addWidget(title_ofertas, 1, 0, 1, 2)

        row = 2
        for oferta, disponible, descripcion, fecha_vencimiento, terminos_condiciones in self.ofertas_disponibilidad():
            # Texto de la oferta
            oferta_label = QLabel(oferta, self)
            oferta_label.setStyleSheet("color: #ffffff; font-size: 18px;")
            layout.addWidget(oferta_label, row, 0)

            # Descripción de la oferta
            descripcion_label = QLabel(descripcion, self)
            descripcion_label.setWordWrap(True)  # Permite que el texto se ajuste automáticamente
            descripcion_label.setStyleSheet("color: #ffffff;")
            layout.addWidget(descripcion_label, row, 1)

            # Barra de progreso para mostrar el tiempo restante (solo si la oferta está disponible)
            if disponible:
                progreso = self.calcular_progreso(fecha_vencimiento)
                progreso_bar = QProgressBar(self)
                progreso_bar.setValue(progreso)
                layout.addWidget(progreso_bar, row + 1, 0, 1, 2)
            else:
                # Si la oferta no está disponible, oculta la barra de progreso
                progreso_bar = QProgressBar(self)
                progreso_bar.setVisible(False)
                layout.addWidget(progreso_bar, row + 1, 0, 1, 2)

            # Términos y condiciones
            terminos_condiciones_label = QLabel(f"Términos y condiciones: {terminos_condiciones}", self)
            terminos_condiciones_label.setWordWrap(True)
            terminos_condiciones_label.setStyleSheet("color: #ffffff;")
            layout.addWidget(terminos_condiciones_label, row + 2, 0, 1, 2)

            # Botón "Aplicar Oferta"
            btn_aplicar = QPushButton("Aplicar Oferta", self)
            btn_aplicar.clicked.connect(lambda oferta=oferta: self.aplicarOferta())
            btn_aplicar.setEnabled(disponible)  # El botón solo está habilitado si la oferta está disponible
            layout.addWidget(btn_aplicar, row + 3, 0, 1, 2)

            row += 5  # Incrementar el índice de fila para agregar espacio entre las ofertas

        # Crear un widget contenedor y asignar el layout de cuadrícula
        container_widget = QWidget(self)
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

    def mostrarMenu(self):
        self.close()

    def aplicarOferta(self):
        print(f"Oferta aplicada")

    def ofertas_disponibilidad(self):
        # Lista de ofertas y disponibilidad
        return [
            ("20% en tu primera Revisión", True, "Ven y aprovecha este descuento especial en tu primera revisión.",
             "20/08/2024", "Aplicable a nuevas reservas hasta la fecha de vencimiento."),
            ("20% en tu primera vacunación", False, "Lo sentimos, esta oferta no está disponible en este momento.",
             "N/A", "Válido solo para usuarios premium."),
            ("15% por visitar la tienda más de 4 veces", True,
             "¡Obtén un 15% de descuento en cada visita después de tu cuarta vez!",
             "Indefinido", "Aplicable a todas las visitas después de la cuarta."),
            ("10% en tu primera cita online", True, "Ahorra tiempo y dinero reservando tu cita online con nosotros.",
             "10/04/2024", "Válido solo para nuevas reservas en línea.")
        ]

    def calcular_progreso(self, fecha_vencimiento):
        if fecha_vencimiento == 'Indefinido':
            return 0  
        else:
            fecha_vencimiento_obj = datetime.strptime(fecha_vencimiento, '%d/%m/%Y')
            fecha_actual = datetime.now()
            tiempo_restante = fecha_vencimiento_obj - fecha_actual
            tiempo_total = fecha_vencimiento_obj - fecha_vencimiento_obj.replace(month=1, day=1)
            progreso = int((tiempo_total - tiempo_restante).total_seconds() / tiempo_total.total_seconds() * 100)
            return max(0, min(progreso, 100))

def main():
    app = QApplication(sys.argv)
    ofertas = Ofertas()
    ofertas.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
