class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1          # 마지막 인덱스. len은 개수라 1 크다

        while left < right:
        # 알파벳/숫자가 아니면 건너뛴다
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False        # 한 쌍이라도 다르면 즉시 끝

            left += 1
            right -= 1

        return True