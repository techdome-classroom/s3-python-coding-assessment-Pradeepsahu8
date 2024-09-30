class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Use '#' as a placeholder for an empty stack
                if mapping[char] != top_element:  # Check if it matches the expected opening bracket
                    return False
            else:
                stack.append(char)  # It's an opening bracket, push onto the stack

        return not stack 





    



  

