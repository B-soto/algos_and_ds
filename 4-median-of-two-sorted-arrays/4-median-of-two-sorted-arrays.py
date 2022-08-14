class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
#         Merge two sorted arrays
        index1, index2 = 0, 0
        merged_array = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                merged_array.append(nums1[index1])
                index1 +=1
            else:
                merged_array.append(nums2[index2])
                index2 +=1
        
        while index1 < len(nums1):
            merged_array.append(nums1[index1])
            index1 +=1
            
        while index2 < len(nums2):
            merged_array.append(nums2[index2])
            index2 +=1
            
        median = float(0)
        if len(merged_array) % 2 == 0: #even number of elements
            mid_index = len(merged_array) / 2 
            mid1 = merged_array[mid_index]
            mid2 = merged_array[mid_index-1]
            median = (float(mid1) + float(mid2)) / 2
        else:
            mid_index = len(merged_array) //2
            median = merged_array[mid_index]
            
        return median