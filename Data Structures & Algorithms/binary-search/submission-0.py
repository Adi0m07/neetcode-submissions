class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(arr,x):
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = (low+high)//2
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    high = mid-1
                else:
                    low = mid+1
            return -1


        r = bs(nums,target)
        s=-1
        if r != -1:
            return r 
        else:
            return s
     
            
    