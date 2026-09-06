class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {c:i for i,c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
              seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return"".join(stack)