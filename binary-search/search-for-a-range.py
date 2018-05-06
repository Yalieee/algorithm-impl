class Solution(object):

    def binSearch(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        left = 0
        right = length - 1

        pos = None
        # find target first
        pos = self.binSearch(nums, target)

        if pos is None:
            return [-1, -1]

        # find left bound
        leftBound = self.binSearch(nums[0:pos], target)
        if leftBound is not None:
            while True:
                newBound = self.binSearch(nums[0:leftBound], target)
                if newBound is None:
                    break
                else:
                    leftBound = newBound

        # find right bound
        rightBound = self.binSearch(nums[pos+1:length], target)
        if rightBound is not None:
            rightBound = pos + 1 + rightBound
            while True:
                newBound = self.binSearch(nums[rightBound+1:length], target)
                if newBound is None:
                    break
                else:
                    rightBound = rightBound + 1 + newBound

        if leftBound is None and rightBound is None:
            return [pos, pos]
        elif leftBound is None:
            return [pos, rightBound]
        elif rightBound is None:
            return [leftBound, pos]
        else:
            return [leftBound, rightBound]


sol = Solution()
assert sol.searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert sol.searchRange([1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8], 8) == [15, 18]
