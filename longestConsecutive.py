class Solution(object):
    def longestConsecutive(nums):
        if not nums:
            return 0
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak  = max(longest_streak ,current_streak)

        return longest_streak

    nums = [1,3,5,2,4]
    print(longestConsecutive(nums))