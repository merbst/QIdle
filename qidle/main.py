import os
from .argparser import parse_args


def main():
    args = parse_args()
    os.environ['QT_API'] = 'pyqt%d' % args.qt
    from .app import Application
    app = Application(args.files, args.verbose)
    app.run()
    del app
