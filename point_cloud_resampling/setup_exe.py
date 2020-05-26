import distutils
import sys
from cx_Freeze import setup, Executable
import os.path
import opcode
distutils_path = os.path.join(os.path.dirname(opcode.__file__), 'distutils')


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


options = {
    'build_exe': {
        'include_files': [(distutils_path, 'distutils'), 'tk86t.dll', 'tcl86t.dll'],
        'excludes': ['distutils'],
        'packages': ["pandas", "numpy", "scipy", "open3d", "rtree", "math", 'pygments', 'pkg_resources._vendor'],
        'includes': ['atexit', 'pygments.lexers'],
    },
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('src/point_cloud_resampling/app/app.py', base=base)
]


setup(
    name="resampling_point_cloud_data",
    version="0.0.1",
    description="A gui-based tree algorithm to resample large data clouds",
    options=options,
    executables=executables
)
