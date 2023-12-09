"""
Test for the challenge
"""

import unittest

from classes import DataCapture, DataStats


class TestDataCapture(unittest.TestCase):
    """Test cases for the DataCapture class"""

    def test_add_valid_number(self):
        """Test that adding a valid number updates the data list."""
        data_capture = DataCapture()
        data_capture.add(42)
        self.assertIn(42, data_capture.data)

    def test_add_invalid_number(self):
        """Test that adding an invalid number raises a ValueError."""
        data_capture = DataCapture()
        with self.assertRaises(ValueError):
            data_capture.add(1000)

    def test_build_stats(self):
        """Test building stats from a DataCapture object."""
        data_capture = DataCapture()
        data_capture.add(42)
        data_stats = data_capture.build_stats()

        self.assertEqual(data_stats.less(100), 1)
        self.assertEqual(data_stats.between(0, 50), 1)
        self.assertEqual(data_stats.greater(10), 1)

    def test_build_stats_empty_capture(self):
        """Test building stats from an empty DataCapture object."""
        data_capture = DataCapture()
        data_stats = data_capture.build_stats()
        # Ensure the returned object is an instance of DataStats
        self.assertIsInstance(data_stats, DataStats)
        # Add more specific assertions based on expected behavior with an empty capture

    def test_add_argument_type(self):
        """Test that add method raises TypeError for non-integer argument."""
        data_capture = DataCapture()
        with self.assertRaises(TypeError):
            data_capture.add("invalid")


class TestDataStats(unittest.TestCase):
    def test_less(self):
        """
        Test the less method of DataStats.
        """
        data = [3, 5, 8, 3, 2, 6, 8]
        biggest_number = 9
        data_stats = DataStats(data, biggest_number)

        # Test less method with valid input
        self.assertEqual(data_stats.less(4), 3)  # Expected result: two values (3, 3) are less than 4
        self.assertEqual(data_stats.less(9), 7)  # Expected result: all values are less than 10

        # Test less method with invalid input (outside range)
        with self.assertRaises(ValueError):
            data_stats.less(-1)  # Expected result: ValueError for a number outside the range
        with self.assertRaises(ValueError):
            data_stats.less(10)  # Expected result: ValueError for a number outside the range

        # Test invalid argument type (string)
        with self.assertRaises(TypeError):
            data_stats.less("invalid")

    def test_greater(self):
        """
        Test the greater method of DataStats.
        """
        data = [3, 5, 8, 3, 2, 6, 8]
        biggest_number = 9
        data_stats = DataStats(data, biggest_number)

        # Test greater method with valid input
        self.assertEqual(data_stats.greater(4), 4)  # Expected result: four values (5, 6, 8, 8) are greater than 4
        self.assertEqual(data_stats.greater(2), 6)  # Expected result: Six values are greater than 2 (all except 2)

        # Test greater method with invalid input (outside range)
        with self.assertRaises(ValueError):
            data_stats.greater(-1)  # Expected result: ValueError for a number outside the range
        with self.assertRaises(ValueError):
            data_stats.greater(10)  # Expected result: ValueError for a number outside the range

        # Test invalid argument type (float)
        with self.assertRaises(TypeError):
            data_stats.greater(3.5)

    def test_between(self):
        """
        Test the between method of DataStats.
        """
        data = [3, 5, 8, 3, 2, 6, 8]
        biggest_number = 9
        data_stats = DataStats(data, biggest_number)

        # Test between method with valid input
        self.assertEqual(data_stats.between(3, 6), 4)  # Expected result: four values between 3 and 6
        self.assertEqual(data_stats.between(0, 9), 7)  # Expected result: all values are between 0 and 10

        # Test between method with invalid input (outside range)
        with self.assertRaises(ValueError):
            data_stats.between(3, -1)  # Expected result: ValueError for lower bound outside the range
        with self.assertRaises(ValueError):
            data_stats.between(3, 10)  # Expected result: ValueError for lower bound outside the range
        with self.assertRaises(ValueError):
            data_stats.between(-1, 7)  # Expected result: ValueError for upper bound outside the range
        with self.assertRaises(ValueError):
            data_stats.between(11, 15)  # Expected result: ValueError for upper bound outside the range
        with self.assertRaises(ValueError):
            data_stats.between(5, 4)  # Expected result: ValueError for upper bound outside the range

        # Test invalid argument type (list)
        with self.assertRaises(TypeError):
            data_stats.between([3, 6], 8)

        # Test invalid argument type (boolean)
        with self.assertRaises(TypeError):
            data_stats.between(2, "True")


if __name__ == '__main__':
    unittest.main()
