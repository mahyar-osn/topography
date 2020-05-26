import sys

from PyQt4 import QtGui

from src.point_cloud_resampling.view.resampling_app_widget import ResamplingWidget


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    app.setPalette(QtGui.QApplication.style().standardPalette())
    ui = ResamplingWidget()
    sys.exit(app.exec_())

main()
