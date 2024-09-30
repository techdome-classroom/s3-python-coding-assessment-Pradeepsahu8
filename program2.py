class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

          roman_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s:
            value = roman_to_value[char]
            # If the current value is greater than the previous value,
            # we subtract twice the previous value (as it was added before)
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value

        return total
        pass




