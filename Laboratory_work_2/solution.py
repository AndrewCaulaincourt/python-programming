import unittest

def add(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sorted(add([2, 7, 11, 15], 9)), [0, 1])

    def test_case_2(self):
        self.assertEqual(sorted(add([3, 2, 4], 6)), [1, 2])

    def test_case_3(self):
        self.assertEqual(sorted(add([3, 3], 6)), [0, 1])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)