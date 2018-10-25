def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """


    if s == '':
        return 0
    longest_len = 1
    curr = []
    for x in s:
        if x in curr:
            index = curr.index(x)
            curr = curr[index + 1:]
            print (curr)
        curr.append(x)
        # print(curr)
        if longest_len < len(curr):
            longest_len = len(curr)
    return longest_len

longest_len = lengthOfLongestSubstring("abaacbca")
print (longest_len)