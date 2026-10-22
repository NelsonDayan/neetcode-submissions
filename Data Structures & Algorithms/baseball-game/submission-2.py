class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=0
        stack=[]
        for i in range(len(operations)):
            print(stack)
            if operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                score = 2*stack[-1]
                stack.append(score)
            elif operations[i] == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            else:
                score = int(operations[i])
                stack.append(score)
        return sum(stack)