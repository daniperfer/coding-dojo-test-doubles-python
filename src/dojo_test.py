import unittest
from unittest.mock import MagicMock
from utils import PrintCollaborator
from datetime import datetime
from dojo import PrintDate

TEST_DATA = datetime.now()


class PrinterSpy(PrintCollaborator):
    def __init__(self):
        self.param = None
        self.counter = 0
        PrintCollaborator.__init__(self)

    def print_param(self, param):
        self.param = param
        self.counter += 1
        PrintCollaborator.print_param(self, param)

    def check_param(self):
        return self.param

    def check_times(self):
        return self.counter


class DaterStub:
    def __init__(self, date=TEST_DATA):
        self.date = date

    def get_current_date(self):
        return self.date


class PrintDateTest(unittest.TestCase):

    def test_current_date_works(self):
        dater_object = DaterStub()
        printer_object = PrinterSpy()
        print_object = PrintDate(printer=printer_object, dater=dater_object)
        print_object.print_current_date()

        # test that method print is called once when print_current_date() is called, and the date is TEST_DATA
        self.assertEqual(printer_object.check_param(), TEST_DATA)
        self.assertEqual(printer_object.check_times(), 1)
