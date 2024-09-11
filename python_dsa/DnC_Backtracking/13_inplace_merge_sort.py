
class Solution(object):

    def merge(self, arr, s, e):
        total_len = e-s+1
        gap = total_len//2 + total_len%2

        while(gap>0):
            i=s
            j=s+gap
            while(j<=e):
                if arr[i]>arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j+=1

            if gap==1:
                break
            gap= gap//2 + gap%2


    def merge_sort(self, arr, s, e):
        if s>=e:
            return
        mid = s + (e - s) // 2
        self.merge_sort(arr, s, mid)
        self.merge_sort(arr, mid+1, e)
        self.merge(arr, s, e)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.merge_sort(nums, 0 , len(nums)-1)
        return nums
