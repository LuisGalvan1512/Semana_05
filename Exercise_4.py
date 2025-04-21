from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    max_values = []
    dq = deque()  

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values

#Test

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# Output: [3, 3, 5, 5, 6, 7]

print(sliding_window_max([4, 2, 12, 3, 8], 2))
# Output: [4, 12, 12, 8]

print(sliding_window_max([9, 11], 2))
# Output: [11]

print(sliding_window_max([], 3))
# Output: []

print(sliding_window_max([10, 5, 2, 7, 8, 7], 3))
# Output: [10, 7, 8, 8]
