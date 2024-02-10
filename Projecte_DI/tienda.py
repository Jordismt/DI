import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class TiendaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tienda de Productos Veterinarios')
        self.setGeometry(100, 100, 800, 600)

        # Inicializar lista de productos y carrito
        self.productos = [
            {"nombre": "Collar para Perro", "precio": 15.99, "imagen": "Projecte_DI/images/collar_perro.jpg"},
            {"nombre": "Correa para Perro", "precio": 12.50, "imagen": "Projecte_DI/images/correa_perro.jpg"},
            {"nombre": "Comedero para Gato", "precio": 9.75, "imagen": "Projecte_DI/images/comedero_gato.jpg"},
            {"nombre": "Juguete para Gato", "precio": 7.99, "imagen": "Projecte_DI/images/juguete_gato.jpg"},
            {"nombre": "Shampoo Antipulgas para Perro", "precio": 20.25, "imagen": "Projecte_DI/images/shampoo_perro.jpg"},
            {"nombre": "Pienso para Perro (1kg)", "precio": 14.50, "imagen": "Projecte_DI/images/pienso_perro.jpg"},
            {"nombre": "Pienso para Gato (1kg)", "precio": 12.99, "imagen": "Projecte_DI/images/pienso_gato.jpg"}
        ]
        self.carrito = []
        
        self.initUI()
        
    def initUI(self):
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Lista de productos
        self.lista_productos = QListWidget()

        for producto in self.productos:
            item = QListWidgetItem()
            widget = QWidget()
            hbox = QHBoxLayout()
            
            # Agregar imagen (si está disponible)
            if 'imagen' in producto:
                label_imagen = QLabel()
                pixmap = QPixmap(producto['imagen'])
                pixmap_resized = pixmap.scaled(150, 150, Qt.KeepAspectRatio)
                label_imagen.setPixmap(pixmap_resized)
                label_imagen.setFixedSize(150, 150)
                label_imagen.setStyleSheet("border: 1px solid gray;")
                hbox.addWidget(label_imagen)
            
            # Agregar nombre y precio del producto
            label_info = QLabel(f"<b>{producto['nombre']}</b><br>Precio: ${producto['precio']:.2f}")
            label_info.setStyleSheet("color:black;")
            hbox.addWidget(label_info)
            
            widget.setLayout(hbox)
            item.setSizeHint(widget.sizeHint())
            self.lista_productos.addItem(item)
            self.lista_productos.setItemWidget(item, widget)
        
        # Estilizar la lista de productos
        self.lista_productos.setStyleSheet("QListWidget { border: 1px solid gray; background-color: #f0f0f0; }")
        
        # Botones de acciones
        self.btn_agregar = QPushButton(QIcon('add.png'), 'Agregar al Carrito')
        self.btn_agregar.clicked.connect(self.agregarAlCarrito)
        
        self.btn_comprar_ahora = QPushButton(QIcon('buy.png'), 'Comprar Ahora')
        self.btn_comprar_ahora.clicked.connect(self.comprarAhora)
        
        self.btn_ver_carrito = QPushButton(QIcon('cart.png'), 'Ver Carrito')
        self.btn_ver_carrito.clicked.connect(self.verCarrito)
        
        # Layout de botones
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_agregar)
        btn_layout.addWidget(self.btn_comprar_ahora)
        btn_layout.addWidget(self.btn_ver_carrito)
        
        # Agregar widgets al layout principal
        layout.addWidget(QLabel("<h2>Lista de Productos Veterinarios:</h2>"))
        layout.addWidget(self.lista_productos)
        layout.addLayout(btn_layout)
        
    def agregarAlCarrito(self):
        # Obtener el elemento seleccionado en la lista
        items = self.lista_productos.selectedItems()
        if not items:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, seleccione un producto de la lista.')
            return

        # Tomar solo el primer elemento seleccionado
        selected_item = items[0]
        widget = self.lista_productos.itemWidget(selected_item)
        label_text = widget.layout().itemAt(1).widget().text()

        # Extraer el nombre y el precio del producto del texto del label
        producto_nombre = label_text.split('<b>')[1].split('</b>')[0]
        producto_precio = float(label_text.split('$')[1])

        # Agregar el producto al carrito
        self.carrito.append({"nombre": producto_nombre, "precio": producto_precio})
        QMessageBox.information(self, 'Añadido al Carrito', f'El producto "{producto_nombre}" ha sido agregado al carrito.')
    
    def verCarrito(self):
        carrito_window = CarritoWindow(self.carrito)
        carrito_window.exec()

    def comprarAhora(self):
        QMessageBox.information(self, 'Compra Realizada', '¡Compra realizada con éxito!')

class CarritoWindow(QDialog):
    def __init__(self, carrito):
        super().__init__()
        self.setWindowTitle('Carrito de Compras')
        self.carrito = carrito
        self.setStyleSheet(
            '''
                @QMainWindow{
                    color: black;
                }
            '''
        )
        self.initUI()
        
    def initUI(self):
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Lista de productos en el carrito
        self.lista_carrito = QListWidget()
        self.lista_carrito.setStyleSheet("QListWidget { border: 1px solid gray; background-color: #f0f0f0; }")
        for producto in self.carrito:
            item = QListWidgetItem()
            widget = QWidget()
            hbox = QHBoxLayout()
            
            # Agregar nombre y precio del producto
            label_info = QLabel(f"<b>{producto['nombre']}</b><br>Precio: ${producto['precio']:.2f}")
            hbox.addWidget(label_info)
            
            widget.setLayout(hbox)
            item.setSizeHint(widget.sizeHint())
            self.lista_carrito.addItem(item)
            self.lista_carrito.setItemWidget(item, widget)
        
        # Total del carrito
        total = sum([p['precio'] for p in self.carrito])
        self.label_total = QLabel(f"<h3>Total: ${total:.2f}</h3>")
        layout.addWidget(QLabel("<h2>Carrito de Compras:</h2>"))
        layout.addWidget(self.lista_carrito)
        layout.addWidget(self.label_total)
        
        # Botón para eliminar producto del carrito
        self.btn_eliminar = QPushButton(QIcon('delete.png'), 'Eliminar del Carrito')
        self.btn_eliminar.clicked.connect(self.eliminarDelCarrito)
        
        # Botón para eliminar todos los productos del carrito
        self.btn_eliminar_todo = QPushButton(QIcon('delete_all.png'), 'Eliminar Todo del Carrito')
        self.btn_eliminar_todo.clicked.connect(self.eliminarTodoDelCarrito)
        
        # Botón para comprar ahora
        self.btn_comprar_todo = QPushButton('Comprar Todo')
        self.btn_comprar_todo.clicked.connect(self.comprarTodo)
        
        # Botón para comprar producto seleccionado
        self.btn_comprar_producto = QPushButton('Comprar Producto')
        self.btn_comprar_producto.clicked.connect(self.comprarProducto)
        
        # Botón para cerrar ventana
        self.btn_cerrar = QPushButton(QIcon('close.png'), 'Cerrar')
        self.btn_cerrar.clicked.connect(self.close)
        
        # Layout de botones
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_eliminar)
        btn_layout.addWidget(self.btn_eliminar_todo)
        btn_layout.addWidget(self.btn_comprar_todo)
        btn_layout.addWidget(self.btn_comprar_producto)
        btn_layout.addWidget(self.btn_cerrar)
   
        layout.addLayout(btn_layout)
        
    def eliminarDelCarrito(self):
        # Obtener el producto seleccionado en el carrito
        items = self.lista_carrito.selectedItems()
        if not items:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, seleccione un producto del carrito.')
            return
        
        selected_item = items[0]
        widget = self.lista_carrito.itemWidget(selected_item)
        label_text = widget.layout().itemAt(0).widget().text()

        # Extraer el nombre y el precio del producto del texto del label
        producto_nombre = label_text.split('<b>')[1].split('</b>')[0]
        producto_precio = float(label_text.split('$')[1])

        # Eliminar producto del carrito
        for producto in self.carrito:
            if producto['nombre'] == producto_nombre and producto['precio'] == producto_precio:
                self.carrito.remove(producto)
                break
        
        # Actualizar la lista del carrito
        self.actualizarCarrito()
        QMessageBox.information(self, 'Eliminado del Carrito', f'El producto "{producto_nombre}" ha sido eliminado del carrito.')

    def eliminarTodoDelCarrito(self):
        # Eliminar todos los productos del carrito
        self.carrito.clear()
        self.lista_carrito.clear()
        self.actualizarCarrito()
        QMessageBox.information(self, 'Carrito Vacío', 'Todos los productos han sido eliminados del carrito.')
    
    def comprarTodo(self):
        if not self.carrito:
            QMessageBox.warning(self, 'Advertencia', 'El carrito está vacío.')
            return

        total = sum([p['precio'] for p in self.carrito])
        reply = QMessageBox.question(self, 'Comprar Todo', f'¿Desea comprar todos los productos del carrito por un total de ${total:.2f}?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Compra Realizada', f'Se ha realizado la compra por un total de ${total:.2f}.')
            self.carrito.clear()
            self.lista_carrito.clear()
            self.actualizarCarrito()
        else:
            QMessageBox.information(self, 'Compra Cancelada', 'La compra ha sido cancelada.')
    
    def comprarProducto(self):
        items = self.lista_carrito.selectedItems()
        if not items:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, seleccione un producto del carrito.')
            return
        
        selected_item = items[0]
        widget = self.lista_carrito.itemWidget(selected_item)
        label_text = widget.layout().itemAt(0).widget().text()

        # Extraer el nombre y el precio del producto del texto del label
        producto_nombre = label_text.split('<b>')[1].split('</b>')[0]
        producto_precio = float(label_text.split('$')[1])

        # Eliminar producto del carrito
        for producto in self.carrito:
            if producto['nombre'] == producto_nombre and producto['precio'] == producto_precio:
                self.carrito.remove(producto)
                break
        
        # Actualizar la lista del carrito
        self.actualizarCarrito()
        QMessageBox.information(self, 'Compra Realizada', f'Se ha comprado el producto "{producto_nombre}" por un total de ${producto_precio:.2f}.')

    def actualizarCarrito(self):
        self.lista_carrito.clear()
        for producto in self.carrito:
            item = QListWidgetItem()
            widget = QWidget()
            hbox = QHBoxLayout()
            
            # Agregar nombre y precio del producto
            label_info = QLabel(f"<b>{producto['nombre']}</b><br>Precio: ${producto['precio']:.2f}")
            hbox.addWidget(label_info)
            
            widget.setLayout(hbox)
            item.setSizeHint(widget.sizeHint())
            self.lista_carrito.addItem(item)
            self.lista_carrito.setItemWidget(item, widget)
        
        total = sum([p['precio'] for p in self.carrito])
        self.label_total.setText(f"<h3>Total: ${total:.2f}</h3>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TiendaApp()
    ventana.show()
    sys.exit(app.exec())
