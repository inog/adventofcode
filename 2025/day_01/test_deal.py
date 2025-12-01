import unittest

from dial import rotate_dial, count_0_in_sequence, count_all_0_in_sequence


class TestDialRotation(unittest.TestCase):
    parameters = [
        ('L', 68),
        ('L', 30),
        ('R', 48),
        ('L', 5),
        ('R', 60),
        ('L', 55),
        ('L', 1),
        ('L', 99),
        ('R', 14),
        ('L', 82),
    ]

    def test_left_rotation(self):
        self.assertEqual(rotate_dial(50, 'L', 68), 82)

    def test_right_rotation(self):
        self.assertEqual(rotate_dial(50, 'R', 48), 98)

    def test_sequence(self):
        result = 50

        for direction, value in self.parameters:
            result = rotate_dial(result, direction, value)
            print(f"The dial is rotated {direction} {value} to point at {result}")

        self.assertEqual(result, 32)

    def test_sequence_and_count_0(self):
        self.assertEqual(count_0_in_sequence(self.parameters), 3)

    def test_sequence_and_count_all_0(self):
        self.assertEqual(count_all_0_in_sequence(self.parameters), 6)

if __name__ == '__main__':
    unittest.main()
