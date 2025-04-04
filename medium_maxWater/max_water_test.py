import unittest
from typing import List, NamedTuple, Set, Tuple
from .max_water import maxArea

class TestMaxWaterContainer(unittest.TestCase):
    class Test(NamedTuple):
        title: str
        heights: List[int]
        expectedArea: int

    test_cases: List[Test] = [
        Test(
            "Test_Area_WithMaxHeights",
            [1,7,2,5,4,7,3,6],
            36,
        ),
        Test(
            "Test_Area_WithEqualHeights",
            [2,2,2],
            4,
        ),
        Test(
            "Test_Area_WithMaxWidths",
            [1,1,4,5,1,1],
            5,
        ),       
    ]

    def test_MaxArea(self):
        for case in self.test_cases:
            with self.subTest(case.title):
                area = maxArea(case.heights)
                self.assertEqual(case.expectedArea, area, 
                    f"Expected area: {case.expectedArea} does not equal result: {area}")

