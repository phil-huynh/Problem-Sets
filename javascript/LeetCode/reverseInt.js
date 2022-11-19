/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
  if (x === 0) {return 0}
  if (x < 0) {
    var isNegative = true
  }
  var copy = Math.abs(x)
  var reversed = 0;
  while (copy) {
    if (copy < 10) {
      reversed += copy
      if (isNegative) {
        if ((0 - reversed) <= -(2**31)) {
          return 0;
        }
        return 0 - reversed
      }
      if (reversed >= ((2**31) - 1)) {
        return 0;
      }
      return reversed
    }
    var onesPlace = copy % 10;
    reversed += onesPlace;
    reversed *= 10;
    copy = (copy - onesPlace)/10;
  }
};