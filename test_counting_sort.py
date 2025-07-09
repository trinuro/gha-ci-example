import unittest

from example_module import counting_sort

class test_counting_sort(unittest.TestCase):
    def testCase1(self):
        test = [1,3,4,2,2,1,0]
        self.assertEqual(counting_sort(test,4), [0, 1, 1, 2, 2, 3, 4])
    def testCase2(self):
        test=[4,2,3,3,22]
        with self.assertRaises(IndexError):
            counting_sort(test,4)

if __name__=="__main__":
    unittest.main()