class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1 = []
        stack2 = []
        for token in s:
            if token == ')':
                while stack1[-1]:
                    if stack1[-1] == '(':
                        stack1.pop()
                        stack1 += stack2
                        stack2 = []
                        break
                    else:
                        stack2.append(stack1.pop())
            else:
                stack1.append(token)
        return ''.join(stack1)