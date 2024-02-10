import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from datetime import datetime

class OpinionWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Opiniones de la Tienda y la App')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #3465A4; color: white;")

        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Texto de ejemplo con algunas opiniones predefinidas
        opiniones = [
            {"nombre": "María", "fecha": "2024-02-10", "contenido": "Excelente tienda, siempre encuentro lo que necesito para mis mascotas.", "sobre": "Variedad de productos"},
            {"nombre": "Juan", "fecha": "2024-02-11", "contenido": "La aplicación es muy fácil de usar y el proceso de compra es rápido.", "sobre": "Funcionalidad de la aplicación"},
            {"nombre": "Laura", "fecha": "2024-02-12", "contenido": "Buena variedad de productos y precios competitivos.", "sobre": "Precios y variedad"},
            {"nombre": "Pepe", "fecha": "2024-04-08", "contenido": "Productos de buena calidad y precios razonables", "sobre": "Productos Tienda"},
            {"nombre": "Jordi", "fecha": "2024-09-08", "contenido": "Buena variedad de productos y precios competitivos.", "sobre": "Precios y variedad"},
            {"nombre": "Juan", "fecha": "2024-10-09", "contenido": "Buena variedad de productos y precios competitivos.", "sobre": "Precios y variedad"}
        ]
        
        # Widget para contener las opiniones
        opiniones_container = QVBoxLayout()
        
        # Agregar cada opinión en un cuadro separado
        for opinion in opiniones:
            frame = QFrame()
            frame.setStyleSheet("background-color: #204A87; border: 1px solid #3465A4; border-radius: 5px;")
            frame_layout = QVBoxLayout(frame)
            
            # Detalles de la opinión
            fecha_formateada = datetime.strptime(opinion['fecha'], "%Y-%m-%d").strftime("%d/%m/%Y")
            label_nombre_fecha = QLabel(f"<b>{opinion['nombre']}</b> ({fecha_formateada})")
            label_nombre_fecha.setStyleSheet("color: white;")
            label_sobre = QLabel(f"<i>{opinion['sobre']}</i>:")
            label_sobre.setStyleSheet("color: white;")
            label_contenido = QLabel(opinion['contenido'])
            label_contenido.setStyleSheet("color: white;")
            
            # Añadir widgets al diseño del cuadro
            frame_layout.addWidget(label_nombre_fecha)
            frame_layout.addWidget(label_sobre)
            frame_layout.addWidget(label_contenido)
            
            # Añadir el cuadro al contenedor de opiniones
            opiniones_container.addWidget(frame)
        
        # Widget para desplazar las opiniones
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(QWidget())
        scroll_area.widget().setLayout(opiniones_container)
        
        # Cuadro de texto para la opinión personalizada
        self.text_edit_personalizada = QTextEdit()
        
        # Botón para enviar la opinión personalizada
        self.btn_enviar_opinion = QPushButton('Enviar Opinión Personalizada')
        self.btn_enviar_opinion.setStyleSheet("background-color: #204A87; color: white; border: 1px solid #3465A4; border-radius: 5px;")
        self.btn_enviar_opinion.clicked.connect(self.enviarOpinionPersonalizada)
        
        # Botón para cerrar la ventana
        self.btn_cerrar = QPushButton('Cerrar')
        self.btn_cerrar.setStyleSheet("background-color: #204A87; color: white; border: 1px solid #3465A4; border-radius: 5px;")
        self.btn_cerrar.clicked.connect(self.close)
        
        # Agregar widgets al diseño principal
        layout.addWidget(QLabel("<h2>Opiniones de los Clientes:</h2>"))
        layout.addWidget(scroll_area)
        layout.addWidget(QLabel("<h2>Añadir Opinión Personalizada:</h2>"))
        layout.addWidget(self.text_edit_personalizada)
        layout.addWidget(self.btn_enviar_opinion)
        layout.addWidget(self.btn_cerrar)

    def enviarOpinionPersonalizada(self):
        opinion_personalizada = self.text_edit_personalizada.toPlainText()
        if opinion_personalizada:
            # Agregar la opinión personalizada al contenedor de opiniones
            frame = QFrame()
            frame.setStyleSheet("background-color: #204A87; border: 1px solid #3465A4; border-radius: 5px;")
            frame_layout = QVBoxLayout(frame)
            
            # Detalles de la opinión personalizada (nombre y fecha actuales)
            nombre = "Usuario"
            fecha_actual = datetime.now().strftime("%d/%m/%Y")
            label_nombre_fecha = QLabel(f"<b>{nombre}</b> ({fecha_actual})")
            label_nombre_fecha.setStyleSheet("color: white;")
            label_contenido = QLabel(opinion_personalizada)
            label_contenido.setStyleSheet("color: white;")
            
            # Añadir widgets al diseño del cuadro
            frame_layout.addWidget(label_nombre_fecha)
            frame_layout.addWidget(label_contenido)
            
            # Añadir el cuadro al contenedor de opiniones
            scroll_area = self.findChild(QScrollArea)
            opiniones_container = scroll_area.widget().layout()
            opiniones_container.addWidget(frame)
        else:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, ingrese una opinión personalizada.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = OpinionWindow()
    ventana.show()
    sys.exit(app.exec())
