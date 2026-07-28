class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        remaining = len(students)
        count = {1:0, 0:0}
        for s in students:
            count[s] += 1
        
        for s in sandwiches:
            if count[s] > 0:
                remaining -= 1
                count[s] -= 1
            else:
                return remaining
        return remaining

