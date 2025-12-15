Intuition

When first tackling this problem, the most natural thought is to check every possible pair of numbers to see if they add up to the target. This is the brute-force method. We could use a nested loop: the outer loop picks a number, and the inner loop iterates through the rest of the array, checking if the sum matches the target.

This approach would look like this:

    Take the first number, nums[0].

    Add it to every other number in the array (nums[1], nums[2], ...).

    If a pair sums to the target, we're done.

    If not, move to the second number, nums[1], and repeat the process.

For an array of size n, this means we'd be doing roughly n×n operations, leading to a time complexity of O(n2). Given the problem constraints (up to 104 elements), an O(n2) algorithm would be far too slow and would likely time out.

This clear inefficiency leads us to a crucial question: How can we find the second number (the "complement") faster than a linear search? We need a data structure that can tell us if we've seen a number before, and do it in constant time. This is the perfect job for a hash map.
Approach: One-Pass Hash Map

To achieve a faster solution, we can trade a bit of memory for a significant speed boost. The idea is to iterate through the array a single time, using a hash map to keep track of the numbers we've seen so far and their indices.

For each element in the array, we do the following:

    Calculate the complement we need to find (i.e., complement = target - current_number).

    Check if this complement already exists as a key in our hash map.

    If it exists, we've found our solution! The value associated with the complement's key is its index, and we have the index of our current number. We can return these two indices immediately.

    If it does not exist, we add the current number and its index to the hash map. This prepares us for future iterations, in case the current number is the complement for a number we haven't seen yet.

This one-pass strategy is extremely efficient because the hash map lookup is so fast.
Complexity

    Time complexity: O(n)

We iterate through the array of n elements exactly once. For each element, the hash map lookup and insertion operations take constant time on average, O(1). Therefore, the total time complexity is linear.

    Space complexity: O(n)

The extra space required is for the hash map. In the worst-case scenario, we might need to store all n elements in the map before finding a solution (e.g., if the two numbers are the last two in the array). Thus, the space complexity is proportional to the size of the input array.