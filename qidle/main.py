import os
from .argparser import parse_args


def main(args=None):
    if not args:
        args = parse_args()
    # if not 'QT_API' in os.environ:
    os.environ['QT_API'] = 'pyqt%d' % args.qt
    from .app import Application
    app = Application(args.files, args.verbose)
    app.run()
    del app
