/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
  var prefix = '';
  var add = true;
  var first = strs[0];
  for (var i = 0; i < first.length; i++) {
    for (var j = 0; j < strs.length; j++) {
      if (first[i] !== strs[j][i]) {
        add = false;
      }
    }
    if (add) {
        prefix += first[i]
    } else {
        break;
    }
  }
  return prefix;
};