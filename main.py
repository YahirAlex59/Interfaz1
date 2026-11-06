import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_formulario import Ui_Formulario


class VentanaPrincipal(QMainWindow):

  def __init__(self):
    super().__init__()
    self.ui = Ui_Formulario()
    self.ui.setupUi(self)

    # remplazo de "PushButton"
    self.ui.btn_guardar.setText("Guardar")

    # botón conectado con la función de guardado
    self.ui.btn_guardar.clicked.connect(self.guardar_en_txt)

  def guardar_en_txt(self):
    nombre = self.ui.txt_nombre.text().strip()
    apellido = self.ui.txt_apellido.text().strip()
    matricula = self.ui.txt_matricula.text().strip()
    telefono = self.ui.txt_telefono.text().strip()

    if not all([nombre, apellido, matricula, telefono]):
      QMessageBox.warning(
          self,
          "Campos vacíos",
          "Por favor completa todos los datos antes de guardar.",
      )
      return
    try:
      with open("registros.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre:    {nombre}\n")
        archivo.write(f"Apellido:  {apellido}\n")
        archivo.write(f"Matrícula: {matricula}\n")
        archivo.write(f"Teléfono:  {telefono}\n")
        archivo.write("-" * 35 + "\n")

      QMessageBox.information(
          self, "Éxito", "Datos guardados correctamente en 'registros.txt'."
      )
      self.limpiar_formulario()

    except Exception as e:
      QMessageBox.critical(
          self, "Error", f"No se pudo guardar el archivo:\n{e}"
      )

  def limpiar_formulario(self):
    self.ui.txt_nombre.clear()
    self.ui.txt_apellido.clear()
    self.ui.txt_matricula.clear()
    self.ui.txt_telefono.clear()
    self.ui.txt_nombre.setFocus()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaPrincipal()
  ventana.show()
  sys.exit(app.exec())