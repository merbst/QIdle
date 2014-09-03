import os
os.environ['QT_API'] = 'pyqt4'
from .app import Application


def main():
    app = Application()
    app.run()
    del app
