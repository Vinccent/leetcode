def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    sets = set(s)
    flag, res = 0, 0
    for letter in sets:
        num = s.count(letter)
        if num % 2 == 0:
            res += num
        else:
            flag = 1
            res += num - 1
    return res + flag