from datetime import datetime

from PySide import QtGui

from .ui_resampling_app import Ui_MainWindow
from ..model.master import PointCloudResampling


class ResamplingWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ResamplingWidget, self).__init__(parent)

        self._model = PointCloudResampling()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._check_settings = dict(input_file=False, output_file=False, factor=False)
        self._previous_location = ''

        self._ui.date_label.setText("Date: " + datetime.today().strftime('%d-%m-%Y'))

        self._ui.plotResampled_pushButton.setEnabled(False)
        self._ui.plotOriginal_pushButton.setEnabled(False)
        self._ui.run_pushButton.setEnabled(False)
        self._ui.export_pushButton.setEnabled(False)

        self._source_path = None

        self._make_connections()
        self.showNormal()

    def _make_connections(self):
        self._ui.load_pushButton.clicked.connect(self._select_source)
        self._ui.output_pushButton.clicked.connect(self._select_output_location)
        self._ui.doubleSpinBox.valueChanged.connect(self._factor_changed)
        self._ui.run_pushButton.clicked.connect(self._run)
        self._ui.plotResampled_pushButton.clicked.connect(self._plot_resampled)
        self._ui.plotOriginal_pushButton.clicked.connect(self._plot_original)
        self._ui.export_pushButton.clicked.connect(self._export_report)

    def _select_source(self):
        self._source_path = QtGui.QFileDialog.getOpenFileName(self, 'Select File Location', self._previous_location)

        if not self._source_path:
            QtGui.QMessageBox.warning(self, 'Invalid source file.', 'Please select a valid source.')
            return

        # set input in the model
        if self._source_path:
            self._previous_location = self._source_path[0]
        self._model.set_input_file(self._previous_location)
        self._check_settings["input_file"] = True
        self._check_run()

    def _select_output_location(self):
        self._output_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Output Location:"))

        if not self._output_path:
            QtGui.QMessageBox.warning(self, 'Invalid output file.', 'Please select a valid path.')
            return

        # set output in the model
        self._model.set_output_location(self._output_path)
        self._check_settings["output_file"] = True
        self._check_run()

    def _factor_changed(self):
        value = self._ui.doubleSpinBox.value()
        self._model.set_factor(value)
        self._check_settings["factor"] = True
        self._check_run()

    def _check_run(self):
        if list(self._check_settings.values()) == [True, True, True]:
            self._ui.run_pushButton.setEnabled(True)

    def _run(self):
        self._ui.statusbar.showMessage('Loading file...', 10000)
        self._model.resample()
        self._ui.plotResampled_pushButton.setEnabled(True)
        self._ui.plotOriginal_pushButton.setEnabled(True)

        self._ui.origSampleSize_label.setText("Original Sample Size: {}".format(self._model.get_original_size()))
        self._ui.resSampleSize_label.setText("Resampled Sample Size: {}".format(self._model.get_resampled_size()))
        self._ui.origMinMax_label.setText("Original Min/Max: {0}/{1}".format(self._model.get_original_min(),
                                                                             self._model.get_original_max()))
        self._ui.resMinMax_label.setText("Resampled Min/Max: {0}/{1}".format(self._model.get_resampled_min(),
                                                                             self._model.get_resampled_max()))
        self._ui.export_pushButton.setEnabled(True)

    def _plot_resampled(self):
        self._model.view_resampled()

    def _plot_original(self):
        self._model.view_original()

    def _export_report(self):
        self._model.get_result_report()
