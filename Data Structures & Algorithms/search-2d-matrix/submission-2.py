class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) # num of rows and cols
        top, bot = 0, rows - 1 # indices for top and bottom rows

        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]: # right-most value in the row
                top = mid_row + 1
            elif target < matrix[mid_row][0]: # left-most value in the row
                bot = mid_row - 1
            else:
                break # break when found the row potentially containing target

        # if no rows showing potential target    
        if not(top <= bot):
            return False
        
        row = (top + bot) // 2 # get the row with most updated top and bot
        # binary search for row

        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
        

