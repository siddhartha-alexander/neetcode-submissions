class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        dici=dict(sorted(dici.items(),key=lambda x : x[1],reverse=True))
        m=list(dici.keys())[:k]
        return m