import unittest
from sentiment_analysis import print_result,StdOutListener


class TestDemo(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test_null_print_result(self):
        """Test method print_result"""
        self.hash_tag_list = ""
        self.assertTrue(print_result(self.analyze))

    def test_complex_print_result(self):
        """Test method print_result"""
        self.hash_tag_list = "┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬"
        a = self.hash_tag_list
        self.assertTrue(print_result(self.analyze))