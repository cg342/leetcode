class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = [1,5]
        count = 1
        ind = 0
        # arr = [2,3,4,7,11], k = 5
        while len(missing) != k:
            if ind < len(arr):
                if arr[ind] != count:
                    missing.append(count)
                else:
                    ind += 1
                count += 1
            else:
                missing.append(count)
                count += 1

        return  missing[-1]
             
                