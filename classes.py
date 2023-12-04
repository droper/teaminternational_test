"""
Challenge code
"""


class FenwickTree:
    """
    Fenwick Tree data structure for efficient range queries and updates.
    """

    def __init__(self, size: int) -> None:
        """
        Initialize a FenwickTree with a given size.

        Args:
            size (int): The size of the Fenwick Tree.
        """
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """
        Update the Fenwick Tree by adding a delta value at a specific index.

        Args:
            index (int): The index to update.
            delta (int): The value to add at the specified index.
        """
        if index > self.size:
            raise ValueError(f"Number {index} outside range \n"
                             f"Range is: [0 - {self.size}]")
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        """
        Query the prefix sum up to a specific index.

        Args:
            index (int): The index for the prefix sum query.

        Returns:
            int: The prefix sum up to the specified index.
        """
        if index > self.size:
            raise ValueError(f"Number {index} outside range \n"
                             f"Range is: [0 - {self.size}]")
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class DataStats:
    """
    DataStats object for querying statistics about the inputs in a DataCapture object.
    """

    def __init__(self, tree_less: FenwickTree, tree_between: FenwickTree,
                 tree_greater: FenwickTree, biggest_number: int) -> None:
        """
        Initialize a DataStats object with Fenwick Trees.

        Args:
            tree_less (FenwickTree): Fenwick Tree for less than queries.
            tree_between (FenwickTree): Fenwick Tree for between queries.
            tree_greater (FenwickTree): Fenwick Tree for greater than queries.
        """
        self.tree_less = tree_less
        self.tree_between = tree_between
        self.tree_greater = tree_greater
        self.biggest_number = biggest_number

    def less(self, value: int) -> int:
        """
        Query how many numbers in the collection are less than a specific value.

        Args:
            value (int): The value to compare.

        Returns:
            int: The count of numbers less than the specified value.
        """
        return self.tree_less.query(value - 1)

    def between(self, lower: int, upper: int) -> int:
        """
        Query how many numbers in the collection are within a specific range.

        Args:
            lower (int): The lower bound of the range.
            upper (int): The upper bound of the range.

        Returns:
            int: The count of numbers within the specified range.
        """

        return self.tree_between.query(upper) - self.tree_between.query(lower - 1)

    def greater(self, value: int) -> int:
        """
        Query how many numbers in the collection are greater than a specific value.

        Args:
            value (int): The value to compare.

        Returns:
            int: The count of numbers greater than the specified value.
        """
        return self.tree_greater.query(self.biggest_number) - self.tree_greater.query(value)


class DataCapture:
    """
    DataCapture object accepts numbers and returns an object for querying statistics about the inputs.
    """

    biggest_number = 999

    def __init__(self) -> None:
        """
        Initialize a DataCapture object.
        """
        self.data = []
        self.tree_less = FenwickTree(self.biggest_number)
        self.tree_greater = FenwickTree(self.biggest_number)
        self.tree_between = FenwickTree(self.biggest_number)

    def add(self, num: int) -> None:
        """
        Add a number to the DataCapture object.

        Args:
            num (int): The number to add.
        """
        self.data.append(num)
        self.tree_less.update(num, 1)
        self.tree_greater.update(num, 1)
        self.tree_between.update(num, 1)

    def build_stats(self) -> DataStats:
        """
        Build statistics object based on the current state of the DataCapture object.

        Returns:
            DataStats: Statistics object for querying.
        """
        return DataStats(self.tree_less, self.tree_between, self.tree_greater, self.biggest_number)


if __name__ == "__main__":

    # Example usage:
    capture = DataCapture()
    capture.add(5)
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(4)
    capture.add(6)
    capture.add(6)
    capture.add(6)

    stats = capture.build_stats()
    print(stats.less(4))                    # should return 2
    print(stats.between(3, 6))   # should return 8
    print(stats.greater(4))                 # should return 5
