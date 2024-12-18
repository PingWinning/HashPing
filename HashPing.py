import hashlib
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton,
    QFileDialog, QWidget, QLineEdit, QComboBox, QHBoxLayout, QFrame
)
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication


class HashVerifier(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HashPing Hash Verifier from PingWinning")
        self.setGeometry(300, 200, 700, 700)
        self.setWindowIcon(QIcon("hash_icon.jpg"))

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()

        # Profile and Marquee Section
        self.profile_message_layout = QHBoxLayout()

        # Profile Image - Rounded
        self.profile_image = QLabel()
        pixmap = QPixmap("pingwining.jpg").scaled(120, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.profile_image.setPixmap(self.make_rounded_pixmap(pixmap))
        self.profile_image.setFixedSize(120, 120)
        self.profile_image.setAlignment(Qt.AlignCenter)
        self.profile_message_layout.addWidget(self.profile_image)

        # Dialogue Box for Marquee
        self.dialogue_box = QLabel(
            "<div style=\"font-size: 14px; font-family: Arial; color: #333; padding: 10px; background-color: #f0f0f0;\">"
            "Secure your files with confidence! Verify hashes to ensure file integrity and detect unwanted modifications.<br>"
            "Support our work and help us build robust, reliable tools: "
            "<a href=\"https://paypal.me/DimitarSimeonov17?country.x=CA&locale.x=en_US\" style=\"color:#0077cc; text-decoration:underline; font-weight:bold;\">Donate via PayPal</a>"
            "</div>"
        )
        self.dialogue_box.setWordWrap(True)
        self.dialogue_box.setTextFormat(Qt.RichText)
        self.dialogue_box.setOpenExternalLinks(True)
        self.dialogue_box.setStyleSheet("border: 2px solid #ccc; border-radius: 10px;")
        self.profile_message_layout.addWidget(self.dialogue_box)

        self.layout.addLayout(self.profile_message_layout)

        # Add Separator
        self.add_separator()

        # File Selection
        self.file_label = QLabel("Select a File to Verify:")
        self.file_label.setStyleSheet("font-weight: bold; font-size: 14px; text-align: center; margin-top: 10px;")
        self.layout.addWidget(self.file_label)

        self.file_button = QPushButton("Choose File")
        self.file_button.setStyleSheet("font-size: 14px; padding: 10px; background-color: #0077cc; color: white; border-radius: 5px;")
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_button)

        self.file_path_label = QLabel("File Path: None")
        self.file_path_label.setStyleSheet("font-size: 12px; text-align: center;")
        self.layout.addWidget(self.file_path_label)

        self.add_separator()

        # Hash Algorithm Selection
        self.hash_algo_label = QLabel("Select Hash Algorithm:")
        self.hash_algo_label.setStyleSheet("font-weight: bold; font-size: 14px; text-align: center;")
        self.layout.addWidget(self.hash_algo_label)

        self.hash_algo_dropdown = QComboBox()
        self.hash_algo_dropdown.setStyleSheet("font-size: 14px; padding: 5px;")
        self.hash_algo_dropdown.addItems([
            "SHA256", "MD5", "SHA1", "SHA224", "SHA384", "SHA512", "BLAKE2b", "BLAKE2s",
            "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512"
        ])
        self.layout.addWidget(self.hash_algo_dropdown)

        self.add_separator()

        # Authentic Hash Input
        self.hash_input_label = QLabel("Enter Authentic Hash (Optional):")
        self.hash_input_label.setStyleSheet("font-weight: bold; font-size: 14px; text-align: center;")
        self.layout.addWidget(self.hash_input_label)

        self.hash_input = QLineEdit()
        self.hash_input.setStyleSheet("font-size: 14px; padding: 5px;")
        self.hash_input.setPlaceholderText("Enter hash to compare (optional)")
        self.layout.addWidget(self.hash_input)

        self.add_separator()

        # Verify Button
        self.verify_button = QPushButton("Calculate and Verify")
        self.verify_button.setStyleSheet("font-size: 14px; padding: 10px; background-color: #0077cc; color: white; border-radius: 5px;")
        self.verify_button.clicked.connect(self.verify_hash)
        self.layout.addWidget(self.verify_button)

        self.add_separator()

        # Calculated Hash Display
        self.calculated_hash_label = QLabel("Calculated Hash: None")
        self.calculated_hash_label.setStyleSheet("font-size: 12px; margin-bottom: 10px;")
        self.layout.addWidget(self.calculated_hash_label)

        self.copy_button = QPushButton("Copy")
        self.copy_button.setStyleSheet("font-size: 14px; padding: 5px; background-color: #0077cc; color: white; border-radius: 5px; width: 80px;")
        self.copy_button.clicked.connect(self.copy_hash)
        self.copy_button.setEnabled(False)
        self.layout.addWidget(self.copy_button, alignment=Qt.AlignRight)

        self.add_separator()

        # Result Display
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-top: 10px;")
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def add_separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line)

    def make_rounded_pixmap(self, pixmap):
        size = min(pixmap.width(), pixmap.height())
        rounded = QPixmap(size, size)
        rounded.fill(Qt.transparent)

        painter = QPainter(rounded)
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return rounded

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_path:
            self.file_path_label.setText(f"File Path: {file_path}")
            self.selected_file = file_path

    def verify_hash(self):
        if not hasattr(self, 'selected_file') or not os.path.exists(self.selected_file):
            self.result_label.setText("❌ Error: No file selected.")
            return

        algo = self.hash_algo_dropdown.currentText().lower()
        with open(self.selected_file, "rb") as f:
            hasher = hashlib.new(algo)
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
            calculated_hash = hasher.hexdigest()

        self.calculated_hash_label.setText(f"Calculated Hash: {calculated_hash}")
        self.copy_button.setEnabled(True)

        user_hash = self.hash_input.text().strip()
        if user_hash:
            if user_hash.lower() == calculated_hash:
                self.result_label.setText("✅ Authenticity Verified: Hashes Match!")
            else:
                self.result_label.setText("❌ Hash Mismatch: File may be altered!")

    def copy_hash(self):
        hash_value = self.calculated_hash_label.text().split(": ")[1]
        QGuiApplication.clipboard().setText(hash_value)
        self.result_label.setText("Hash copied to clipboard!")


if __name__ == "__main__":
    app = QApplication([])
    verifier = HashVerifier()
    verifier.show()
    app.exec()
