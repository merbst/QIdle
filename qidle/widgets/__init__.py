from .class_explorer import ClassExplorer
from .run_config import RunConfigWidget
from .picker import FilePicker
try:
    from .shell import Shell
except ImportError:
    # IPython not available
    Shell = None
