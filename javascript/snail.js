snail = function(array) {
  const snailArray = []
  let top = 0
  let bottom = array.length
  let left = 0
  let right = array[0].length

  while (top < bottom && left < right) {

    for (let i = left; i < right; i++) {
      snailArray.push(array[top][i])
    }
    top++

    for (let j = top; j < bottom; j++) {
      snailArray.push(array[j][right - 1])
    }
    right--

    if (top < bottom){
      for (let k = right - 1; k > left - 1; k--){
        snailArray.push(array[bottom -1][k])
      }
      bottom--
    }

    if (left < right){
      for (let l = bottom - 1; l > top - 1; l--) {
        snailArray.push(array[l][left])
      }
      left++
    }

  }
  return snailArray
}