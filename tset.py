import unittest
import os
import sentiment_analysis

class TestDemo(unittest.TestCase):

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
        sentiment_analysis.input = ""
        self.assertTrue(sentiment_analysis.print_result(sentiment_analysis.analyze))

    def test_complex_print_result(self):
        """Test method print_result"""
        sentiment_analysis.input = "┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬"
        a = sentiment_analysis.hash_tag_list
        self.assertTrue(sentiment_analysis.print_result(sentiment_analysis.analyze))
