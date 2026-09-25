class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False

        if len(s)!=len(t):
            return False
        hash_s=[]
        hash_t=[]
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0)+1
            hash_t[t[i]] = hash_t(t[i],0)+1
            if hash_s==has_t:
                return True
            else:
                return False