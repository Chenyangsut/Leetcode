#-*-coding:utf-8-*-
# 001 two sum 两数之和
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
# nums = [2,7,11,15]
# target = 9
# for i in range(0,len(nums)):
#     res = []
#     for j in range(0,len(nums)):
#         if nums[i] + nums[j] == target:
#             res = [i,j]
#             print res
#             break
#         else:
#             pass
#     if res != None:
#         break


