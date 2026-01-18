from PyQt5 import QtWidgets
from .settings import get_version, save_settings, load_settings

class KeybindsUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Keybinds")
        self.resize(500, 200)
        
        layouts = []

        # Version Label
        self.version_label = QtWidgets.QLabel(f" Version: {get_version()}", self)
        vl = QtWidgets.QHBoxLayout()
        vl.addWidget(self.version_label)
        layouts.append(vl)

        # open
        self.open_label = QtWidgets.QLabel("Open file: ", self)
        self.open_le = QtWidgets.QLineEdit(self)
        self.open_le.setText(load_settings()["open"])
        
        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addWidget(self.open_label)
        h1_layout.addWidget(self.open_le)
        layouts.append(h1_layout)
        
        # up
        self.up_label = QtWidgets.QLabel("Up command: ", self)
        self.up_le = QtWidgets.QLineEdit(self)
        self.up_le.setText(load_settings()["up"])
        
        h2_layout = QtWidgets.QHBoxLayout()
        h2_layout.addWidget(self.up_label)
        h2_layout.addWidget(self.up_le)
        layouts.append(h2_layout)
        
        # down
        self.down_label = QtWidgets.QLabel("Down command: ", self)
        self.down_le = QtWidgets.QLineEdit(self)
        self.down_le.setText(load_settings()["down"])
        
        h3_layout = QtWidgets.QHBoxLayout()
        h3_layout.addWidget(self.down_label)
        h3_layout.addWidget(self.down_le)
        layouts.append(h3_layout)
        
        # left
        self.left_label = QtWidgets.QLabel("Left command: ", self)
        self.left_le = QtWidgets.QLineEdit(self)
        self.left_le.setText(load_settings()["left"])
        
        h4_layout = QtWidgets.QHBoxLayout()
        h4_layout.addWidget(self.left_label)
        h4_layout.addWidget(self.left_le)
        layouts.append(h4_layout)
        
        # right
        self.right_label = QtWidgets.QLabel("Right command: ", self)
        self.right_le = QtWidgets.QLineEdit(self)
        self.right_le.setText(load_settings()["right"])
        
        h5_layout = QtWidgets.QHBoxLayout()
        h5_layout.addWidget(self.right_label)
        h5_layout.addWidget(self.right_le)
        layouts.append(h5_layout)
        
        # opacity up
        self.op_up_label = QtWidgets.QLabel("Opacity up command: ", self)
        self.op_up_le = QtWidgets.QLineEdit(self)
        self.op_up_le.setText(load_settings()["op_up"])
        
        h7_layout = QtWidgets.QHBoxLayout()
        h7_layout.addWidget(self.op_up_label)
        h7_layout.addWidget(self.op_up_le)
        layouts.append(h7_layout)
        
        # opacity down
        self.op_down_label = QtWidgets.QLabel("Opacity down command: ", self)
        self.op_down_le = QtWidgets.QLineEdit(self)
        self.op_down_le.setText(load_settings()["op_down"])
        
        h8_layout = QtWidgets.QHBoxLayout()
        h8_layout.addWidget(self.op_down_label)
        h8_layout.addWidget(self.op_down_le)
        layouts.append(h8_layout)
        
        # In
        self.in_label = QtWidgets.QLabel("Zoom in command: ", self)
        self.in_le = QtWidgets.QLineEdit(self)
        self.in_le.setText(load_settings()["in"])
        
        h9_layout = QtWidgets.QHBoxLayout()
        h9_layout.addWidget(self.in_label)
        h9_layout.addWidget(self.in_le)
        layouts.append(h9_layout)
        
        # Out
        self.out_label = QtWidgets.QLabel("Zoom out command: ", self)
        self.out_le = QtWidgets.QLineEdit(self)
        self.out_le.setText(load_settings()["out"])
        
        h10_layout = QtWidgets.QHBoxLayout()
        h10_layout.addWidget(self.out_label)
        h10_layout.addWidget(self.out_le)
        layouts.append(h10_layout)
        
        # Settings
        self.settings_label = QtWidgets.QLabel("Settings command: ", self)
        self.settings_le = QtWidgets.QLineEdit(self)
        self.settings_le.setText(load_settings()["settings"])
        
        h11_layout = QtWidgets.QHBoxLayout()
        h11_layout.addWidget(self.settings_label)
        h11_layout.addWidget(self.settings_le)
        layouts.append(h11_layout)
        
        # Quit
        self.quit_label = QtWidgets.QLabel("Quit command: ", self)
        self.quit_le = QtWidgets.QLineEdit(self)
        self.quit_le.setText(load_settings()["quit"])
        
        h12_layout = QtWidgets.QHBoxLayout()
        h12_layout.addWidget(self.quit_label)
        h12_layout.addWidget(self.quit_le)
        layouts.append(h12_layout)
        
        # Save Button
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self._save_settings)
        
        h13_layout = QtWidgets.QHBoxLayout()
        h13_layout.addWidget(self.save_button)
        layouts.append(h13_layout)
        
        # Layout
        v_layout = QtWidgets.QVBoxLayout(self)
        for i in layouts:
            v_layout.addLayout(i)
            
    def _save_settings(self):
        open_value = self.open_le.text().strip()
        up_value = self.up_le.text().strip()
        down_value = self.down_le.text().strip()
        left_value = self.left_le.text().strip()
        right_value = self.right_le.text().strip()
        op_up_value = self.op_up_le.text().strip()
        op_down_value = self.op_down_le.text().strip()
        in_value = self.in_le.text().strip()
        out_value = self.out_le.text().strip()
        settings_value = self.settings_le.text().strip()
        quit_value = self.quit_le.text().strip()

        save_settings(
            open_=open_value,
            up=up_value,
            down=down_value,
            left=left_value,
            right=right_value,
            op_up=op_up_value,
            op_down=op_down_value,
            in_=in_value,
            out=out_value,
            settings_=settings_value,
            quit=quit_value
        )
        
        self.accept()
