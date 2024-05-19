__all__ = ["User", "MinHeap"]

from typing import Any, List
import heapq


class User:
    """
    A class representing a user with a name and age.

    Attributes:
        name_param (str): The name of the user.
        age_param (int): The age of the user.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.
        """
        self.name_param: str = name
        self.age_param: int = age

    def __lt__(self, other: Any) -> bool:
        """
        Compares two User instances first by age, then by name.

        Args:
            other (Any): Another User instance to compare against.

        Returns:
            bool: True if this User instance is considered less than the other, False otherwise.
        """
        if self.age_param == other.age_param:
            return self.name_param < other.name_param
        return self.age_param < other.age_param

    def __repr__(self) -> str:
        """
        Returns a string representation of the User instance.

        Returns:
            str: The string representation of the User instance.
        """
        return f"{self.name_param} ({self.age_param})"


class MinHeap:
    """
    A class representing a minimum heap for User instances.

    Attributes:
        heap (List[Any]): The underlying list representing the heap.
    """

    def __init__(self) -> None:
        """
        Initializes an empty MinHeap instance.
        """
        self.heap: List[Any] = []

    def insert(self, user: User) -> None:
        """
        Inserts a User instance into the heap.

        Args:
            user (User): The User instance to insert.
        """
        heapq.heappush(self.heap, user)

    def extract_min(self) -> Any:
        """
        Extracts and returns the smallest User instance from the heap.

        Returns:
            Any: The smallest User instance in the heap.
        """
        return heapq.heappop(self.heap)

    def is_empty(self) -> bool:
        """
        Checks if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0
