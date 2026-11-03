class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = []
        for detail in details:
            age = int(detail[11:13])
            ages.append(age)
        count = 0
        for age in ages:
            if age > 60:
                count += 1
        return count