import os.path
import unittest
from app.controllers.services.import_excel import analysis_excel


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = r'C:\Users\wikil\Desktop\test.xlsx'

    def test_analysis(self):
        a, b = analysis_excel(self.file_path)
        print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
