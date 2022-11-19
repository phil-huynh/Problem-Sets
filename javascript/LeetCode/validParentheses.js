/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
  if (s.length === 1) {return false}
  var array = s.split('')
  var close = [];
  for (var i = 0; i < array.length; i ++) {
    if(array[i] === '(') {
      close.push(')')
    }
    if(array[i] === '[') {
      close.push(']')
    }
    if(array[i] === '{') {
      close.push('}')
    }
    if(array[i] === ')' || array[i] === ']' || array[i] === '}') {
      let correctClose = close.pop();
      if (array[i] !== correctClose) {
        return false;
      }
    }
  }
  if (close.length !== 0) {return false}
  return true;
};

