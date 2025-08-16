class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        need_count = len(t)
        left = 0
        result = ""
        min_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] <= need[ch]:
                need_count -= 1

            while need_count == 0:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right+1]

                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    need_count += 1
                left += 1

        return result