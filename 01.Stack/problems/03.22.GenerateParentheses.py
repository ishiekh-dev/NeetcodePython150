from typing import List


class Solution:

    def generateParenthesis(self, n:int) -> List[str]:
        stack = []
        result = []

        def backtrack(openN, closedN):
            # my base condition for recursion
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN  + 1)
                stack.pop()

        backtrack(0 , 0)
        return result