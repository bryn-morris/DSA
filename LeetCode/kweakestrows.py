#         """
#         :type mat: List[List[int]]
#         :type k: int
#         :rtype: List[int]
#         """

## Test Cases

mat1 = [   
        [1,0,0,0],
        [1,1,1,0],
        [1,1,0,0],
        [1,1,1,0],
    ]

mat2 = [
        [1,1,0,0],
        [1,0,0,0],
        [1,1,1,0],
        [1,0,0,0],
    ]

## Types  to convert to type hints
## return Value = List[int]
## k = int
## mat = List[List[int]

class Solution(object):
    def kWeakestRows(self, mat, k):

        # Variables
        m = len(mat)
        
        ## Constraints
        if m > 100 or k < 1 or k > m:
            return 'Constraint Error 1'
        for li in mat:
            if len(li) < 2:
                return 'Constraint Error 2'
            
            for el in li:
                if el != 0 and el != 1:
                    return 'Constraint Error 3'
        
        # Solution Code

        # Refactor to list comprehension
        strength_dict = {}

        for i, list in enumerate(mat):
            strength_dict[i] = sum(list)

        sorted_strength_vo = sorted(strength_dict.items(), key = lambda j:j[1])

        return_list = []
        
        for tup in sorted_strength_vo:
            if len(return_list) <= k-1:
                return_list.append(tup[0])

        return return_list

        # Notes
        ## Refactor to recursive loop for bonus points

sol1 = Solution()
print(sol1.kWeakestRows(mat1, 1))