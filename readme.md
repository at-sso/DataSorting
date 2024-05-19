# MinHeap and User Sorting

## Description

This project demonstrates the implementation of a `User` class and a `MinHeap` class to sort users by age, and then by name if ages are the same. The `MinHeap` class is used to maintain a heap data structure, allowing for efficient insertion and extraction of the smallest element.

## Files

- `main.py`: Contains the implementation of the `User` and `MinHeap` classes, and demonstrates their usage.
- `sorters.py`: May contain additional sorting-related utility functions.

## Classes

### User

A class representing a user with a name and age.

#### Attributes

- `name_param` (str): The name of the user.
- `age_param` (int): The age of the user.

#### Methods

- `__init__(self, name: str, age: int) -> None`: Initializes a User instance with the given name and age.
- `__lt__(self, other: Any) -> bool`: Compares two User instances first by age, then by name.
- `__repr__(self) -> str`: Returns a string representation of the User instance.

### MinHeap

A class representing a minimum heap for User instances.

#### Attributes

- `heap` (List[Any]): The underlying list representing the heap.

#### Methods

- `__init__(self) -> None`: Initializes an empty MinHeap instance.
- `insert(self, user: User) -> None`: Inserts a User instance into the heap.
- `extract_min(self) -> Any`: Extracts and returns the smallest User instance from the heap.
- `is_empty(self) -> bool`: Checks if the heap is empty.

## Usage

To run the demonstration, execute the `main.py` file. The script will:

1. Create a list of `User` instances.
2. Insert the users into a `MinHeap`.
3. Extract users from the heap in sorted order and print them.

### Example

Also provided [here](main.py)!

```python
from sorters import *

users: List[User] = [
    User("Alice", 30),
    User("Bob", 25),
    User("Charlie", 25),
    User("Dave", 35),
    User("Eve", 30),
]

heap = MinHeap()

# Insert users into the heap
for user in users:
    heap.insert(user)  # Add each user to the heap

sorted_users: List[Any] = []
while not heap.is_empty(): # Extract users from the heap until it is empty
    sorted_users.append(heap.extract_min())  # Remove the smallest user from the heap

# Print the result.
print("Sorted users:")
for user in sorted_users:
    print(user)
```

## Output

The script will print the users in sorted order first by age, and then by name if ages are the same. For the example provided, the output will be:

```
Sorted users:
Bob (25)
Charlie (25)
Alice (30)
Eve (30)
Dave (35)
```

## Requirements

- Python +3.10.12.
  Ensure the `sorters.py` file is in the same directory as `main.py` if it contains additional required functions or classes.
