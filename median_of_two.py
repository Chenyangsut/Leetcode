#-*-coding:utf-8-*-
# Median of Two Sorted Arrays 两个有序数组的中位数
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5
nums1 = [1,3]
nums2 = [2]
nums3 = nums1 + nums2
nums3 = sorted(nums3)
i = len(nums3)/2
if len(nums3)%2 == 0:
    median = float(nums3[i-1]+nums3[i])/2
else:
    median = nums3[i]
print 'the median is %s'%median