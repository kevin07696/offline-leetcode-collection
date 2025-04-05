import unittest
from typing import List, NamedTuple, Set, Tuple
from .trap_rain import trap

class TestMaxWaterContainer(unittest.TestCase):
    class Test(NamedTuple):
        title: str
        heights: List[int]
        expectedWaterUnits: int

    test_cases: List[Test] = [
        Test(
            "Test_Convex",
            [0,1,0,2,1,0,1,3,2,1,2,1],
            6,
        ),
        Test(
            "Test_Flat",
            [2,2,2],
            0,
        ),
        Test(
            "Test_Concave",
            [4,2,0,3,2,5],
            9,
        ),       
    ]

    def test_Trap(self):
        for case in self.test_cases:
            with self.subTest(case.title):
                water = trap(case.heights)
                self.assertEqual(case.expectedWaterUnits, water, 
                    f"Test Case: {case.title}: Expected water units: {case.expectedWaterUnits} does not equal result: {water}")

