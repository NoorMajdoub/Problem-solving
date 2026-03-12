class Solution(object):
    def isPalindrome(self, s):
            ll = 0
            rr = len(s)-1
            while ll < rr:
                    while ll < rr and not s[ll].isalnum():
                        ll += 1
                    while ll < rr and not s[rr].isalnum():
                          rr -= 1
                    if s[ll].lower() != s[rr].lower():
                        return False
                    ll += 1
                    rr -= 1
            return True
