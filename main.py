from typing import Any, List
from sorters import *

if __name__ == "__main__":
    # Create a list of User instances.
    users: List[User] = [
        User("Alice", 30),
        User("Bob", 25),
        User("Charlie", 25),
        User("Dave", 35),
        User("Eve", 30),
    ]

    # Initialize a MinHeap instance.
    minheap = MinHeap()

    # Insert users into the heap
    for user in users:
        minheap.insert(user)  # Add each user to the heap.

    # Prepare to extract and display users in order.
    sorted_users: List[Any] = []

    # Extract users from the heap until it is empty.
    while not minheap.is_empty():
        sorted_users.append(minheap.extract_min())

    # Print the sorted users
    print("Sorted users:")
    for user in sorted_users:
        print(user)  # Print each user in sorted order.
