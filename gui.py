import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

class DragAndDropLabel(QLabel):
    def __init__(self, parent=None):
        super(DragAndDropLabel, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText("\n\n Drag and Drop an Image Here \n\n")
        self.setStyleSheet("border: 2px dashed #aaa;")
        self.file_path = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            self.file_path = url.toLocalFile()
            self.setPixmap(QPixmap(self.file_path).scaled(self.width(), self.height(), Qt.KeepAspectRatio))
            event.accept()
        else:
            event.ignore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop Image")
        self.setGeometry(100, 100, 800, 600)

        self.label = DragAndDropLabel(self)
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setText("Result will be shown here.")
        
        self.check_button = QPushButton("Check", self)
        self.check_button.clicked.connect(self.check_image)

        self.clear_button = QPushButton("Clear Image", self)
        self.clear_button.clicked.connect(self.clear_image)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.check_button)
        button_layout.addWidget(self.clear_button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Load VGG16 model
        self.vgg16_model = VGG16(weights='imagenet')

    def check_image(self):
        if self.label.file_path:
            img_path = self.label.file_path
            img_array = self.preprocess_image(img_path)
            predictions = self.vgg16_model.predict(img_array)
            decoded_predictions = decode_predictions(predictions, top=3)[0]
            result = f"Predicted: {decoded_predictions}"
            self.result_label.setText(result)
        else:
            self.result_label.setText("Please drag and drop an image.")

    def clear_image(self):
        self.label.clear()
        self.label.setText("\n\n Drag and Drop an Image Here \n\n")
        self.result_label.setText("Result will be shown here.")
        self.label.file_path = None

    def preprocess_image(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
