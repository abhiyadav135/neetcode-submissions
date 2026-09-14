class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = "", float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window_count[c] = window_count.get(c, 0) + 1

            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while have == need:
                # Update our minimum result
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = s[left : right + 1]

                # Pop from the left of our window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        return res