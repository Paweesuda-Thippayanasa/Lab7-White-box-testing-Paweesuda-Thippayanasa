# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# 653380137-5 ปวีณ์สุดา ทิพยนาสา  sec.1
import unittest
from source.CountClump import CountClump

class TestCountClump(unittest.TestCase):

    def setUp(self):
        self.count_clump = CountClump()

    def test_none_input(self):
        self.assertEqual(self.count_clump.count_clumps(None), 0)

    def test_empty_list(self):
        self.assertEqual(self.count_clump.count_clumps([]), 0)

    def test_single_clump(self):
        self.assertEqual(self.count_clump.count_clumps([3, 1, 1, 1]), 1)

    def test_no_clumps(self):
        self.assertEqual(self.count_clump.count_clumps([1, 2, 3]), 0)

    def test_multiple_clumps(self):
        self.assertEqual(self.count_clump.count_clumps([1, 2, 2, 3, 3]), 2)

    def test_alternating_numbers(self):
        self.assertEqual(self.count_clump.count_clumps([1, 2, 1, 2, 1, 2]), 0)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCountClump('test_none_input'))
    suite.addTest(TestCountClump('test_empty_list'))
    suite.addTest(TestCountClump('test_single_clump'))
    suite.addTest(TestCountClump('test_no_clumps'))
    suite.addTest(TestCountClump('test_multiple_clumps'))
    suite.addTest(TestCountClump('test_alternating_numbers'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
