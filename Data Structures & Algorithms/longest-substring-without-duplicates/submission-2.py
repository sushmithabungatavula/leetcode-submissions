class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_len=0
        # for i in range(len(s)):
        #     seen=set()
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #     max_len=max(max_len, len(seen))
        # return max_len

        seen=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len, right-left+1)
        return max_len
            

            











        # seen=[]
        # cnt=0
        # max_cnt=0
        # for i in range(len(s)):
        #     if s[i] not in seen:
        #         seen.append(s[i])
        #         cnt+=1
        #         max_cnt=max(max_cnt,cnt)
        #     else:
        #         cnt=1
        # return max_cnt
        