"""
Test for the challenge
"""

import unittest

from classes import DataCapture, DataStats, FenwickTree


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

        # Assuming FenwickTree is correctly implemented
        self.assertEqual(data_stats.less(100), 1)
        self.assertEqual(data_stats.between(0, 50), 1)
        self.assertEqual(data_stats.greater(10), 1)


class TestDataStats(unittest.TestCase):
    """Test cases for the DataStats class."""

    def setUp(self):
        """Set up a DataCapture object with some sample data."""
        biggest_number = 9
        tree_less = FenwickTree(biggest_number)
        tree_between = FenwickTree(biggest_number)
        tree_greater = FenwickTree(biggest_number)

        tree_less.update(3, 1)
        tree_less.update(5, 1)
        tree_less.update(8, 1)

        tree_between.update(3, 1)
        tree_between.update(5, 1)
        tree_between.update(8, 1)

        tree_greater.update(3, 1)
        tree_greater.update(5, 1)
        tree_greater.update(8, 1)

        self.stats = DataStats(tree_less, tree_between, tree_greater, biggest_number)

    def test_less(self):
        """Test the less method of DataStats."""
        self.assertEqual(self.stats.less(4), 1)  # one values (3, ) is less than 4

    def test_between(self):
        """Test the between method of DataStats."""
        self.assertEqual(self.stats.between(3, 6), 2)   # two values (3, 5) between 3 and 6

    def test_greater(self):
        """Test the greater method of DataStats."""
        self.assertEqual(self.stats.greater(4), 2)  # two values (5, 8) are greater than 4


class TestFenwickTree(unittest.TestCase):
    """Test cases for the FenwickTree class."""

    def test_update_query(self):
        """Test the update and query methods of FenwickTree."""
        fenwick_tree = FenwickTree(10)
        fenwick_tree.update(3, 2)
        fenwick_tree.update(5, 1)
        fenwick_tree.update(8, 3)

        self.assertEqual(fenwick_tree.query(3), 2)
        self.assertEqual(fenwick_tree.query(5), 3)
        self.assertEqual(fenwick_tree.query(8), 6)
        self.assertEqual(fenwick_tree.query(10), 6)

    def test_invalid_update(self):
        """Test that updating with an invalid index raises a ValueError."""
        fenwick_tree = FenwickTree(5)

        with self.assertRaises(ValueError):
            fenwick_tree.update(6, 2)  # Index out of bounds

    def test_invalid_query(self):
        """Test that querying with an invalid index raises a ValueError."""
        fenwick_tree = FenwickTree(5)

        with self.assertRaises(ValueError):
            fenwick_tree.query(6)  # Index out of bounds


if __name__ == '__main__':
    unittest.main()
