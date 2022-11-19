/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
  if (x < 0) {return false}
  if (x < 10) {return true}
  var reversed = 0;
  var copy = x
  while (copy) {
    var onesPlace = copy % 10;
    let newNum = (copy - onesPlace)/10;
    reversed += onesPlace;
    if (reversed === x) {return true}
    reversed *= 10;
    copy = newNum;
  }
  return false;
};

// var isPalindrome = function(x) {
//   if (x < 0) {return false}
//   var reversed = 0;

//   var reverseInt =(num) => {
//     if (num < 10) {
//       reversed += num;
//       return
//     }
//     var onesPlace = num % 10;
//     reversed += onesPlace;
//     reversed *= 10;
//     let newNum = (num - onesPlace)/10;
//     reverseInt(newNum);
//   }
//   reverseInt(x);
//   if (x !== reversed) {
//     return false;
//   }
//   return true;
// };