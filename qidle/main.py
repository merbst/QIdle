import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description='IDLE clone made with PyQt and pyQode')
    parser.add_argument('files', type=str, nargs='*',
                        help='List of files to open, if any')
    parser.add_argument('--qt', default=5, type=int,
                        help='The qt api to use: 4 or 5. Default is 5 (PyQt5)')
    parser.add_argument('--verbose', dest='verbose', action='store_true',
                        help='Verbose mode will enable debug and info '
                             'messages to be shown in the application log')
    return parser.parse_args()


def main():
    args = parse_args()
    os.environ['QT_API'] = 'pyqt%d' % args.qt
    from .app import Application
    app = Application(args.files, args.verbose)
    app.run()
    del app
