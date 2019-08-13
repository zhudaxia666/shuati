class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0: return 0
        candy_nums = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_nums[i] = candy_nums[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_nums[i - 1] = max(candy_nums[i - 1], candy_nums[i] + 1)
        return sum(candy_nums)