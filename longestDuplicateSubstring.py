class Solution(object):
    def search(self, s, length):
        MOD = 2**63 - 1  
        base = 26  

       
        def rolling_hash(s, length):
            hash_val = 0
            for i in range(length):
                hash_val = (hash_val * base + ord(s[i])) % MOD
            return hash_val

        seen = set()
        hash_val = rolling_hash(s, length)
        seen.add(hash_val)

        base_pow_length = pow(base, length, MOD)
        for i in range(1, len(s) - length + 1):
            
            hash_val = (hash_val * base - ord(s[i - 1]) * base_pow_length + ord(s[i + length - 1])) % MOD
            if hash_val in seen:
                return s[i:i + length]
            seen.add(hash_val)
        return ""

    def longestDupSubstring(self, s):
        left = 1
        right = len(s)
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            duplicate = self.search(s, mid)
            if duplicate:
                result = duplicate
                left = mid + 1
            else:
                right = mid - 1
        return result

s = "banana"
sln = Solution()
print(sln.longestDupSubstring(s))


#TRY YOURSELF

'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.
'''