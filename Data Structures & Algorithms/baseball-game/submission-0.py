class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
                if op == "+":
                    score = scores[-1] + scores[-2]
                    scores.append(score)
                elif op == "D":
                    score = scores[-1]*2
                    scores.append(score)
                elif op == "C":
                    scores.pop(-1)
                else:
                    score = int(op)
                    scores.append(score)
        return sum(scores)

            