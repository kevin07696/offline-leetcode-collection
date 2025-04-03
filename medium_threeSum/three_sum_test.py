import unittest
from typing import List, NamedTuple, Set, Tuple
from .three_sum import threeSum

class TestThreeSum(unittest.TestCase):
    class Test(NamedTuple):
        title: str
        nums: List[int]
        expectedTriplets: Set[Tuple[int, int, int]]

    test_cases: List[Test] = [
        Test(
            "Test_FindsATriplet",
            [0, -1, 1],
            {(-1, 0, 1)},
        ),
        Test(
            "Test_IfLeftRepeats",
            [0, 0, -1, 1],
            {(-1, 0, 1)},
        ),
        Test(
            "Test_IfInternalLeftRepeats",
            [0, 0, 0, -1, 1],
            {(0, 0, 0), (-1, 0, 1)},
        ),
        Test(
            "Test_IfRightRepeats",
            [0, 0, 0, -1, 1, 1],
            {(0, 0, 0), (-1, 0, 1)},
        ),        
    ]

    def test_threeSum(self):
        for case in self.test_cases:
            with self.subTest(case.title):
                result = threeSum(self, case.nums)
                self.assertEqual(len(case.expectedTriplets), len(result), 
                    f"Expected length: {len(case.expectedTriplets)} does not equal result length: {len(result)}.\nResult: {result}")
                for i in range(len(result)):
                    result[i].sort()
                    self.assertTrue(tuple(result[i]) in case.expectedTriplets)

