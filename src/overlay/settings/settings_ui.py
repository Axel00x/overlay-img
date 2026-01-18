from PyQt5 import QtWidgets
from .settings import get_version, save_settings
from .keybinds_ui import KeybindsUI

class SettingsUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.resize(300, 200)

        # Version Label
        self.version_label = QtWidgets.QLabel(f" Version: {get_version()}", self)
        
        layouts = []

        # Move
        self.move_label = QtWidgets.QLabel("Move by: ", self)
        self.move_le = QtWidgets.QLineEdit(self)
        self.move_le.setPlaceholderText("Number of px...")
        
        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addWidget(self.move_label)
        h1_layout.addWidget(self.move_le)
        layouts.append(h1_layout)
        
        # Zoom
        self.zoom_label = QtWidgets.QLabel("Zoom by: ", self)
        self.zoom_le = QtWidgets.QLineEdit(self)
        self.zoom_le.setPlaceholderText("Number of px...")
        
        h2_layout = QtWidgets.QHBoxLayout()
        h2_layout.addWidget(self.zoom_label)
        h2_layout.addWidget(self.zoom_le)
        layouts.append(h2_layout)
        
        # Opacity
        self.opacity_label = QtWidgets.QLabel("Opacity: ", self)
        self.opacity_le = QtWidgets.QLineEdit(self)
        self.opacity_le.setPlaceholderText("0.0 to 1.0")
        
        h3_layout = QtWidgets.QHBoxLayout()
        h3_layout.addWidget(self.opacity_label)
        h3_layout.addWidget(self.opacity_le)
        layouts.append(h3_layout)
        
        # Save Button
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self._save_settings)
        
        self.keybinds_button = QtWidgets.QPushButton("Keybinds", self)
        self.keybinds_button.clicked.connect(self._open_keybinds_ui)
        
        h4_layout = QtWidgets.QHBoxLayout()
        h4_layout.addWidget(self.save_button)
        h4_layout.addWidget(self.keybinds_button)
        layouts.append(h4_layout)
        
        # Layout
        v_layout = QtWidgets.QVBoxLayout(self)
        for i in layouts:
            v_layout.addLayout(i)
            
    def _save_settings(self):
        move_value = self.move_le.text()
        zoom_value = self.zoom_le.text()
        opacity_value = self.opacity_le.text()

        save_settings(
            move=int(move_value) if move_value else None,
            zoom=int(zoom_value) if zoom_value else None,
            opacity=float(opacity_value) if opacity_value else None
        )
        
        self.accept()
    
    def _open_keybinds_ui(self):
        try:
            dialog = KeybindsUI(self)
            dialog.exec_()
        except Exception as e:
            print("Error opening settings:", e)
            QtWidgets.QMessageBox.critical(
                self, "Error", f"Failed to open settings: {e}"
            )