import os
os.environ['QT_API'] = 'pyqt4'
import logging
logging.basicConfig(level=logging.INFO)
from .app import Application


def main():
    app = Application()
    app.run()
    del app
