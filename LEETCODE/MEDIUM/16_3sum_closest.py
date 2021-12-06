class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        pass

    def threeSumClosestBruteForce(self, nums, target) -> int:
        nums.sort()
        closest = float("-inf")


if __name__ == "__main__":
    nums, target = [1,1,1,0], -100
    s = Solution()
    print(s.threeSumClosestBruteForce(nums, target))
    #print(s.threeSumClosest(nums, target))