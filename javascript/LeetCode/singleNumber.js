/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
  var obj = {};
  for (var i = 0; i < nums.length; i++) {
    if (obj[nums[i]] === true) {
      delete obj[nums[i]];
    } else {
      obj[nums[i]] === true;
    }
  }
  var key = Object.keys(obj).join();
  return obj[key]
};