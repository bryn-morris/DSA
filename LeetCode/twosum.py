


#Test Values
tc1 = [1,7,9,13,-4,37,0]
tc2 = [6,7,2,1,-5,3,3]

## For use with tc1
tt1 = 9
tt2 = 33

## For use with tc2
tt3 = 6
tt4 = -4

class Solution(object):
    def twoSum(self, nums: 'list[int]', target: int) -> 'list[int]':
        
        # return 'is this working?'
        
        # nums_but_better = {}
        testing_value = 0

        for i,val in enumerate(nums):
            # nums_but_better[i] = val
            testing_value = nums[0]


soln1 = Solution()
print(soln1.twoSum(tc1,tt2))

## 
## Return List of Indices