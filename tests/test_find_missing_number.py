import unittest

from example_module import find_missing_number

class Test_Find_Missing_Number(unittest.TestCase):
    def test_case_1(self):
        A = [1,2,3,4,6]
        self.assertEqual(find_missing_number(A,0,len(A)), 5) # 5 is the missing number
    def test_case_2(self):
        A = [4,5,7,8,9]
        self.assertEqual(find_missing_number(A,0,len(A)), 6) # 6 is the missing number

if __name__ == "__main__":
    unittest.main()