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
            if char in mapping:  
                top_element = stack.pop() if stack else '#'  
                if mapping[char] != top_element:  
                    return False
            else:
                stack.append(char)  # It's an opening bracket, push onto the stack

        return not stack 





    



  

