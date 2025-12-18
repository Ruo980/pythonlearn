class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 二分法查找法：注意开闭区间和终止条件的关系
        i: int = 0
        j: int = len(nums) - 1
        mid: int = 0
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target: #二是 nums[mid],不是 nums[i]+nums[j]
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    nums: list[int] = list(
        map(int, input().split(","))
    )  # 使用 map 转为迭代器,然后使用 list 进行转换
    target: int = int(input())
    solution: Solution = Solution()
    result = solution.search(nums, target)
    print(result)
