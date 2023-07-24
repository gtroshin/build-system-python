# Build System

This project contains Python scripts that address various coding challenges. Each script can be run standalone, and they do not have any external dependencies beyond the Python Standard Library.

## Getting Started

### Prerequisites

The scripts are written in Python. Ensure you have Python installed on your machine. The Python version used for these scripts is Python 3.9+. 

### Installation

1. Clone the repo
   ```
   git clone https://github.com/gtroshin/build-system-python.git
   ```
2. Navigate to the project directory
   ```
   cd build-system-python
   ```

## Usage

Here is how to run each script:

1. `set_of_stacks.py` - This script can be run as follows:
   ```
   python3 set_of_stacks.py
   ```

2. `genealogical_data.py` - Before running this script, ensure the `genealogical_data.csv` file is in the same directory. Then, you can run the script as follows:
   ```
   python3 genealogical_data.py
   ```

3. `tower.py` - This script can be run as follows:
   ```
   python3 tower.py
   ```

4. `log_errors_counter.py` - This script takes two command line arguments, the start and end week numbers for which to count the errors. Here is how you can run it:
   ```
   python3 log_errors_counter.py <start_week> <end_week>
   ```

Replace `<start_week>` and `<end_week>` with the desired week numbers.

Please note that the `log_errors_counter.py` script expects log files to be in a directory named "logs" in the same directory as the script itself. For testing purposes, there are test logs already included.

## Details

### Question 1

[See implementation](set_of_stacks.py).

The `SetOfStacks` class implementation allows you to push and pop items onto and from a set of stacks. 
When a stack reaches its maximum capacity, a new stack is created and subsequent items are added to the new stack. 
When a stack becomes empty, it is removed from the set of stacks.

The push method adds an item to the last stack in `self.stacks`, creating a new stack if necessary.

The pop method removes and returns the last item from the last stack, removing the last stack if it becomes empty (unless it's the only stack).

### Question 2

[See implementation](genealogical_data.py) and [some test data](genealogical_data.csv).

This code first defines a Person class to represent individuals. The GenealogicalData class represents the genealogical data as an adjacency list. The add_person method adds a person to the data, and the add_parent_child method adds a parent-child relationship.

The are_biologically_related method uses a BFS approach (Breadth-First Search) to check if a person1 and a person2 are related. It starts with a person1 and checks all of their descendants, marking each visited person to avoid cycles. If it encounters person2 during this process, it returns True, indicating that person1 and person2 are related. If it checks all descendants of a person1 without encountering the person2, it returns False.

This implementation has a time complexity of O(V + E), where V is the number of people and E is the number of parent-child relationships. The space complexity is also O(V + E), for storing the adjacency list and the queue. While this isn't the most efficient possible solution, it should be reasonably efficient for a graph of this size, provided that the graph is somewhat sparse (i.e., each person doesn't have too many direct descendants). If the graph is very dense, a different approach might be needed.

### Question 3

[See implementation.](set_of_stacks.py)

This issue is a variant of the Longest Increasing Subsequence (LIS) problem, where I am looking for the longest subsequence of boxes where each box is both shorter and lighter than the previous box. It can be solved by using dynamic programming.
If I had more time, I would consider using a more efficient algorithm for finding the longest increasing subsequence. The dynamic programming solution has a time complexity of O(n^2), where n is the number of boxes. There are more efficient algorithms for the LIS problem that run in O(n log n) time, but they are more complex to implement. One such approach involves maintaining multiple active lists and using binary search to decide where to place the next element. This would likely involve a more complex data structure and more complicated update logic.

### Question 4

[See implementation](log_errors_counter.py) and [test data (logs)](logs/).

Memory and run-time imperatives of a program:    

1. **Runtime:** The script peruses each log record line by line, so the time complexity is O(n), where n is the full number of lines overall log records. On the off chance that the number of log sections increments, the runtime will increment straightly. In any case, perusing records line by line is for the most part very quick, so the script ought to still perform well indeed with huge log records.   

2. **Memory:** The script stores unique errors per client in a settled lexicon, where the keys are the usernames and the values are sets of unique errors. Hence, memory utilization is relative to the number of unique errors overall for clients. On the off chance that the number of one-of-a-kind errors or the number of clients increments essentially, memory utilization will moreover increment. In any case, since we're only putting away error messages and not the whole log passages, the memory utilization ought to still be sensible indeed with an expansive number of errors. 
