"""
QIdle entry point. To run the IDE install pyqode.python using pip and run this
script.

"""
import logging
logging.basicConfig(level=logging.INFO)
from qidle.main import main


if __name__ == '__main__':
    main()
