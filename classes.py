"""
Challenge code
"""

from typing import List


class DataStats:
    """
    Class that Calculates statistics for the data
    """

    def __init__(self, data: List, biggest_number: int) -> None:
        """
        Initialize DataStats with given data and the biggest number.

        Args:
            data (List): List of numbers.
            biggest_number (int): The biggest number in the data.
        """

        # Sort the data for efficient calculations
        self.data = sorted(data)

        # The biggest number in the range
        self.biggest_number = biggest_number

        # Size of the range including the biggest number
        self.size = biggest_number + 1

        # Dictionary to store the count of each element
        self.elem_dict = {}

        # Dictionaries to store accumulated counts for less and greater operations
        self.less_dict = {}
        self.greater_dict = {}

        # Populate elem_dict with counts for each element
        for i in self.data:
            if i in self.elem_dict:
                self.elem_dict[i] += 1
            else:
                self.elem_dict[i] = 1

        # Calculate accumulated counts for numbers less than each element
        acum = 0
        for i in range(self.size):
            self.less_dict[i] = acum
            if i in self.elem_dict:
                acum += self.elem_dict[i]

        # Calculate accumulated counts for numbers greater than each element
        acum = 0
        for i in reversed(range(self.size)):
            self.greater_dict[i] = acum
            if i in self.elem_dict:
                acum += self.elem_dict[i]

    def less(self, value: int) -> int:
        """
        Get the count of numbers less than a specified value.

        Args:
            value (int): The value to compare.

        Returns:
            int: The count of numbers less than the specified value.
        """
        if value > self.size or value < 0:
            raise ValueError(f"Number {value} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")
        return self.less_dict[value]

    def greater(self, value: int) -> int:
        """
        Get the count of numbers greater than a specified value.

        Args:
            value (int): The value to compare.

        Returns:
            int: The count of numbers greater than the specified value.
        """
        if value > self.size or value < 0:
            raise ValueError(f"Number {value} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")
        return self.greater_dict[value]

    def between(self, lower: int, upper: int) -> int:
        """
        Get the count of numbers within a specified range.

        Args:
            lower (int): The lower bound of the range.
            upper (int): The upper bound of the range.

        Returns:
            int: The count of numbers within the specified range.
        """
        if lower > self.size or lower < 0:
            raise ValueError(f"Number {lower} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")
        elif upper > self.size or upper < 0:
            raise ValueError(f"Number {upper} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")

        # If the upper value is in the elements list then add the number of
        # repetitions of the upper number
        if upper in self.elem_dict:
            return self.elem_dict[upper] + self.less_dict[upper] - self.less_dict[lower]
        return self.less_dict[upper] - self.less_dict[lower]


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

    def add(self, num: int) -> None:
        """
        Add a number to the DataCapture object.

        Args:
            num (int): The number to add.
        """
        self.data.append(num)

    def build_stats(self) -> DataStats:
        """
        Build statistics object based on the current state of the DataCapture object.

        Returns:
            DataStats: Statistics object for querying.
        """
        return DataStats(self.data, self.biggest_number)


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

