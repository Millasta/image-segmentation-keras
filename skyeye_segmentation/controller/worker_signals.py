import traceback, sys
from PyQt5.QtCore import QObject, pyqtSignal


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        `str` message to acknowledge the achievement

    progrssed
        `int` percentage of actual progression

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    '''
    finished = pyqtSignal(str)
    progressed = pyqtSignal(int)
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)