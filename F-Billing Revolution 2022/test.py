from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.name = QLineEdit()
        self.program_type = QLineEdit()
        self.product_code = QLineEdit()
        self.customer = QLineEdit()
        self.vendor = QLineEdit()
        self.n_errors = QSpinBox()
        self.n_errors.setRange(0, 1000)
        self.comments = QTextEdit()

        self.generate_btn = QPushButton("Generate PDF")

        layout = QFormLayout()
        layout.addRow("Name", self.name)
        layout.addRow("Program Type", self.program_type)
        layout.addRow("Product Code", self.product_code)
        layout.addRow("Customer", self.customer)
        layout.addRow("Vendor", self.vendor)
        layout.addRow("No. of Errors", self.n_errors)

        layout.addRow("Comments", self.comments)
        layout.addRow(self.generate_btn)

        self.setLayout(layout)


app = QApplication([])
w = Window()
w.show()
app.exec()