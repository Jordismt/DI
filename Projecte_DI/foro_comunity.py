import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class CommunityForum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Foro de Comunidad - HealtMate')
        self.setGeometry(250, 250, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Etiqueta de bienvenida
        welcome_label = QLabel("Bienvenido al Foro de Comunidad - HealtMate", self)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white; margin-bottom: 20px;")
        layout.addWidget(welcome_label)

        # Área de texto para mostrar publicaciones
        self.posts_textedit = QTextEdit(self)
        self.posts_textedit.setReadOnly(True)  # Hacer el texto solo de lectura
        self.posts_textedit.setStyleSheet("font-size: 14px; color: white; background-color: #1E2A3A;")
        layout.addWidget(self.posts_textedit)

        # Botón para crear una nueva publicación
        new_post_button = QPushButton("Nueva Publicación", self)
        new_post_button.clicked.connect(self.chooseCategory)
        new_post_button.setStyleSheet("background-color: #1E2A3A; color: #009688; font-weight: bold; padding: 10px; border: 2px solid #009688;")
        layout.addWidget(new_post_button)

        # Widget principal
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def chooseCategory(self):
        # Método para abrir un cuadro de diálogo y permitir al usuario elegir una categoría para la nueva publicación
        category_dialog = QInputDialog()
        category_dialog.setOption(QInputDialog.UseListViewForComboBoxItems)  # Utilizar una lista desplegable para mostrar las categorías
        categories = ["Cuidado General", "Nutrición", "Comportamiento", "Salud Preventiva", "Emergencias"]
        category_dialog.setComboBoxItems(categories)  # Establecer las opciones de categoría en el cuadro de diálogo
        category_dialog.setWindowTitle("Seleccione una categoría")  # Establecer el título del cuadro de diálogo
        category_dialog.setLabelText("Seleccione la categoría para su publicación:")  # Establecer la etiqueta del cuadro de diálogo
        category_dialog.setOkButtonText("Aceptar") 
        category_dialog.setCancelButtonText("Cancelar") 
        if category_dialog.exec():  # Ejecutar el cuadro de diálogo y verificar si se aceptó una selección
            selected_category = category_dialog.textValue()  # Obtener la categoría seleccionada por el usuario
            if selected_category:  # Verificar si se seleccionó una categoría
                self.createNewPost(selected_category)  # Llamar al método para crear una nueva publicación con la categoría seleccionada

    def createNewPost(self, category):
        # Método para crear una nueva publicación en la categoría seleccionada por el usuario
        title, ok = QInputDialog.getText(self, 'Nueva Publicación', 'Título de la publicación:')  # Solicitar al usuario que ingrese el título de la publicación
        if ok and title.strip():  # Verificar que el título no esté vacío y que el usuario haya presionado el botón de aceptar
            content, ok = QInputDialog.getMultiLineText(self, 'Nueva Publicación', 'Contenido de la publicación:')  # Solicitar al usuario que ingrese el contenido de la publicación
            if ok and content.strip():  # Verificar que el contenido no esté vacío y que el usuario haya presionado el botón de aceptar
                self.fadeInNewPost(category, title, content)  # Llamar al método para agregar la nueva publicación con efecto de desvanecimiento
            else:
                QMessageBox.warning(self, "Advertencia", "El contenido de la publicación no puede estar vacío.")  # Mostrar un mensaje de advertencia si el contenido está vacío
        else:
            QMessageBox.warning(self, "Advertencia", "El título de la publicación no puede estar vacío.")  # Mostrar un mensaje de advertencia si el título está vacío

    def fadeInNewPost(self, category, title, content):
        # Construir el texto de la publicación con formato HTML
        post_text = f"<b>Categoría:</b> {category}<br><b>Título:</b> {title}<br><b>Contenido:</b><br>{content}"
        
        # Agregar el texto de la publicación al área de texto
        self.posts_textedit.append(post_text)
        
        # Desplazar el área de texto hacia abajo para mostrar la nueva publicación
        self.posts_textedit.verticalScrollBar().setValue(self.posts_textedit.verticalScrollBar().maximum())
        
        # Repintar el área de texto para asegurarse de que se muestre la nueva publicación
        self.posts_textedit.repaint()
        
        # Agregar un efecto de opacidad al área de texto para el efecto de desvanecimiento
        self.posts_textedit.setGraphicsEffect(QGraphicsOpacityEffect(self))
        
        # Crear una animación de propiedad para cambiar la opacidad del efecto gráfico
        self.fade_animation = QPropertyAnimation(self.graphicsEffect(), b"opacity", self)
        
        # Establecer la duración de la animación en milisegundos
        self.fade_animation.setDuration(2000)  # Duración de la animación en milisegundos (2 segundos)
        
        # Definir el valor inicial de la opacidad como completamente opaco (1.0)
        self.fade_animation.setStartValue(1.0)
        
        # Definir el valor final de la opacidad como completamente transparente (0.0)
        self.fade_animation.setEndValue(0.0)
        
        # Conectar la señal 'finished' de la animación para eliminar el efecto de opacidad al finalizar la animación
        self.fade_animation.finished.connect(lambda: self.posts_textedit.setGraphicsEffect(None))
        
        # Iniciar la animación y especificar que se elimine automáticamente una vez que termine
        self.fade_animation.start(QAbstractAnimation.DeleteWhenStopped)

def main():
    app = QApplication(sys.argv)
    forum = CommunityForum()
    forum.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
