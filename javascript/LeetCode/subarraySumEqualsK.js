/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
*/
var subarraySum = function(nums, k) {
  var count = 0;
  for (var i = 0; i < nums.length; i++) {
    var total = 0
    for (var j = i; j < nums.length; j++) {
      total += nums[j]
      if(total === k) {
        count += 1;
      }
    }
  }
  return count;
};