"""
Challenge code
"""

from typing import Dict


class DataStats:
    """
    Class that Calculates statistics for the data
    """

    def __init__(self, data: Dict, total_numbers: int, biggest_number: int) -> None:
        """
        Initialize DataStats with given data and the biggest number.

        Args:
            data (List): List of numbers.
            biggest_number (int): The biggest number in the data.
        """
        if not isinstance(data, Dict):
            raise TypeError("Data must be a dictionary")
        if not isinstance(total_numbers, int):
            raise TypeError("total_numbers must be an integer.")
        if not isinstance(biggest_number, int):
            raise TypeError("biggest_number must be an integer.")

        # Sort the data for efficient calculations
        self.data = data

        # The biggest number in the range
        self.biggest_number = biggest_number

        # Size of the range including the biggest number
        self.size = biggest_number + 1

        # Dictionaries to store accumulated counts for less and greater operations
        self.less_dict = {}
        self.greater_dict = {}

        # Calculate accumulated counts for numbers less and greater than each element
        acum = 0
        for i in range(self.size):
            self.less_dict[i] = acum
            if i in self.data:
                acum += self.data[i]
            self.greater_dict[i] = total_numbers - acum

    def less(self, value: int) -> int:
        """
        Get the count of numbers less than a specified value.

        Args:
            value (int): The value to compare.

        Returns:
            int: The count of numbers less than the specified value.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")

        if value > self.biggest_number or value < 0:
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
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")

        if value > self.biggest_number or value < 0:
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
        if not isinstance(lower, int) or not isinstance(upper, int):
            raise TypeError("Lower and upper bounds must be integers.")

        if upper < lower:
            raise ValueError(f"upper limit can't be lower than lower limit!!!")
        if lower > self.biggest_number or lower < 0:
            raise ValueError(f"Number {lower} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")
        elif upper > self.biggest_number or upper < 0:
            raise ValueError(f"Number {upper} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")

        # If the upper value is in the elements list then add the number of
        # repetitions of the upper number
        if upper in self.data:
            return self.data[upper] + self.less_dict[upper] - self.less_dict[lower]
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
        self.data = {}
        self.total_numbers = 0

    def add(self, num: int) -> None:
        """
        Add a number to the DataCapture object.

        Args:
            num (int): The number to add.
        """
        if not isinstance(num, int):
            raise TypeError(f"Invalid type for 'num'. Expected int, got {type(num).__name__}")

        if num > self.biggest_number or num < 0:
            raise ValueError(f"Number {num} outside range \n"
                             f"Range is: [0 - {self.biggest_number}]")

        # Populate elem_dict with counts for each element
        if num in self.data:
            self.data[num] += 1
        else:
            self.data[num] = 1

        self.total_numbers += 1

    def build_stats(self) -> DataStats:
        """
        Build statistics object based on the current state of the DataCapture object.

        Returns:
            DataStats: Statistics object for querying.
        """
        return DataStats(self.data, self.total_numbers, self.biggest_number)


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

