from PySide import QtGui

from .ui_resampling_app import Ui_MainWindow


class ResamplingWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ResamplingWidget, self).__init__(parent)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._source_path = None

        self._make_connections()
        self.showNormal()

    def _make_connections(self):
        self._ui.open_pushButton.clicked.connect(self._select_source)
        self._ui.save.clicked.connect(self._save)

    def _select_source(self):
        self._source_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Source"))

        if not self._source_path:
            QtGui.QMessageBox.warning(self, 'Invalid source file.', 'Please select a valid source.')
            return

        # display path
        self._ui.source_path.setText(self._source_path)

    def _save(self):
        self._ui.statusbar.showMessage('Saving...', 10000)

        # check source path
        if not self._source_path:
            QtGui.QMessageBox.warning(self, 'Invalid source file', 'Please select a valid source')
            return

        # get save path
        save_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select a destination"))
        if not save_path:
            QtGui.QMessageBox.warning(self, 'Invalid destination.', 'Please select a valid folder.')
            return
        save_path = self._update_save_path(save_path)

        self._grid(save_path)

        self._ui.statusbar.showMessage('Resampled data saved.', 5000)
