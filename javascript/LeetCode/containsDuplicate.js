/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
  var obj = {};
  for (var i = 0; i < nums.length; i++) {
    if(obj[nums[i]] !== undefined) {
      return true;
    }
    obj[nums[i]] = true;
  }
  return false
};