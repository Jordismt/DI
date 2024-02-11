import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class Mascota:
    def __init__(self, nombre, edad, especie, imagen):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.imagen = imagen


class VentanaAdopcion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Adopción de Mascotas')
        self.setGeometry(100, 100, 800, 600)

        # Fondo de la ventana
        self.setStyleSheet("background-color: #2c3e50;")

        # Lista de mascotas
        self.lista_mascotas = QListWidget()
        self.lista_mascotas.setStyleSheet("background-color: rgba(255, 255, 255, 0.7); border-radius: 10px;")
        self.lista_mascotas.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lista_mascotas.itemClicked.connect(self.mostrar_detalle_mascota)

        # Botones
        buscar_button = QPushButton('Buscar')
        buscar_button.setStyleSheet("background-color: #2980b9; color: white; padding: 10px; border-radius: 10px;")
        buscar_button.clicked.connect(self.buscar_mascotas)
        adoptar_button = QPushButton('Adoptar')
        adoptar_button.setStyleSheet("background-color: #c0392b; color: white; padding: 10px; border-radius: 10px;")
        adoptar_button.clicked.connect(self.adoptar_mascotas)
        agregar_button = QPushButton('Agregar')
        agregar_button.setStyleSheet("background-color: #16a085; color: white; padding: 10px; border-radius: 10px;")
        agregar_button.clicked.connect(self.agregar_mascota)
        eliminar_button = QPushButton('Eliminar')
        eliminar_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px; border-radius: 10px;")
        eliminar_button.clicked.connect(self.eliminar_mascotas)
        limpiar_button = QPushButton('Limpiar')
        limpiar_button.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px; border-radius: 10px;")
        limpiar_button.clicked.connect(self.limpiar_campos)

        # Campos de búsqueda avanzada
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")
        self.especie_input = QLineEdit()
        self.especie_input.setPlaceholderText("Especie")
        self.edad_input = QLineEdit()
        self.edad_input.setPlaceholderText("Edad")

        # Diseño de la ventana
        layout = QVBoxLayout()
        header_label = QLabel('<h1 style="color: white; text-align: center;">Adopción de Mascotas</h1>')
        layout.addWidget(header_label)
        layout.addWidget(self.lista_mascotas)
        
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.nombre_input)
        filter_layout.addWidget(self.especie_input)
        filter_layout.addWidget(self.edad_input)
        filter_layout.addWidget(buscar_button)
        layout.addLayout(filter_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(agregar_button)
        button_layout.addWidget(eliminar_button)
        button_layout.addWidget(limpiar_button)
        button_layout.addWidget(adoptar_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Cargar mascotas
        self.cargar_mascotas()

    def cargar_mascotas(self):
        # Simulación de datos de mascotas disponibles para adopción
        mascotas_disponibles = [
            Mascota("Luna", "2 años", "Perro", "Projecte_DI/images/perro_luna.jpg"),
            Mascota("Simba", "5 meses", "Gato", "Projecte_DI/images/gato_simba.jpg"),
            Mascota("Rocky", "3 años", "Perro", "Projecte_DI/images/perro_rocky.jpg"),
            Mascota("Pepe", "5 años", "Ave", "Projecte_DI/images/ave.jpg"),
            Mascota("Pepito", "2 años", "Conejo", "Projecte_DI/images/conejo.jpg"),
            Mascota("Gustavo", "3 meses", "Ave", "Projecte_DI/images/agaporni.jpg"),
        ]

        # Agregar las mascotas a la lista
        for mascota in mascotas_disponibles:
            item = QListWidgetItem(mascota.nombre)
            self.lista_mascotas.addItem(item)
            item.setData(Qt.UserRole, mascota)

    def mostrar_detalle_mascota(self, item):
        mascota = item.data(Qt.UserRole)
        mensaje = f"<h2 style='color: white;'>Detalles de {mascota.nombre}</h2>"
        mensaje += f"<b style='color: white;'>Edad:</b> {mascota.edad}<br>"
        mensaje += f"<b style='color: white;'>Especie:</b> {mascota.especie}<br>"
        mensaje += f'<img src="{mascota.imagen}" width="200" height="200">'
        QMessageBox.information(self, "Detalles de Mascota", mensaje)

    def buscar_mascotas(self):
        # Implementa la funcionalidad de búsqueda de mascotas por nombre, especie, edad, etc.
        nombre = self.nombre_input.text().strip()
        especie = self.especie_input.text().strip()
        edad = self.edad_input.text().strip()
        for i in range(self.lista_mascotas.count()):
            item = self.lista_mascotas.item(i)
            mascota = item.data(Qt.UserRole)
            if nombre.lower() in mascota.nombre.lower() and especie.lower() in mascota.especie.lower() and edad.lower() in mascota.edad.lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def adoptar_mascotas(self):
        # Implementa la funcionalidad para adoptar las mascotas seleccionadas.
        mascotas_seleccionadas = self.lista_mascotas.selectedItems()
        if mascotas_seleccionadas:
            nombres_mascotas = [item.text() for item in mascotas_seleccionadas]
            QMessageBox.information(self, 'Adoptar Mascotas', f'Se han adoptado a {", ".join(nombres_mascotas)} correctamente.')
            for item in mascotas_seleccionadas:
                self.lista_mascotas.takeItem(self.lista_mascotas.row(item))
        else:
            QMessageBox.warning(self, 'Adoptar Mascotas', 'Por favor, seleccione al menos una mascota para adoptar.')

    def agregar_mascota(self):
        # Implementa la funcionalidad para agregar una nueva mascota.
        nombre, ok = QInputDialog.getText(self, 'Agregar Mascota', 'Ingrese el nombre de la nueva mascota:')
        if ok and nombre:
            edad, ok = QInputDialog.getText(self, 'Agregar Mascota', 'Ingrese la edad de la nueva mascota:')
            if ok and edad:
                especie, ok = QInputDialog.getText(self, 'Agregar Mascota', 'Ingrese la especie de la nueva mascota:')
                if ok and especie:
                    imagen, ok = QInputDialog.getText(self, 'Agregar Mascota', 'Ingrese la URL de la imagen de la nueva mascota:')
                    if ok and imagen:
                        nueva_mascota = Mascota(nombre, edad, especie, imagen)
                        item = QListWidgetItem(nombre)
                        self.lista_mascotas.addItem(item)
                        item.setData(Qt.UserRole, nueva_mascota)

    def eliminar_mascotas(self):
        # Implementa la funcionalidad para eliminar las mascotas seleccionadas.
        mascotas_seleccionadas = self.lista_mascotas.selectedItems()
        if mascotas_seleccionadas:
            for item in mascotas_seleccionadas:
                self.lista_mascotas.takeItem(self.lista_mascotas.row(item))
        else:
            QMessageBox.warning(self, 'Eliminar Mascotas', 'Por favor, seleccione al menos una mascota para eliminar.')

    def limpiar_campos(self):
        # Implementa la funcionalidad para limpiar los campos de búsqueda.
        self.nombre_input.clear()
        self.especie_input.clear()
        self.edad_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_adopcion = VentanaAdopcion()
    ventana_adopcion.show()
    sys.exit(app.exec())
