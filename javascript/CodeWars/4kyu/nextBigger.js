/*
https://www.codewars.com/kata/55983863da40caa2c900004e/javascript

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
*/

function nextBigger(n){
  n = n.toString()
  let index;
  let last;
  for (let i = n.length - 1; i >= 0; i--) {
    if (i === n.length - 1 && n[i] === 0) { continue }
    if (i === 0 && n[i] >= last) { return -1 }
    if (!last || Number(n[i] >= last)) { last = Number(n[i]) }
    else if (Number(n[i]) < last) {
      index = i
      break
    }

  }
  let front = n.slice(0, index)
  let end = n.slice(index)
  let lowest = end[1]
  let lowIndex = 1
  end = end.split('')
  for (let j = 1; j < end.length; j++) {
    if(Number(end[j]) < lowest && Number(end[0]) < Number(end[j])) {
      lowest = Number(end[j])
      lowIndex = j
    }
  }
  end[lowIndex] = end[0]
  end[0] = lowest.toString()
  let piece = end.slice(1)
  piece.sort()
  let final = [end[0]]
  piece.forEach((num) => {
    final.push(num)
  })
  final = final.join("")
  result = `${front}${final}`
  return Number(result)
}