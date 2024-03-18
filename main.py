def twoSum(nums,target):
  n=0
  for item in nums:
    for x in range(n,len(nums)):
      if item+nums[x] == target and n != x :
        return [n,x]
    n+=1
  return []
print(twoSum([3,2,4],6 ))
print(twoSum([3,3],6 ))
print(twoSum([2,7,11,15],9))
print(twoSum([7,11,15],9))