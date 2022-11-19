var twoSum = function(nums, target) {
  var differences = {}
  for (var i = 0; i < nums.length; i++) {
    if (differences[nums[i]] !== undefined) {
      return [differences[nums[i]], i]
    }
    differences[target - nums[i]] = i ;
  }
  return null;
};