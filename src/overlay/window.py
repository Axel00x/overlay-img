import os
import ctypes
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia, QtMultimediaWidgets

GWL_EXSTYLE      = -20
WS_EX_LAYERED    = 0x00080000
WS_EX_TRANSPARENT= 0x00000020

class OverlayWindow(QtWidgets.QMainWindow):
    sig_open    = QtCore.pyqtSignal()
    sig_up      = QtCore.pyqtSignal()
    sig_down    = QtCore.pyqtSignal()
    sig_left    = QtCore.pyqtSignal()
    sig_right   = QtCore.pyqtSignal()
    sig_plus    = QtCore.pyqtSignal()
    sig_minus   = QtCore.pyqtSignal()
    sig_zoom_in  = QtCore.pyqtSignal()
    sig_zoom_out = QtCore.pyqtSignal()
    sig_quit    = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._connect_signals()
        self._make_click_through()

    def _setup_ui(self):
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.container    = QtWidgets.QStackedWidget(self)
        self.image_label  = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.image_label.setScaledContents(False)
        self._orig_pixmap = None # Placeholder for original pixmap if needed
        #self.video_widget = QtMultimediaWidgets.QVideoWidget()
        #self.player       = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        #self.player.setVideoOutput(self.video_widget)

        self.container.addWidget(self.image_label)
        #self.container.addWidget(self.video_widget)
        self.container.setCurrentWidget(self.image_label)
        self.setCentralWidget(self.container)

        self.opacity = 1.0
        self.w, self.h = 400, 300
        self.setWindowOpacity(self.opacity)
        self.resize(self.w, self.h)
        self.show()

    def _make_click_through(self):
        user32 = ctypes.windll.user32
        if ctypes.sizeof(ctypes.c_void_p) == 8:  # 64-bit
            GetWindowLongPtr = user32.GetWindowLongPtrW
            SetWindowLongPtr = user32.SetWindowLongPtrW
            GetWindowLongPtr.restype = ctypes.c_longlong
            SetWindowLongPtr.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_longlong)
        else:  # 32-bit
            GetWindowLongPtr = user32.GetWindowLongW
            SetWindowLongPtr = user32.SetWindowLongW
            GetWindowLongPtr.restype = ctypes.c_long
            SetWindowLongPtr.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_long)

        hwnd = int(self.winId())
        ex_style = GetWindowLongPtr(hwnd, GWL_EXSTYLE)
        ex_style |= (WS_EX_LAYERED | WS_EX_TRANSPARENT)
        SetWindowLongPtr(hwnd, GWL_EXSTYLE, ex_style)

    def _connect_signals(self):
        self.sig_open .connect(self.open_file)
        self.sig_up   .connect(lambda: self.move_by(   0, -10))
        self.sig_down .connect(lambda: self.move_by(   0,  10))
        self.sig_left .connect(lambda: self.move_by(-10,   0))
        self.sig_right.connect(lambda: self.move_by( 10,   0))
        self.sig_plus .connect(lambda: self.change_opacity( 0.05))
        self.sig_minus.connect(lambda: self.change_opacity(-0.05))
        self.sig_zoom_in .connect(lambda: self.change_size(10))
        self.sig_zoom_out.connect(lambda: self.change_size(-10))
        self.sig_quit .connect(self.close)

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File",
            os.path.expanduser("~"),
            "Images (*.png *.jpg *.bmp *.jpeg *.gif);;"  # Videos (*.mp4 *.avi *.mov);;All Files (*)
        )
        if not path:
            return

        ext = os.path.splitext(path)[1].lower()
        if ext in ['.png', '.jpg', '.bmp', '.jpeg', '.gif']:
            pix = QtGui.QPixmap(path)
            if pix is None or pix.isNull():
                print("Unable to load the image: ", path)
                return

            self._orig_pixmap = pix
            self._update_pixmap()

            self.container.setCurrentWidget(self.image_label)

            if hasattr(self, "player") and getattr(self, "player") is not None:
                try:
                    self.player.stop()
                except Exception as e:
                    print("Warning: failed to stop player:", e)

            return

        # se arriva qui, non è un'immagine gestita (eventuale gestione video)
        print("Invalid file type for video playback.")
        # url = QtCore.QUrl.fromLocalFile(path)
        # self.player.setMedia(QtMultimedia.QMediaContent(url))
        # self.container.setCurrentWidget(self.video_widget)
        # self.player.play()

    def move_by(self, dx, dy):
        g = self.frameGeometry()
        g.moveTopLeft(g.topLeft() + QtCore.QPoint(dx, dy))
        self.setGeometry(g)

    def change_opacity(self, delta):
        self.opacity = max(0, min(1.0, self.opacity + delta))
        self.setWindowOpacity(self.opacity)
        
    def _update_pixmap(self):
        if not self._orig_pixmap:
            return
        target_w, target_h = self.w, self.h
        scaled = self._orig_pixmap.scaled(
            target_w, target_h,
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled)
        self.image_label.setFixedSize(scaled.size())
    
    def change_size(self, delta):
        new_w = max(100, self.w + delta)
        new_h = max(100, self.h + delta)

        old_geom = self.frameGeometry()
        center = old_geom.center()

        self.w, self.h = new_w, new_h
        self.resize(self.w, self.h)

        new_geom = self.frameGeometry()
        new_geom.moveCenter(center)
        self.setGeometry(new_geom)

        self._update_pixmap()
