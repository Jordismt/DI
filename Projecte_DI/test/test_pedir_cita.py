import sys
import os
import pytest
from PySide6.QtWidgets import QApplication

# Afegir el directori que conté pedir_cita.py al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pedir_cita import PedirCita

# Crear la instància de QApplication una sola vegada al principi del fitxer
app = QApplication(sys.argv)


#Test per a comprovar que no s'afegisca Text al cuadro de text si els valors del ComboBox son els de per Defecte
def test_pedir_cita_no_agregar_texto(qtbot):
    # Crear i mostrar la finestra de PedirCita
    ventana = PedirCita()

    # Obtindre referència al QTextEdit
    cuadro_texto = ventana.cuadro_texto

    # Obtindre el text actual al QTextEdit
    texto_actual = cuadro_texto.toPlainText()

    # Establir els ComboBox a els valors per defecte
    qtbot.waitUntil(lambda: ventana.tipo_mascota_combo.setCurrentIndex(0))
    qtbot.waitUntil(lambda: ventana.servicio.setCurrentIndex(0))

    # Esperar un moment per a que el text tinga l'oportunitat d'afegir-se (si s'afegira)
    qtbot.wait(1000)

    # Verificar que no s'haja afegit cap text al QTextEdit si els ComboBox estan en els valors per defecte
    assert cuadro_texto.toPlainText() == texto_actual

if __name__ == '__main__':

    pytest.main([__file__])
