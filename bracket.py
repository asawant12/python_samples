# code to print multiple valid combinations of paranthesis

class Solution(object):
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
           self.backtrack(S+'(', left+1, right)
        if right < left:
           self.backtrack(S+')', left, right+1)
    def generateParenthesis(self, N):
        ans = []
        self.backtrack()

        
        return ans
