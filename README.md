# Find pairs in an array with sum as target

## Question:
Given array, find all the pairs of numbers whose sum is a given target.


## Examples:

Arr = [3,7,9,4,8,2,6,11,14,16,12]
sorted_array = [2,3,3,4,6,7,8,9,11,12,12,14,16]
Target = 15

Output:
[7,8], [4,11], [3,12],[9,6]


## Algorithm:
1. Sort the array
1. Find the diff (desired pair) from the highest number in array
2. See if the lowest index is the diff, more than diff or less than diff
3. Increment and Decrement the two pointers as needed
